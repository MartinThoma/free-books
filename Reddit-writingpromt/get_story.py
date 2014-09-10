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
    if not text.endswith(suffix):
        return text.strip()
    return text[:len(text)-len(suffix)].strip()


def latex_escape(text):
    text = text.replace('$', "\\$")
    text = text.replace('#', "\\#")
    text = text.replace('_', "\\_")
    text = text.replace('%', "\\%")
    return text


def main(html):
    # Extract the content
    content = html

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
    #content = "".join(map(str, BeautifulSoup.BeautifulSoup(content).div.contents))
    content = content.strip()
    # Remove any non-ascii symbol
    content = ''.join([i if ord(i) < 128 else ' ' for i in content])
    content = "\yinipar{\color{black}%s}" % content[0] + content[1:]

    print(content)

html = """
<div class="md"><p>God was white. Thank you, Jesus. I don’t know what I would have done if I’d gone my whole life spreading the good Lord’s word just to get up to Heaven and find out that the godless liberals were right about him being some brown-skinned Arab.</p>

<p>They didn’t let me in to see Him right away, mind you. I mean, you wouldn’t believe the line to get in. Between the gays and the socialists and those Jews and muslims, I didn’t know that there were that many good people left on the Earth. From the looks of some of these yahoos, I started to wonder if St. Peter was hitting the sauce too hard when he made the big list, but as long as I was on it I wasn’t going to complain.</p>

<p>Not that there was ever a question I’d get in to see the big man. I’d gone to church since I was a little boy and I voted Republican since I was 17. I cheered at The Passion, booed outside of Planned Parenthood, and never once said “Happy Holidays” when I could wish someone a Merry Christmas. If there was a speed pass, I would have gone straight to the front.</p>

<p>Since I had time to kill, I looked for Cheryl. My sweet wife had left us two years back, but I didn’t see her in the crowd. I saw Bill from the office and my old Sunday school teacher Mrs. Jennings and nearly everyone else I knew who had passed on, but not Cheryl. She always was a bit too fond of her books about dragons and magic stuff, but she was good enough. I guess it’s not my place to question the Lord’s will.</p>

<p>The longer I stood in line, the more I realized that Heaven wasn’t nearly as fun as I thought it would be. Everyone was just standing around all mopey-like. Maybe they were just missing the folks who didn’t make the cut. I missed Cheryl something fierce, but she obviously didn’t put her heart into praying and spreading the word. Besides, there were a whole heap of pretty women here. Christian women.</p>

<p>“Hey!” I yelled out to the crowd with a laugh. “Cheer up already.  You’re in Heaven.”</p>

<p>A sweet young angel with blond hair escorted me to the front door. A golden light blinded me as I stepped into the room.</p>

<p>“It’s so bright,” my voice echoed across the mahogany walls of the hollow room. </p>

<p>“I should think so,” my Lord replied. “They do call me the Morning Star.”</p>

<p>As my eyes adjusted to the glow, I realized that this was not God. He was white, sure, but he had twisted goat’s horns and massive black wings that spread from wall to wall of this barren room.</p>

<p>“Beelzebub!” I shouted as my fists balled in holy rage.</p>

<p>“Oh please,” the devil laughed. “He is busy ruling over Hell. I am Lucifer, the one true lord of the kingdom of Heaven.”</p>

<p>“No. You were cast out of Heaven. Revelation 12:9. ‘So down the great dragon was hurled...’”</p>

<p>“You don’t have to quote the whole thing to me. It was my idea.”</p>

<p>“I don’t understand. How did this happen?”</p>

<p>“I asked Him. For someone so versed in scripture, you seem to forget that I was His companion and adviser. Your Creator hasn’t lived in this kingdom since time immemorial.”</p>

<p>“But why would he abandon us?”</p>

<p>“Abandon you?” Lucifer laughed with a force that shook the room. “Oh, that just never gets old. Let me ask you, Harris, have you seen your good wife since you’ve arrived here?”</p>

<p>“Well, no, but I just thought…”</p>

<p>“You thought she was in Hell? Cheryl? The woman who stayed with you even while you cursed her out nightly? The woman who regularly volunteered her time and gave to charity from her own pocket because you sure as hell weren’t going to help her out. What could she have possibly done to deserve eternal damnation?”</p>

<p>I knew the answer, but it just wasn’t coming to mind. She wasn’t here, so obviously she had done something wrong.</p>

<p>“Well then why isn’t she here in Heaven?” I shouted back.</p>

<p>“Cheryl never wanted Heaven, Harris,” Lucifer explained as if he’d done this a thousand times. “That was your obsession, not hers. You were blindly devoted to protesting and proselytizing to secure your spot up here, so here you are. She just wanted to be a good person and make life just slightly less horrible for everyone else.”</p>

<p>“So where is she?”</p>

<p>“At God’s side,” Lucifer said with a wide smile. “Where all good souls should be.”</p>

<p>He was lying. He had to be. He always lied. 2 Corinthians - “even Satan disguises himself as an angel of light.” John 8 - “there is no truth in him.” The chapters and verses were all there, and yet Cheryl wasn’t in Heaven.</p>

<p>Bill was here and he was so righteous that he gave himself a heart attack while yelling at girls outside of an abortion clinic. Mrs. Jennings was here and she was willing to disown her own son for turning his back on the Lord for his own deviant, sinful desires. These were all good people, devout people who had worked their whole lives to earn their spot in Heaven. Just like me.</p>

<p>I don’t know how I got out of Lucifer’s chamber. My feet had taken control while my mind was trying to find some answer. I was a good person, wasn’t I?</p>

<p>“Hey, asshole,” a voice from the line of new arrivals called out to me. “Cheer up already.  You’re in Heaven!”</p>
</div>
"""

main(html)
