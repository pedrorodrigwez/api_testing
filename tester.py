"""
Purpose: Test some testing with a public API 
Public Endpoint Docs: https://alexwohlbruck.github.io/cat-facts/

"""
import requests


url_base = "https://cat-fact.herokuapp.com"


def cat_fact():
    """
    
    Fetch a Random Fact from the api

    """
    try:
        r = requests.get(url_base+'/facts/random')
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    if r.status_code == 200:
        response = r.json()
        fact = response['text']
    else:
        fact = None
    return fact


if __name__ == "__main__":
    fact = cat_fact()
    print(fact)