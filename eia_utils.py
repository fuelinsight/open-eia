import requests

def validate_api_key(api_key=None):

    if api_key == None:
        try:
            with open('api_key.txt') as f:
                api_key = f.readlines()[0]
                
        except:
            raise Exception('api_key.txt not found, please provide an API key.')
    
    url = f'https://api.eia.gov/v2/electricity?api_key={api_key}'

    r = requests.get(url)

    if r.status_code == 200:
        print('Success!')
    elif r.status_code == 403:
        raise Exception('Invalid API key.')
    else:
        raise Exception(f'API Request failed with status code {r.status_code}.')

    return api_key