# bc-dl

Bandcamp music downloader (**BETA**)

## Usage:

Run `main.py` with arguments:

```
-f  File one or more urls of the artist|album|track. Each link should be on a separate line.
-u  Url of the artist|album|track.
-l  Location of downloaded files. The music files will be sorted into folders of artists and albums
-t  Create lyrics file. 1 - create, 0 - don't create, default - 0
-s  Don't sort by artists and albums directories. 1 - sort, 0 - don't sort, default - 0
```

### Example:

```
$ python3 main.py -f urls.txt -l /home/admin/Music -s 1

$ python3 main.py -u someartist.bandcamp.com -l /home/admin/Music -t 1
```
