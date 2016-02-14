# -*- coding: utf-8 -*-
#!/usr/bin/env python

# This script copies all articles from a given category and copies it to another wiki. The bot doesn't need an
# account on the first wiki, but it needs an account (and permission to edit) on the second wiki.
#
# The bot will comment templates, but you should check all articles imported with this bot as there may be some errors.
#
# BEFORE running it, edit the variables below

import pywikibot as pwb
import urllib
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

##################################
## EDIT THE FOLLOWING VARIABLES ##
##################################

categoria = None # The category from where you want to copy the articles
wiki = "https://ca.wikipedia.org/" # url of the wiki from where articles will be copied. Include the http:// and the final /!
catname = "Categoria:" # Local name of the Category namespace

################################
## DON'T TOUCH ANYTHING ELSE! ##
################################

if categoria == None:
    print("You must specify a category in order to run this program!")
    sys.exit()
wpapilink = wiki + 'w/api.php?action=query&list=categorymembers&cmtitle={0}&format=json&cmlimit=500&prop=info&inprop=url'
wprawlink = wiki + 'w/index.php?title={0}&action=raw'


def catmem(cat):
    """ Obtains all articles from a category """
    text = urllib.urlopen(wpapilink.format(cat)).read()
    print(text)
    data = json.loads(text)
    for pag in data['query']['categorymembers']:
         if pag['title'].startswith(catname):
             pass
         else:
             print(pag['title'])
             pagetext(pag['title'])
    #pagetext(data['query']['categorymembers'][0]['title'])
    
def pagetext(pagetitle):
    """ Modifies the text (comments all templates and replaces {{reflist}} by <references/>"""
    text = urllib.urlopen(wprawlink.format(pagetitle)).read()
    newtext = newtext.replace('{{Reflist}}', '<references/>')
    newtext = newtext.replace('{{', '<!-- TEMPLATE: {{').replace('}}', '}} END of template -->')
    print("\n\nMODIFIED TEXT WITH COMMENTED TEMPLATES:\n")
    print(newtext)
    createpage(newtext, pagetitle)
    
def createpage(text, title):
    """ Creates the page """
    site = pwb.Site()
    page = pwb.Page(site, title)
    if page.text != '':
        print("This page already exists... skipping it")
        return
    print(page.text)
    page.text = text
    page.save("Creating page from %stitle" % wiki)
    
catmem(categoria)
