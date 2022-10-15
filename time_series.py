import pandas as pd
import requests
import json
import os
from datetime import date

from eia_utils import validate_api_key

def time_series_EIA(series_path, api_key=None):

    valid_api_key = validate_api_key(api_key)

    url = f'https://api.eia.gov/v2/{series_path}?api_key={valid_api_key}'

    r = requests.get(url)

    json_data = json.dumps(r.json())

    if r.status_code == 200:
        print('Success!')
    else:
        print(r.status_code)

    return json_data

if __name__ == '__main__':

    df = time_series_EIA('petroleum')

    with open("sample.json", "w") as outfile:
        outfile.write(df)