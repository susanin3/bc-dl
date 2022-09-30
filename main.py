import tldextract
from urllib.parse import urlparse

import logs
import parser
from track import Track
import argparse


def main():
    for url in URLS:
        logs.log("\n\ndownloading from: " + url)
        if parser.is_url_valid(url):
            tracks = parser.parse(url)
            for t in tracks:
                if LOCATION:
                    t.location = LOCATION
                t.download(create_lyrics_file=CREATE_LYRICS_FILE, sort_by_aa=SORT)


# print("!!!!!", args.u)

if __name__ == '__main__':
    arpar = argparse.ArgumentParser(description='Bandcamp music downloader')
    arpar.add_argument('-u', type=str, help='Url of the artist|album|track', required=False)
    arpar.add_argument('-f', type=str, help='File one or more urls of the artist|album|track. '
                                            'Each link should be on a separate line', required=False)
    arpar.add_argument('-l', type=str, help='Location of downloaded files. '
                                            'The music files will be sorted into folders of artists and albums.',
                       required=False)
    arpar.add_argument('-t', type=str, help='Create lyrics file. 1 - create, 0 - don\'t create, default - 0', required=False)
    arpar.add_argument('-s', type=str, help='Don\'t sort by artists and albums directories. 1 - sort, 0 - don\'t sort, default - 0', required=False)
    args = arpar.parse_args()
    URLS = []
    LOCATION = None
    CREATE_LYRICS_FILE = False
    SORT = True

    if args.s:
        s = args.s.strip()
        SORT = True if s == "1" else False if s == "0" else None
        if SORT is None:
            logs.log("-s must be 0 or 1", mode="error")

    if args.t:
        t = args.t.strip()
        CREATE_LYRICS_FILE = True if t == "1" else False if t == "0" else None
        if CREATE_LYRICS_FILE is None:
            logs.log("-t must be 0 or 1", mode="error")

    if args.l:
        LOCATION = args.l

    if args.f:
        with open(args.f, 'r', encoding="UTF-8") as f:
            URLS.extend([i.strip().strip("/") for i in f.readlines() if not i.startswith("#")])
            f.close()

    if args.u:
        URLS.append(args.u.strip().strip("/"))

    if not URLS:
        logs.log("there are not any valid urls", mode="error")
        quit(0)
    else:
        main()
    pass
    # main('https://radostmoja.bandcamp.com')
