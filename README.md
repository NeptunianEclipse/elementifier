# Elementifier

This is a Python script that when given a string or a list of strings, will output all ways of writing those strings using elemental 
symbols. For example, the word `` can be written as `` and ``.

## Usage

The script can be run in two ways:

1. `python elementifier [input-string]`\
The script will print all possible encodings of `input-string` in elemental symbols.

2. `python elementifier -f [file] -d [destination]`\
The script will attempt to encode all line-seperated strings in `file` and write them to `destination`


Running `python elementifier -f dictionary.txt -d encodings.txt` will attempt encode all English words (using the provided `dictionary.txt`
file) and write these encodings to `encodings.txt`
