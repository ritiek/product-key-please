# Product-Key-Please

- This handy python script finds product keys for commercial softwares by looking for them on the Internet.

- You need to have a template of how the product key looks like before hand (something like ????-????-????-????), that gives an idea how the key looks like.

## Installation & Usage:

```
git clone https://github.com/Ritiek/Product-Key-Please
cd Product-Key-Please
```

- We need Requests and BeautifulSoup:

`sudo pip install -r requirements.txt`

- Now to use the script, pass the software name and the key template:

- You can find the `.txt` file in `keys/` directory holding all the product keys it found.

- For example:

`sudo python find_key.py 'windows 7' '?????-?????-?????-?????-?????'`

It will keep presenting you with possible product keys for the software and save them to `keys/windows_7.txt`.

- Press `Ctrl+C` to exit anytime.

## Disclaimer:

In no way I support piracy. This tool is meant for educational purposes only and I will not be held responsible for any misuse.

## License:

`The MIT License`
