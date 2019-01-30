#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from multiprocessing import Pool
import protoconf


def run_parsing(task):
    """Run parsing all sites"""
    for page in range(1, protoconf.max_page):
        routine = lambda url: lambda shorturl: lambda keywords: lambda codec: task['proc'](url, shorturl, keywords, codec)
        routine(task['url'].format(str(page)))(task['shorturl'])(protoconf.keywords)(task['codec'])

def main():
    start_time = time.time()
    with Pool(protoconf.process_count) as p:
        try:
            p.map(run_parsing, protoconf.tasks_list)
        except:
            print("Stop parsing")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
