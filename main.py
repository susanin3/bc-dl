import tldextract
from urllib.parse import urlparse

import logs
import parser
from track import Track
import argparse


def main():
    for url in URLS:
        logs.log("\n\n" + url)
        if parser.is_url_valid(url):
            tracks = parser.parse(url)
            for t in tracks:
                if LOCATION:
                    t.location = LOCATION
                t.download()


# print("!!!!!", args.u)

if __name__ == '__main__':
    arpar = argparse.ArgumentParser(description='Bandcamp music downloader')
    arpar.add_argument('-u', type=str, help='Url of the artist|album|track', required=False)
    arpar.add_argument('-f', type=str, help='File one or more urls of the artist|album|track. '
                                            'Each link should be on a separate line', required=False)
    arpar.add_argument('-l', type=str, help='Location of downloaded files. '
                                            'The music files will be sorted into folders of artists and albums',
                       required=False)
    args = arpar.parse_args()
    URLS = []
    LOCATION = None
    if args.l:
        LOCATION = args.l

    if args.f:
        with open(args.f, 'r', encoding="UTF-8") as f:
            URLS.extend([i.strip().strip("/") for i in f.readlines() if not i.startswith("#")])
            f.close()

    if args.u:
        URLS.append(args.u)

    if not URLS:
        logs.log("there are not any valid urls", mode="error")
        quit(0)
    else:
        main()
    pass
    # main('https://radostmoja.bandcamp.com')
