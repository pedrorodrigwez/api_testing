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
    r = requests.get(url_base+'/facts/random')
    response = r.json()
    fact=response['text']
    return fact


if __name__ == "__main__":
    fact = cat_fact()
    print(fact)