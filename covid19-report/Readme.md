# Cne scrapy

This script consults data from the following API: https://covid19-api.com/docs and obtains the reports from all the countries and generates a csv with the following columns: country confirmed, recovered, dead and critical.


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
Consult information and generate CSV
```bash
python covid19.py
```
**NOTE** The csv file will be saved as covid19_data.csv by default


## License
[MIT](https://choosealicense.com/licenses/mit/)
