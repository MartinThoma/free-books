http://www.reddit.com/r/nosleep is a nice source for free stories.
Most stories are quite short, though.

The theme of the stories is mostly (only?) horror.

## Workflow
### Used regexes

To improve the content, I've used the following regexes.

#### Newlines

* Search: `<p>(.*?)</p>`
* Replace: `$1\\\\`

#### Special chars

* Search: `&#39;`
* Replace: `'`

* Search: `’`
* Replace: `'`

#### Quotes

* Search: `"(.*?)"`, `"(.*?)”`, `“(.*?)"`, `&quot;(.*?)&quot;`,`“(.*?)”`, 
* Replace: `\\enquote{$1}`

#### dots

* Search: `...`, `…`
* Replace: `\dots`

### Finish
* Make sure that the first letter is `\yinipar{\color{black}L}`
* Make sure that all `<` and `>` are away and all `&` and `#` are replaced.
* Run spell-checker: `aspell --lang=en --mode=tex check doc.tex`