# flask-download-file-from-browser
> Input text from a browser. Download file from a browser filled with text input from the browser. Made with python flask

## Overview

```
                input text
    browser  ---------------> flask server
 (download)  <--------------- (write file)
              send file(.txt)
```

## Features
* Input text from a web browser
* Write text to a .txt file
* Send files from a python flask server
* Download the text file from a browser (UUID v4 filenames) 

## Getting started

### Prerequisites
* [python, pip](https://www.python.org/downloads/) installed

### Setup
```bash
pip install -r requirements.txt 
```

### Run server

```bash
# run shell script
chmod +x run_server.sh
./run_server.sh

# run commands (alternative)
export FLASK_APP=app.py
export FLASK_ENV=development # optional
flask run --host 0.0.0.0 --port 5000

# run in the background
nohup flask run --host 0.0.0.0 --port 5000 >log.txt 2>&1 &
```

### Show logs
```bash
# in case running in the background
tail -f log.txt
```

## How to use
1. Run server as above
2. http://localhost:5000
3. Write text
4. Push `send` button
5. Download a file
6. Check written in the downloaded file

