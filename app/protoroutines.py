#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
import protoutils

def freelansim(url, shorturl, keywords, codec):
    rs = protoutils.get_html(url, codec)
    ts = protoutils.get_page_data(rs, "article", "task task_list")
    for t in ts:
        ref = shorturl + t.find('a').get("href")
        title = t.find('a').text.strip()
        items = ''
        for i in t.find_all('a', class_='tags__item_link'):
            items = items + ',' + i.text.lower()
        protoutils.append_data(title, ref, items, keywords)


def moikrug(url, shorturl, keywords, codec):
    rs = protoutils.get_html(url, codec)
    ts = protoutils.get_page_data(rs, "div", "info")
    for t in ts[5:]:
         ref = shorturl + t.find('a').get("href")
         title = t.find('div').get("title")
         items = ''
         for i in t.find_all('a', class_='skill'):
             items = items + ',' + i.text.lower()
         protoutils.append_data(title, ref, items, keywords)


def flru(url, shorturl, keywords, codec) :
    rs = protoutils.get_html(url, codec)
    ts = protoutils.get_page_data(rs,"div","b-post")
    for t in ts:
        ref = shorturl + t.find('a').get("href")
        title = t.find('a').text.strip()
        pattern = '(?<=<div\ class="b-post__txt\ ">).*?(?=</div>)'
        items = t.find('script',text=re.compile(pattern))
        item = re.search(pattern, items.text).group()
    protoutils.append_data(title, ref, item, keywords)

def freelancehunt(url, shorturl, keywords, codec) :
    rs = protoutils.get_html(url, codec)
    ts = protoutils.get_page_data(rs, "td", "left")
    for t in ts:
        ref = shorturl + t.find('a').get("href")
        title = t.find('a').text.strip()
        try:
            items = t.find('p').text.strip()
        except:
            try:
                items = t.find('small').text.strip()
            except:
                items = ""
        protoutils.append_data(title, ref, items, keywords)


def pchelnet(url, shorturl, keywords, codec):
    rs = protoutils.get_html(url, codec)
    ts = protoutils.get_page_data(rs, "div", "project-block-cont")
    for t in ts:
        ref = shorturl + t.find('a').get("href")
        title = t.find('a').text.strip()
        ptext = t.find('div', class_="project-text").text.strip().replace("\n"," ").replace("\r"," ")
        items = ''
        for i in t.find_all('div', class_='project-tags project-tags2'):
            items = items + ',' + i.text.lower().replace("\n"," ").strip()
        protoutils.append_data(title, ref, ptext+items, keywords)

def weblancer(url, shorturl, keywords, codec):
    rs = protoutils.get_html(url, codec)
    ts = protoutils.get_page_data(rs, "div", "row")
    for t in ts[1:-2]:
        ref = shorturl + t.find('a').get("href")
        title = t.find('a').text.strip()
        try:
            ptext = t.find('p', class_="text_field").text.strip().replace("\n"," ").replace("\r"," ")
        except:
            ptext = ''
        protoutils.append_data(title, ref, ptext, keywords)
