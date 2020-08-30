"""
Purpose: Test some testing

"""
import requests


url_base = "https://cat-fact.herokuapp.com"


def cat_fact:
    """
    Testint Kitty API
    """
    r = requests.get(url_base+'/facts/random')
    response = r.json()
    fact=response['text']
    return fact


if __name__ == "__main__":
    fact = cat_fact()
    print(fact)