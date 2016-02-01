http://www.reddit.com/r/nosleep is a nice source for free stories.
Most stories are quite short, though.

The theme of the stories is mostly horror, but there are also some stories
that are more difficult to categorize.


## About this project

This is a repository for stories in a high quality typsetting.


## Add new stories

### Workflow
* Get Data with `get_story.py`
* Make sure that the first letter is `\yinipar{\color{black}L}`
* Make sure that all `<` and `>` are away and all `&` and `#` are replaced.
* Run spell-checker: `aspell --lang=en --mode=tex check doc.tex`
* Check for numbers that might need a protected space `~` or `num` formatting: `\d+`
* Check dashes

### Dashes

* Hyphen (`-`):
  * form compound modifiers (a well-attended event)
* En-dash (`--`):
  * indicate a range (read pages 162 -- 195; 4:00 p.m.--6:00 p.m.)
  * connect a prefix with an open compound (post--World War II; ex--vice president)
* Em-dash (`---`):
  * used in pairs to emphasize an element or elements within a sentence
  * show an abrupt change in thought
  * show interrupted dialogue

Source: http://www.dailywritingtips.com/how-to-use-dashes/

### Series

Series should get the following at the end:

```latex
\clearpage
\section*{Stories of this series}

\begin{itemize}
    \item Story~1: Title 1
    \item Story~2: Title 2
    \item Story~3: Title 3
\end{itemize}
```