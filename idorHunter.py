#!/bin/python3
import random
import requests
import argparse
import sys
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', help="-u is the argument needed to provide a link to IDORhunter. Example: -u https://hack.me/")
    args = parser.parse_args()
    sys.stdout.write(str(scraper(args)))

#User agent
ua = UserAgent().random
headers={
        'User-Agent' : ua
    }

def scraper(args):
    #headers = {'User-Agent' : GET_UA()}
    source = requests.get(args.u, headers=headers).text

    soup = BeautifulSoup(source, 'lxml')

    links = []
    for match in soup.find_all('a'):
        link = match.get('href')
        if '#' in link:
            continue
        if link not in links:
            print(link)
            links.append(link)
    
if __name__ == '__main__':
    main()

