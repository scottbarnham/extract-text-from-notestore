# Basic script to extract text from NoteStore.sqlite file.

Apple Notes app stores text notes in `NoteStore.sqlite` file in `~/Library/Group Containers/group.com.apple.notes/`

The file is a sqlite database which has a table named `ZICNOTEDATA` with column `ZDATA` which contains a blob. This binary is gzip compressed utf-8 text wrapped in some other binary.

Pass the `NoteStore.sqlite` file to the script like:

```
python3 extract.py NoteStore.sqlite
```

The script does these steps:
+ Open the sqlite file
+ Get data from each row in the table
+ Decode the gzip data
+ Remove some bytes from the start
+ Search through the text until it reaches more non-printable binary data
+ Cut out just the text
+ Write the text to a file in an `output` directory - the file name is an ID and the start of the first line of the text

The text may include '￼' characters (embedded object placeholder).

The script does not export images.

Minimally tested. Hope it helps.
