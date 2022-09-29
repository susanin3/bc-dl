import os
import requests as req
import music_tag
from logs import log


def get_url_content(url: str) -> bytes:
    return req.get(url=url).content


def mk_path(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def clear_unavailable_symbols(text: str) -> str:
    return ("".join([i for i in text if not (i in r"\/:*?\"<>|+")])).replace(r"\u200b", "")


class Track:
    def __init__(self, url, artist, album, title, lyrics, files, cover=None, location="music"):
        """

        :param url:
        :param artist:
        :param album:
        :param title:
        :param lyrics:
        :param files:
        :param cover:
        :param location: directory with music
        """
        self.url = url
        self.artist = artist
        self.album = album
        self.title = title
        self.lyrics = lyrics
        self.files = files
        self.cover = cover
        self.location = location
        self.local_file = ""

    def download(self, location: str = None, dl_name: str = None, sort_by_aa: bool = True,
                 localize: bool = False) -> None:
        """
        :param location:
        :param dl_name:
        :param sort_by_aa:
        :param localize: Bandcamp recognize your country by ip
        and may translate title and other data in metadata
        of the track in your language (if artist specified it)
        :return:
        """
        log(f'start downloading {self.artist}-{self.album}-{self.title}')
        if sort_by_aa:
            path = f'{location if location else self.location}/' \
                   f'{clear_unavailable_symbols(self.artist)}/{clear_unavailable_symbols(self.album)}/'
        else:
            path = f'{location if location else self.location}/'
        file_name = dl_name if dl_name else clear_unavailable_symbols(f'{self.artist} - {self.title}.mp3')
        if len(file_name) >= 140:
            file_name = file_name[0:140]
        mk_path(path)
        with open(path + file_name, "wb") as f:
            f.write(get_url_content(self.files[list(self.files.keys())[-1]]))

        if not localize:
            f = music_tag.load_file(path + file_name)
            f['artist'] = self.artist
            f['album'] = self.album
            f['title'] = self.title
            f.save()
        self.local_file = path + file_name
        log(f'downloaded')
