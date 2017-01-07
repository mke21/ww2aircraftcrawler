#!/usr/bin/env python3
from ww2crawler.makedatabase import insert_in_database

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--cache',
        help='Directory where json\'s are stored'
        )
    parser.add_argument(
        '-d', '--db',
        help="Database file"
        )
    args = parser.parse_args()    
    insert_in_database(args.cache, args.db)

