from threading import Thread
from threading import get_ident
from threading import current_thread
from collections import defaultdict
from math import ceil
import pdb
import os.path
import requests
import random
import time
import pdb
import os


def download(status, url):
    chunk_size = 1024
    file_name = url.split("/")[len(url.split("/")) - 1]

    response = requests.get(url, stream=True)
    maximum = int(response.headers.get("Content-Length"))

    status[current_thread().name]['maximum'] = maximum
    status[current_thread().name]['current'] = 0

    with open(os.path.join("/home/halka/Desktop/courses/python_bootcamp", file_name), 'wb') as fd:
        for chunk in response.iter_content(chunk_size):
            status[current_thread().name]['current'] += 1024
            fd.write(chunk)

    '''for _ in range(maximum):
        time.sleep(random.random())
        status[current_thread().name]['current'] += 1'''


if __name__== "__main__":
    '''http://www.physikdidaktik.uni-karlsruhe.de/publication/Historical_Burdens.pdf,
       http://www.physik.uni-regensburg.de/forschung/rincke/Allgemeines/statement_strunk_rincke.pdf,
       http://www.physikdidaktik.uni-karlsruhe.de/kpk/english/KPK_Volume_1.pdf
    '''
    bars = 100
    status = defaultdict(dict)
    urls = ['http://www.physikdidaktik.uni-karlsruhe.de/publication/Historical_Burdens.pdf',
            'http://www.physik.uni-regensburg.de/forschung/rincke/Allgemeines/statement_strunk_rincke.pdf',
            'http://www.physikdidaktik.uni-karlsruhe.de/kpk/english/KPK_Volume_1.pdf']

    threads = []
    for url in urls:
        url_arr = url.split("/")
        thread = Thread(name=url_arr[len(url_arr) - 1], target=download, args=(status, url))
        thread.start()
        threads.append(thread)
        
    while True:
        # new line
        # the line
        print("I am the {} and I these are my slaves:".format(current_thread().name))
        
        lines = 0
        for thread in threads:
            # foreground u'\u2588'
            # background u'\u2591'
            s = status[thread.name]
            blanks = '                               '
            if 'maximum' in s and 'current' in s:
                if s['maximum'] / 1024 < s['current'] / 1024:
                    s['current'] = s['current'] - s['maximum'] // 1024
                foreground = ceil((s['current'] / s['maximum']) * bars)
                background = bars - foreground
                status_bar = ''.join([''.join(u'\u2588' for f in range(foreground)), ''.join(u'\u2591' for b in range(background))])
            
                print(thread.name + blanks[:-len(thread.name)], status_bar, '{}%'.format(ceil((s['current'] / s['maximum']) * 100)), )
                print("")

                lines += 2

        if any([thread.is_alive() for thread in threads]):
            time.sleep(0.1)
            print("\033[F" * (lines + 2))
        else:
            break

    
