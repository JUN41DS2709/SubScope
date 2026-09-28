import requests
import json
import re


def anubis(domain):
    anubis_url = "https://anubisdb.com/subdomains/"
    url = anubis_url + domain
    try:
        r = requests.get(url ,timeout=10)
        r.raise_for_status()
        data = r.json()
        return data
    except Exception as err:
        return []