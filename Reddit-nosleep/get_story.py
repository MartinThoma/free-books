#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Get the content of a Reddit /nosleep and output LaTeX for a book."""

import requests
import BeautifulSoup
import logging
import sys
import os
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG,
                    stream=sys.stdout)
import re
from datetime import datetime
import shutil
import glob


def strip_end(text, suffix):
    """
    Remove suffix from text.

    Parameters
    ----------
    text : str
    suffix : str

    Returns
    -------
    str
    """
    if not text.endswith(suffix):
        return text.strip()
    return text[:len(text)-len(suffix)].strip()


def latex_escape(text):
    text = text.replace('$', "\\$")
    text = text.replace('#', "\\#")
    text = text.replace('_', "\\_")
    text = text.replace('%', "\\%")
    return text


def main(url):
    # Get the data
    headers = {'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/37.0.2062.94 Safari/537.36')}
    r = requests.get(url, headers=headers)
    html = r.text
    logging.info("Fetched %i characters from '%s'", len(html), url)

    # Extract the content
    soup = BeautifulSoup.BeautifulSoup(html)
    content = str(soup.findAll("div", {"class": "md"})[1])
    title = str(soup.find("title").text)
    title = strip_end(title, ": nosleep")
    title_url = title.replace(" ", "-")
    title_url = title_url.replace("/", "-")
    title_url = title_url.replace("_", "-")
    tagline = str(soup.find("p", {"class": "tagline"}))
    creat_time = BeautifulSoup.BeautifulSoup(tagline).find("time")['datetime']
    creat_time = datetime.strptime(creat_time[:-6], "%Y-%m-%dT%H:%M:%S")
    creat_time = datetime.strftime(creat_time, "%B %d, %Y")
    author_tag = BeautifulSoup.BeautifulSoup(tagline).find("a")
    author = author_tag.text
    author_url = author_tag['href']

    title = latex_escape(title)
    author = latex_escape(author)

    print("Title: %s" % title)
    print("Title URL: %s" % title_url)
    print("Date: %s" % creat_time)
    print("Author: %s" % author)
    print("Author url: %s" % author_url)

    # Replace HTML paragraphs
    paragraph = re.compile('<p>(.*?)</p>', re.DOTALL)
    content = paragraph.sub(r'\n\1\\\\\n', content)
    # apostophes
    content = content.replace('&#39;', "'")
    content = content.replace('’', "'")
    content = content.replace('‘', "'")
    # dashes and dots
    content = content.replace('–', "--")
    content = content.replace('...', "\\dots ")
    content = content.replace('…', "\\dots ")
    # dollars, hashes and underscores
    content = latex_escape(content)
    # Italic
    em = re.compile('<em>(.*?)</em>', re.DOTALL)
    content = em.sub(r'\\textit{\1}\n', content)
    # Bold
    bold = re.compile('<strong>(.*?)</strong>', re.DOTALL)
    content = bold.sub(r'\\textbf{\1}\n', content)
    # Quotes
    content = content.replace('“', "&quot;")
    content = content.replace('”', "&quot;")
    paragraph = re.compile('"(.*?)"')
    content = paragraph.sub(r'\\enquote{\1}', content)
    paragraph = re.compile('&quot;(.*?)&quot;')
    content = paragraph.sub(r'\\enquote{\1}', content)
    content = content.replace('&quot;', '"')
    content = "".join(map(str,
                          BeautifulSoup.BeautifulSoup(content).div.contents))
    content = content.strip()
    # Remove any non-ascii symbol
    content = ''.join([i if ord(i) < 128 else ' ' for i in content])
    # content = "\yinipar{\color{black}%s}" % content[0] + content[1:]

    # Create draft
    if not os.path.exists(title_url):
        shutil.copytree("template/", title_url)
    else:
        logging.info("The title '%s' does already exist.", title_url)
        sys.exit()
    # Rename main file
    shutil.move(os.path.join(title_url, "template.tex"),
                os.path.join(title_url, "%s.tex" % title_url))
    # Adjsut all files there
    os.chdir(title_url)
    for filename in glob.glob("*"):
        logging.info("Adjust '%s' ...", filename)
        with open(filename) as f:
            file_contents = f.read()
        file_contents = file_contents.replace("{{title}}", title)
        file_contents = file_contents.replace("{{date}}", creat_time)
        file_contents = file_contents.replace("{{title-url}}", title_url)
        file_contents = file_contents.replace("{{source}}", url)
        file_contents = file_contents.replace("{{author}}", author)
        file_contents = file_contents.replace("{{author-url}}", author_url)
        file_contents = file_contents.replace("{{content}}", content)
        with open(filename, "w") as f:
            f.write(file_contents)

if __name__ == "__main__":
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-u", "--url", dest="url",
                        required=True,
                        help="a url where the story can be found",
                        metavar="URL")
    args = parser.parse_args()
    main(args.url)
