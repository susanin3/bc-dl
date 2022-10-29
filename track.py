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
    return ("".join([i for i in text if not (i in "\/:*?\"<>|+")])).replace("​", "")  # replacing unavailable symbols and ZWSP


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
                 localize: bool = False, create_lyrics_file: bool = False) -> None:
        """
        :param location:
        :param dl_name:
        :param sort_by_aa: sort by artists and albums directories
        :param localize: Bandcamp recognize your country by ip
        :param create_lyrics_file:
        and may translate title and other data in metadata
        of the track in your language (if artist specified it)
        :return:
        """
        self.artist = clear_unavailable_symbols(self.artist)
        self.album = clear_unavailable_symbols(self.album)
        self.title = clear_unavailable_symbols(self.title)

        log(f'start downloading {self.artist}-{self.album}-{self.title}')
        if sort_by_aa:
            path = f'{location if location else self.location}/' \
                   f'{self.artist}/{self.album}/'
        else:
            path = f'{location if location else self.location}/'
        file_name = dl_name if dl_name else f'{self.artist} - {self.title}'
        extension = ".mp3"
        if len(file_name) >= 140:
            file_name = file_name[0:140]
        mk_path(path)
        with open(f"{path}{file_name}{extension}", "wb") as f:
            f.write(get_url_content(self.get_best_file()))

        if create_lyrics_file and self.lyrics is not None:
            with open(f"{path}{file_name}.lrc", "w", encoding="UTF-8") as f:
                f.write(self.lyrics)

        if not localize:
            f = music_tag.load_file(f"{path}{file_name}{extension}")
            f['artist'] = self.artist
            f['album'] = self.album
            f['title'] = self.title
            f.save()
        self.local_file = f"{path}{file_name}{extension}"
        log(f'downloaded')

    def get_best_file(self):
        return self.files[list(self.files.keys())[-1]]


if __name__ == '__main__':
    ...
