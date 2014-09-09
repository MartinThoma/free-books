http://www.reddit.com/r/nosleep is a nice source for free stories.
Most stories are quite short, though.

The theme of the stories is mostly (only?) horror.

## Workflow
* Copy an already typeseted book
* Get Data with `get_story.py`
* Replace content with that from `get_story.py`
* Add author / title / first letter
* Finish

### Finish
* Make sure that the first letter is `\yinipar{\color{black}L}`
* Make sure that all `<` and `>` are away and all `&` and `#` are replaced.
* Run spell-checker: `aspell --lang=en --mode=tex check doc.tex`