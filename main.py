import parser
from track import Track


def main():
    url = "https://radostmoja.bandcamp.com"
    tracks = parser.parse(url)
    # print(tracks)
    for t in tracks:
        t.download()


if __name__ == '__main__':
    main()
