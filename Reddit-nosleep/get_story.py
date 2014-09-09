#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import BeautifulSoup
import logging
import sys
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG,
                    stream=sys.stdout)
import re


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
    # Replace HTML paragraphs
    paragraph = re.compile('<p>(.*?)</p>')
    content = paragraph.sub(r'\n\1\\\\\n', content)
    # apostophes
    content = content.replace('&#39;', "'")
    content = content.replace('’', "'")
    # dots
    content = content.replace('...', "\\dots ")
    content = content.replace('…', "\\dots ")
    # Quotes
    content = content.replace('“', "&quot;")
    content = content.replace('”', "&quot;")
    paragraph = re.compile('"(.*?)"')
    content = paragraph.sub(r'\\enquote{\1}', content)
    paragraph = re.compile('&quot;(.*?)&quot;')
    content = paragraph.sub(r'\\enquote{\1}', content)
    return content


if __name__ == "__main__":
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-u", "--url", dest="url",
                        required=True,
                        help="a url where the story can be found",
                        metavar="URL")
    args = parser.parse_args()
    print(main(args.url))
