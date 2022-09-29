import datetime
from urllib.parse import urlparse
import re
import json as js
import requests
from bs4 import BeautifulSoup
import requests as req
import tldextract
from track import Track
from logs import log


def dtn_int() -> str:
    return "".join([i for i in str(datetime.datetime.now()) if i.isdigit()])


def is_url_valid(url: str) -> bool:
    """

    :param url:
    :return: bool
    """
    subdomain = tldextract.extract(url).subdomain
    url = urlparse(url)
    netloc = url.netloc
    path = url.path
    if subdomain and any((not path.split("/") or path == "", "album" in path.split("/")[0: 2],
                          "track" in path.split("/")[0: 2])) and 'bandcamp' in netloc:
        return True
    return False


def get_url_type(url: str) -> str | None:
    """

    :param url:
    :return: artist|album|track|None
    """
    subdomain = tldextract.extract(url).subdomain
    url = urlparse(url)
    netloc = url.netloc
    path = url.path
    if subdomain:
        if not path.split("/") or path == "":
            log('url type is artist')
            return 'artist'
        elif "album" in path.split("/")[0: 2]:
            log('url type is album')
            return "album"
        elif "track" in path.split("/")[0: 2]:
            log('url type is track')
            return "track"
    log('url type undefined', mode='warning')
    return None


def get_page(url: str) -> requests.Response:
    log("getting page")
    resp = req.request('get', url)
    return resp


def extract_artist_url(url):
    url = urlparse(url)
    return f"{url.scheme}://{url.netloc}"


def parse(url: str) -> list[Track]:
    url_type = get_url_type(url)
    tracks = []
    artist_url = extract_artist_url(url)
    match url_type:
        case "artist":
            albums = parse_albums(url=url)
            tr_urls = []
            for album in albums:
                tr_urls.extend(parse_tracks(album, artist_url))
            for tr in tr_urls:
                tracks.append(parse_track(tr))

        case "album":
            tr_urls = parse_tracks(url, artist_url)
            for tr in tr_urls:
                tracks.append(parse_track(tr))

        case "track":
            tracks.append(parse_track(url))
    return tracks


def parse_albums(url: str) -> tuple:
    """
    :param url:
    :return: tuple of the albums links
    """
    log('starting parse albums')
    page = get_page(url)
    log('page got')
    soup = BeautifulSoup(page.text, "html.parser")
    albums = soup.find('ol', attrs={"id": "music-grid"})
    res = []
    for i in albums.find_all('li'):
        link = i.find('a', href=True)['href']
        res.append(url.rstrip('/') + link)
    log('albums parsed')
    return tuple(res)


def parse_tracks(url: str, artis_url: str) -> tuple:
    """
    :param url:
    :param artis_url:
    :return: tuple of the tracks links
    """
    log('parse tracks starting')
    page = get_page(url)
    res = []
    log('page got')
    soup = BeautifulSoup(page.text, "html.parser")
    tracks = soup.find('table', attrs={"id": "track_table"})
    if tracks is None:
        log(f"tracks parsing error while parsing {url}")
        log(f"try to parse track")
        try:
            res.append(parse_track(url))
            log(f"trying  is successful")
        except:
            log(f"trying failed")
        return tuple(res)
    else:
        tracks = tracks.find_all('tr', attrs={'class': 'track_row_view linked'})
    for track in tracks:
        link = track.find('a', href=True)['href']
        res.append(artis_url.rstrip('/') + link)
    log('tracks parsed')
    return tuple(res)


def parse_track(url) -> Track:
    """
    :param url:
    :return: Track
    """
    log('parse track starting')
    page = get_page(url)
    log('page got')
    soup = BeautifulSoup(page.text, "html.parser")
    script = soup.find('script', attrs={"data-tralbum": True})
    log('script parsed')
    # print(script)
    data = script.attrs.get('data-tralbum')
    data = js.loads(data)
    log('track data extruding')
    trackinfo = data['trackinfo'][0]
    taa = parse_track_title_album_artist(html=page.text)
    artist = taa['artist']
    album = taa['album']
    title = taa['title']
    lyrics = trackinfo['lyrics']
    files = trackinfo['file']
    log(f'track data extruded: {artist=}; {album=}; {title=}')
    # print(artist, album, title, files, lyrics)
    # will work too:
    # artist = data['artist']
    # title = trackinfo['title']
    return Track(url=url, artist=artist, album=album, title=title, lyrics=lyrics, files=files)


def parse_track_title_album_artist(url: str = None, html: str = None) -> dict | None:
    """
    set url or html
    :param url: if url is specified, html will be loaded from url
    :param html: if the url is not specified, the html will be obtained from the html variable
    :return: dict of artist name, album name, title
    """
    if url is not None:
        page = get_page(url)
        if not page:
            return None
        html = page.text
    elif url is html is None:
        return None
    soup = BeautifulSoup(html, "html.parser")
    name_section = soup.find("div", attrs={"id": "name-section"})

    album = name_section.find("span", attrs={"class": "fromAlbum"})
    if album is not None:
        album = album.text.strip()
    else:
        # album = f"unknown album - {dtn_int()}"
        album = f"unknown album"

    title = name_section.find("h2", attrs={"class": "trackTitle"})
    if title is not None:
        title = title.text.strip()
    else:
        title = f"untitled - {dtn_int()}"
    band_name = soup.find("p", attrs={"id": "band-name-location"})
    artist = band_name.find("span", attrs={"class": "title"}).text.strip()
    return {"artist": artist, "album": album, "title": title}


if __name__ == '__main__':
    pass
    # print(extract_artist_url('https://radostmoja.bandcamp.com/album/suitsid'))
    # print(parse_tracks('https://radostmoja.bandcamp.com/album/suitsid'))
    # print(parse_albums('https://radostmoja.bandcamp.com/'))
    # t = parse_track("https://radostmoja.bandcamp.com/track/zerkalo-polina-adovskaja")
    # get_url_type('https://radostmoja.bandcamp.com/')
    # print(parse_track("https://radostmoja.bandcamp.com/track/begi-tuda-gde-net-nikogo"))
    # print(parse_track_title_album_artist("https://radostmoja.bandcamp.com/track/begi-tuda-gde-net-nikogo"))
