#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import protoroutines

keywords = ['парсинг','парсер','parser','python','oracle']
max_page = 10
delimiter = '|'
filename = 'data.csv'
filecodec = 'utf-8'
fields = ['title', 'ref', 'items']

proclist = [
            {'url': 'https://www.weblancer.net/jobs/?page={}',
             'shorturl': 'https://www.weblancer.net',
             'proc': protoroutines.weblancer,
             'codec': 'cp1251',
             'active': True
             },
            {'url': 'https://freelansim.ru/tasks?page={}',
             'shorturl': 'https://freelansim.ru',
             'proc': protoroutines.freelansim,
             'codec': 'utf-8',
             'active': True
            },
            {'url': 'https://moikrug.ru/vacancies?page={}&type=all',
             'shorturl': 'https://moikrug.ru',
             'proc': protoroutines.moikrug,
             'codec': 'utf-8',
             'active': True
            },
            {'url': 'https://www.fl.ru/projects/?page={}',
             'shorturl': 'https://www.fl.ru',
             'proc': protoroutines.flru,
             'codec': 'utf-8',
             'active': False
            },
            {'url': 'https://freelancehunt.com/projects?page={}',
             'shorturl': 'https://freelancehunt.com/projects',
             'proc': protoroutines.freelancehunt,
             'codec': 'utf-8',
             'active': True
            },
            {'url': 'https://pchel.net/jobs/page-{}/',
             'shorturl': 'https://pchel.net',
             'proc': protoroutines.pchelnet,
             'codec': 'utf-8',
             'active': False
             }
            ]

tasks_list = [proclist[i] for i in range(0,len(proclist)) if proclist[i]['active']]
process_count = len(tasks_list)
