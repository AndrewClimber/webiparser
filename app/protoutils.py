#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import csv
from bs4 import BeautifulSoup
import protoconf

def get_html(url, codec):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    try:
        result = requests.get(url, headers = header)
        return (result.text).encode(codec)
    except:
        return str(result.status_code)

def write_csv(data):
    with open(protoconf.filename, 'a', newline='', encoding=protoconf.filecodec) as f:
        order = protoconf.fields
        writer = csv.DictWriter(f, fieldnames=order,delimiter=protoconf.delimiter)
        writer.writerow(data)

def get_page_data(html, tag_name, class_name):
    soup = BeautifulSoup(html,'lxml')
    result = soup.find_all(tag_name, class_=class_name)
    return result

def append_data(title, ref, items, keywords):
    """использование атрибута функции для борьбы с дублями."""
    if not hasattr(append_data, '_clist'):  # инициализация значения
        append_data._clist = []

    ti_ref = title + ref
    data = {'title': title, 'ref': ref, 'items': items}
    if len(keywords) > 0:
        for kw in keywords:
            if (ti_ref  not in append_data._clist) and \
               (items.lower().find(kw) != -1 or title.lower().find(kw) != -1):
                write_csv(data)
                append_data._clist.append(ti_ref)
    else:
        write_csv(data)
