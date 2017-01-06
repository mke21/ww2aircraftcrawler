#!/usr/bin/env python3
import json
import os
import logging

from ww2crawler.walksite import walk_index, walk_thread
logging.basicConfig(level=logging.INFO)

import datetime

def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()


def threadname(part):
    return part.strip('/').split('/')[-1]

def main(outputfolder, base, forumpart):
    # set to keep track of used thread urls
    done = set()
    for base, threadpart in walk_index(base, forumpart):

        # if already done, ignore
        if threadpart in done:
            continue
        else: # not done yet
            # get threadname
            th = threadname(threadpart)
            logging.info('Downloading %s', th)
            
            json.dump(
                walk_thread(base, threadpart), # get all posts
                open(
                    os.path.join(
                        outputfolder,
                        th + '.json'
                        )
                    , 'w'
                    ),
                default = datetime_handler
                ) # saves as json
            done.add(threadpart) # register as done

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-b', '--base',
        default = 'https://ww2aircraft.net/forum/',
        help= 'standard part of the url, must have a trailing "/", default = https://ww2aircraft.net/forum/'
        )
    parser.add_argument(
        '-p', '--part',
        help = 'selective part of url that defines forum in url, f.i.: "topics/aviation.13/"'
        )
    parser.add_argument(
        '-o', '--outdir',
        help='Directory to save content'
        )
    args = parser.parse_args()    
    main(
        args.outdir,
        args.base,
        args.part
        )
