"""This script generates the direct-download.md file."""

from typing import List, Literal, Tuple, Dict, Any, Optional
from pathlib import Path
import os
import yaml  # pyyaml
from urllib.parse import quote

from pydantic import BaseModel

LanguageCodes = Literal["en", "de", "fr"]  # Extend when necessary

code2language: Dict[LanguageCodes, str] = {
    "en": "English",
    "de": "German (Deutsch)",
    "fr": "French (Francais)",
}


class FreeBooksMeta(BaseModel):
    source: str
    source_file: str  # Needs to have at least one dot in it


class OriginalBookData(BaseModel):
    language: LanguageCodes
    title: str


class BookSeries(BaseModel):
    title: str  # Title in the current language, NOT the original language
    order: int  # Order for the current book; int starting at 1


class BookMeta(BaseModel):
    book_meta_version: int
    language: LanguageCodes
    title: str
    author: str  # Last name, First name(s)
    series: Optional[BookSeries]=None
    original: OriginalBookData
    free_books_project: FreeBooksMeta


def main(directory: Path):
    directory = os.path.abspath(directory)
    book_meta_files = get_book_meta_files(directory)
    metas = [
        (book_meta_file, parse_book_meta(book_meta_file))
        for book_meta_file in book_meta_files
    ]
    meta_dict = restructure_list(metas)
    md = generate_markdown(meta_dict)
    save_md("direct-download.md", md)


def get_book_meta_files(directory: Path) -> List[Path]:
    data = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename != "book-meta.yaml":
                continue
            filepath = os.path.abspath(os.path.join(root, filename))
            data.append(filepath)
    return data


def parse_book_meta(book_meta_file: str) -> BookMeta:
    with open(book_meta_file, "r") as stream:
        return BookMeta.parse_obj(yaml.safe_load(stream))


def restructure_list(metas: List[Tuple[Path, BookMeta]]):
    """First by language, then by author, then by title."""
    books = {}
    for meta in metas:
        language = meta[1].language
        author = meta[1].author
        if language not in books:
            books[language] = {}
        if author not in books[language]:
            books[language][author] = []
        books[language][author].append(meta)
    return books


def generate_markdown(books: Dict[str, Any]) -> str:
    md = "# Direct Download Page\n"
    for language_code, author_dict in sorted(books.items()):
        md += f"\n## {code2language[language_code]}\n"
        for author, books in sorted(author_dict.items()):
            # Maybe group series as well
            if len(books) == 1:
                pdf_link = get_file_link(books[0][0], books[0][1], ".pdf")
                epub_link = get_file_link(books[0][0], books[0][1], ".epub")
                md += f"\n* {author}: {books[0][1].title} ([PDF]({pdf_link}), [epub]({epub_link}))"
            else:
                md += f"\n* {author}: \n"
                for meta_path, book in sorted(books, key=lambda n: n[1].title):
                    pdf_link = get_file_link(meta_path, book, ".pdf")
                    epub_link = get_file_link(meta_path, book, ".epub")
                    md += f"    * {book.title} ([PDF]({pdf_link}), [epub]({epub_link}))\n"
    return md


def get_file_link(meta_path: Path, meta: BookMeta, extension: str) -> Path:
    base = "https://raw.githubusercontent.com/MartinThoma/free-books/master/"
    source_file = os.path.splitext(meta.free_books_project.source_file)[0]
    relative = os.path.dirname(meta_path.split("/free-books/")[1])
    return base + quote(relative + "/" + source_file + extension)


def save_md(destination: Path, content: str):
    with open(destination, "w") as fp:
        fp.write(content)


if __name__ == "__main__":
    main(Path("."))
