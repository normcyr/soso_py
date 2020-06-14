## Create a virtual environment with Python 3

```bash
virtualenv -p python3 venv
```

## Activate the virtual environment

```bash
source venv/bin/activate
```

## Install the required libraries via pip

```bash
pip install -r requirements
```

## Run the scraper

Before running the program, you need to get the proper `list_requests.json` file.

Or alternatively, you can use the `list_requests_test.json` file to test the script.

Then, go ahead!

```bash
python soso.py
```

Image files will be saved in the folder corresponding to the book number.
