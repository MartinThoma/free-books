free-books
==========

A repository for free books. The goal of this project is to provide
books that are fun to read and NOT to provide exact copies of the
original books. 

The sense of the texts should not get changed, but I want correct
punctuation and correct spelling of words and no footnotes that 
inform about these corrections.


Sources
=======
At the moment, the only book is from
http://www.sandroid.org/GutenMark/wasftp.GutenMark/MarkedTexts/

Rules for books
===============
All books that get uploaded have to match these rules:
 * Every single book has to have an own folder
 * A serie of books has to be in one folder 
   (e.g. all Sherlock Holmes books have to be in one folder and have
    their own folder)
 * The books have to be made with LaTeX
 * The LaTeX-document has to be encoded in utf-8 (check with $ file -bi [filename])
 * Every books has to have its own Makefile, with which it produces
   a PDF document