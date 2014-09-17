http://www.reddit.com/r/nosleep is a nice source for free stories.
Most stories are quite short, though.

The theme of the stories is mostly horror, but there are also some stories
that are more difficult to categorize.

## Workflow
* Get Data with `get_story.py`
* Make sure that the first letter is `\yinipar{\color{black}L}`
* Make sure that all `<` and `>` are away and all `&` and `#` are replaced.
* Run spell-checker: `aspell --lang=en --mode=tex check doc.tex`
* Check for numbers that might need a protected space `~` or `num` formatting: `\d+`

## Series

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