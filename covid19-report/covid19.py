import requests
from pandas import DataFrame


BASE_URL = 'https://covid19-api.com'
DEFAULT_COLUMNS = ('country', 'confirmed', 'recovered', 'critical')
FILENAME_CSV = 'covid19_data.csv'


def get_latest_all_countries():

    try:
        return requests.get(f"{BASE_URL}/country/all").json()

    except Exception as e:
        print(e)
        exit(0)

if __name__ == '__main__':
    print('Getting Data...')
    payload = get_latest_all_countries()
    df = DataFrame(payload, columns=DEFAULT_COLUMNS)
    df.to_csv(FILENAME_CSV, index=False)
    print('Csv saved as ', FILENAME_CSV)
