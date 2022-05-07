#!/usr/bin/env python3

""" Geo-locate IP (w/ optional IPv4/6 CLI argument) """

import sys
from ipaddress import ip_address
from xml.etree import ElementTree

import requests

url = "https://freegeoip.app/xml/"

if len(sys.argv) == 2:
    ip = sys.argv[1]
    try:
        url += str(ip_address(ip))
    except ValueError:
        print(f'Invalid IP: "{ip}". Using your public IP...\n')
    else:
        print(f'Geo-locating address: {ip}\n')

xml = ElementTree.fromstring(requests.get(url).content)

for cell in xml:
    print(f'{cell.tag}: {cell.text}')
