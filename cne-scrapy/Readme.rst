# Cne scrapy

Scrapy to get information about Venezuelan identification number and export data to csv file

## Requirements
python > 3.7

## Preparing the environment

Create your python environment

```bash
python3 -m venv env
source env/bin/activate
```

## install dependencies

`pip install -r requirements.txt`
## Usage
Extract DNI info with a Venezuelan identification number set:

```bash
python command.py --dni=v20000001,20000002,e20000001
```
**NOTE**: You can add the prefixes "v" or "e" to specify the nationality, if you do not add any of these by default it will be "v".

Extract DNI info with a list of dni specified in a file.
**NOTE**: identification number set split by line
```bash
python command.py --file=example_dni_list.txt
```
**NOTE** The csv file will be saved as dni_data.csv by default

**Other options:**

```
    Optional:
      # Export csv options
      -o OUTPUT_DIR, --output=OUTPUT_DIR,
      -n CSV_NAME.csv, --name=CSV_NAME.csv, 
```

## License
[MIT](https://choosealicense.com/licenses/mit/)