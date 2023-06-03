from dotenv import load_dotenv
import os
import requests
from pprint import pprint


def get_reviews(api_key):
    url = 'https://dvmn.org/api/user_reviews/'
    headers = {'Authorization': f'Token {api_key}'}
    response = requests.get(
        url, 
        headers=headers
        )
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('DVMN_API_KEY')
    reviews = get_reviews(api_key)
    pprint(reviews)
