import datetime
import os
import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QObject

import ui.ui as gui
import parser
import logs
from track import Track


def get_file_urls(path: str) -> list[str]:
    res = []
    with open(path, "r", encoding="UTF-8") as f:
        lines = f.readlines()
    for i in lines:
        if i.startswith("#"):
            pass
        else:
            res.append(i.strip().strip("/"))
    return res


class MainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.thrd = QtCore.QThread()

        self.ui.btn_download.setEnabled(True)
        self.ui.btn_download.clicked.connect(self.btn_download_onclick)

        self.ui.le_url.textChanged.connect(self.le_url_onchanged)

        self.ui.cb_sort.setChecked(True)

        self.ui.le_url.setText("urls.txt")

        self.start_dl = StartDl(self)
        self.start_dl.moveToThread(self.thrd)

        self.thrd.started.connect(self.start_dl.run)

        self.ui.tb_url.clicked.connect(self.select_urls_file)

        self.ui.btn_stop.clicked.connect(self.stop_downloading)

    def check_valid_le_url(self):
        url = self.ui.le_url.text()
        return parser.is_url_valid(url) or os.path.exists(url)

    def le_url_onchanged(self):
        ...

    def select_urls_file(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Open text file with urls", "", "Text Files (*.txt)")[0]
        self.ui.le_url.setText(file)

    def btn_download_onclick(self):
        self.thrd.start()
        # url = self.ui.le_url.text()
        # location = self.ui.le_location.text()
        # location = location if location != "" else "music"
        # localize = self.ui.cb_localize.isChecked()
        # sort_by_aa = self.ui.cb_sort.isChecked()
        # create_lyrics_file = self.ui.cb_lyrics.isChecked()
        # if parser.is_url_valid(url):
        #     self.tb_log(f"Parsing tracks urls for {url}...")
        #     tracks = parser.parse(url)
        #     self.tb_log(f"Found {len(tracks)} tracks")
        #     self.download_tracks(tracks=tracks, location=location, localize=localize, sort_by_aa=sort_by_aa,
        #                          create_lyrics_file=create_lyrics_file)
        # elif os.path.exists(url):
        #     self.tb_log(f"Parsing tracks urls for {url}...")
        #     urls = get_file_urls(url)
        #     tracks = []
        #     for url in urls:
        #         tracks.extend(parser.parse(url))
        #     self.tb_log(f"Found {len(tracks)} tracks")
        #     self.download_tracks(tracks=tracks, location=location, localize=localize, sort_by_aa=sort_by_aa,
        #                          create_lyrics_file=create_lyrics_file)
        # else:
        #     QtWidgets.QMessageBox.warning(self, "URL or path is invalid", "Enter valid URL or path to file with URLS")

    # def download_tracks(self, tracks: list[Track], location: str = "music", localize=False, sort_by_aa=True,
    #                     create_lyrics_file=False):
    #     self.tb_log("Start downloading tracks")
    #     prbar = self.ui.pb_downloading
    #     if len(tracks) > 0:
    #         step = 100 // len(tracks)
    #         for track in tracks:
    #             try:
    #                 track.download(location=location, localize=localize, sort_by_aa=sort_by_aa,
    #                                create_lyrics_file=create_lyrics_file)
    #                 self.tb_log(f"Track {track.artist}-{track.title} downloaded", mode="success")
    #                 prbar.setValue(prbar.value() + step)
    #             except Exception as err:
    #                 self.tb_log(f"While {track.artist}-{track.title} downloaded error occurred: <b>{err}</b>",
    #                             mode="error")
    #         prbar.setValue(100)
    #     else:
    #         self.tb_log('No tracks found', mode="error")

    def tb_log(self, text: str, mode: str = "info"):
        """
        insert log into logs text browder
        :param text:
        :param mode: info|success|warning|error
        :return:
        """
        tb = self.ui.textbr_logs
        match mode:
            case "info":
                tb.insertHtml(f"<br><span style='color: #ffffff'>[+][{datetime.datetime.now()}]{text}</span>")
            case "success":
                tb.insertHtml(f"<br><span style='color: #69e256'>[+][{datetime.datetime.now()}]{text}</span>")
            case "warning":
                tb.insertHtml(f"<br><span style='color: yellow'>[!][{datetime.datetime.now()}]{text}</span>")
            case "error":
                tb.insertHtml(f"<br><span style='color: red'>[-][{datetime.datetime.now()}]{text}</span>")
            case _:
                raise Exception("Invalid mode")
        tb.moveCursor(QtGui.QTextCursor.End)

    def stop_downloading(self):
        self.ui.btn_download.setEnabled(True)
        self.ui.cb_sort.setEnabled(True)
        self.ui.cb_lyrics.setEnabled(True)
        self.ui.cb_localize.setEnabled(True)
        self.ui.btn_stop.setEnabled(False)
        self.thrd.terminate()


class StartDl(QObject):
    def __init__(self, inf: MainWin):
        super().__init__()
        self.inf = inf  # inf = interface
        # self.tracks = tracks
        # self.location = location
        # self.localize = localize
        # self.sort_by_aa = sort_by_aa
        # self.create_lyrics_file = create_lyrics_file

    @QtCore.pyqtSlot()
    def run(self):
        self.inf.ui.btn_download.setEnabled(False)
        self.inf.ui.cb_sort.setEnabled(False)
        self.inf.ui.cb_lyrics.setEnabled(False)
        self.inf.ui.cb_localize.setEnabled(False)
        self.inf.ui.btn_stop.setEnabled(True)
        url = self.inf.ui.le_url.text()
        location = self.inf.ui.le_location.text()
        location = location if location != "" else "music"
        localize = self.inf.ui.cb_localize.isChecked()
        sort_by_aa = self.inf.ui.cb_sort.isChecked()
        create_lyrics_file = self.inf.ui.cb_lyrics.isChecked()
        tracks = []
        if parser.is_url_valid(url):
            self.inf.tb_log(f"Parsing tracks urls for {url}...")
            tracks = parser.parse(url)
            self.inf.tb_log(f"Found {len(tracks)} tracks")
            self.download_tracks(tracks=tracks, location=location, localize=localize, sort_by_aa=sort_by_aa,
                                 create_lyrics_file=create_lyrics_file)
        elif os.path.exists(url):
            self.inf.tb_log(f"Parsing tracks urls from {url.split('/')[-1]}...")
            urls = get_file_urls(url)
            tracks = []
            for url in urls:
                tracks.extend(parser.parse(url))
            self.inf.tb_log(f"Found {len(tracks)} tracks")
            self.download_tracks(tracks=tracks, location=location, localize=localize, sort_by_aa=sort_by_aa,
                                 create_lyrics_file=create_lyrics_file)
        else:
            QtWidgets.QMessageBox.warning(self.inf, "URL or path is invalid",
                                          "Enter valid URL or path to file with URLS")

        # self.download_tracks(tracks=tracks, location=location, localize=localize, sort_by_aa=sort_by_aa,
        #                      create_lyrics_file=create_lyrics_file)
        self.inf.ui.btn_download.setEnabled(True)
        self.inf.ui.cb_sort.setEnabled(True)
        self.inf.ui.cb_lyrics.setEnabled(True)
        self.inf.ui.cb_localize.setEnabled(True)
        self.inf.ui.btn_stop.setEnabled(False)
        self.inf.thrd.terminate()

    def download_tracks(self, tracks: list[Track], location: str = "music", localize=False, sort_by_aa=True,
                        create_lyrics_file=False):
        self.inf.tb_log("Start downloading tracks")
        # prbar = self.inf.ui.pb_downloading
        if len(tracks) > 0:
            step = 100 // len(tracks)
            for track in tracks:
                try:
                    track.download(location=location, localize=localize, sort_by_aa=sort_by_aa,
                                   create_lyrics_file=create_lyrics_file)
                    self.inf.tb_log(f"Track {track.artist}-{track.title} downloaded", mode="success")
                    # prbar.setValue(prbar.value() + step)
                except Exception as err:
                    self.inf.tb_log(f"While {track.artist}-{track.title} downloaded error occurred: <b>{err}</b>",
                                    mode="error")
            # prbar.setValue(100)
            self.inf.tb_log('DOWNLOADING COMPLETE', mode="success")
        else:
            self.inf.tb_log('No tracks found', mode="error")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWin()
    window.show()
    # app.exec()
    sys.exit(app.exec())
