# bc-dl

Bandcamp music downloader (**BETA**)

## Usage:

Run `main.py` with arguments:

```
-f  File one or more urls of the artist|album|track. Each link should be on a separate line.
-u  Url of the artist|album|track.
-l  Location of downloaded files. The music files will be sorted into folders of artists and albums
```

### Example:

```
$ python3 main.py -f urls.txt -l /home/admin/Music

$ python3 main.py -u someartist.bandcamp.com -l /home/admin/Music
```
