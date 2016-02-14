# -*- coding: utf-8 -*-

# This script adds internal link for the given pages on *all* pages of a wiki (only main namespace).
#
# BEFORE running this script you should edit the variables below (and obtain permission from the community to run the bot)

import pywikibot as pwb
from pywikibot import pagegenerators as pg
import urllib
import json
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')

###################################
## EDIT THE FOLLOWING DICTIONARY ##
###################################
paraules = { # Add the word using regexp and next to it, the word without regexp (see the example). You can add an infinite amount of words.
        u' ([Pp]ag(e|es))( |\.|\,)': u'Page',
        }

def main(page, paraula):
    if page.title() == paraules[paraula]:
        print(u"Skipping %s because is the link page" % str(page))
        return
    substitucio = ' [[' + paraules[paraula] + '|\\1]]\\3'
    #site = pwb.Site()
    #page = pwb.Page(site, page)
    print(u"Page: %s" % page)
    text = page.text
    comptador = re.search(paraula, text)
    if comptador:
        print("======= EDITING PAGE %s! =======" % page)
        noutext = re.sub(paraula, substitucio, text)
        page.text = noutext
        page.save(u'Bot: Adding links for %s' % paraules[paraula])
    else:
        print("No links added")
        return
    
if __name__ == '__main__':
    allpages = pg.AllpagesPageGenerator(site=pwb.Site(), start="!", namespace=0, includeredirects = True)
    pages = pg.PreloadingGenerator(allpages, pageNumber = 100)
    for page in pages:
        for paraula in paraules:
            main(page, paraula)
    print("\nFinished!")
