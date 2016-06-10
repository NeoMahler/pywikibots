# -*- coding: utf-8 -*-

# This scripts replaces a given text for another text in all wiki pages. You just need two configuration settings:

oldtext = u"some text here" # Here you can put the old text you want to replace
newtext = u"a nice new text here!" # Here you can put the new text that will replace oldtext

import pywikibot as pwb
import pagegenerators as pg

def replace(text, antiga, nova):
    if not antiga in text:
        pass
    else:
        noutext = text.replace(antiga, nova)
        page.text = noutext
        page.save("Bot: Replacing -%s; +%s." % (antiga, nova))

if __name__ == '__main__':
    site = pwb.Site()
    for page in list(pg.AllpagesPageGenerator(site=site)):
        replace(page.text, oldtext, newtext)
