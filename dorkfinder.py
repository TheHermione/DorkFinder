#!/usr/bin/python3

# Script created by glavstroy (hermione)
# Thanks to @reewardius

import requests
from bs4 import BeautifulSoup
import url_list
import time
import random
import os
import urllib.parse
import sys

# ANSI color codes for better readability
RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m' 
CYAN = "\033[36m"
END = "\033[0m"

# function to print banner
def print_banner():
    banner = f"""
    ██████╗  ██████╗ ██████╗ ██╗  ██╗███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
    ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
    ██║  ██║██║   ██║██████╔╝█████╔╝ █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
    ██║  ██║██║   ██║██╔══██╗██╔═██╗ ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
    ██████╔╝╚██████╔╝██║  ██║██║  ██╗██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
    """
    print(banner)
    print('\n')

# function to perform Google search and analyze results
def perform_google_search(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Site": "cross-site",
        "TE": "trailers"
    }
    try:
        r = requests.get('https://www.google.com/search?q='+urllib.parse.quote(url), headers=headers, timeout=95)
        if r.status_code == 200:
            html = r.text
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.find_all('h3')
        elif r.status_code == 429:
            print(f"{RED}You've got a captcha from Google. Try again later or use another proxy{END}")
            sys.exit()

        else:
            print(f'{RED}Unknown error{END}')
            sys.exit()

        if len(links) >= 1:
            print(f'{BLUE}[+]{END} {url}   {CYAN}======>{END}  {GREEN}Found{END}')
            return True
        else:
            print(f'{BLUE}[!]{END} {url}   {CYAN}======>{END}  {RED}Not found{END}')
            return False
    except Exception as e:
        print(f"{RED}An error occurred while performing Google search: {str(e)}{END}")
        sys.exit()

# function to write URLs to output file
def write_to_output(url):
    file_path = 'output.txt'
    with open(file_path, 'a', encoding='utf-8') as output_file:
        output_file.write(f'{url}\n')

# main
def main():
    print_banner()
    print(f"\033[1m{YELLOW}[WARNING]{END}\033[0m \033[1mIt's very important not to stress the Google during usage of dork payloads. \nThat's why I cause about 60 seconds delay between requests. Just be patient...\033[0m")

    # clean output file
    file_path = 'output.txt'
    if os.path.exists(file_path):
        os.remove(file_path)

    for url in url_list.urls:
        if url_list.cli:
            if perform_google_search(url):
                if url_list.args.output:
                    write_to_output(url)

        # delay between requests
        time.sleep(random.randint(58,66))
        

# exception handling
try:
    main()
except KeyboardInterrupt:
    print(f'\nInterrupted')
    exit()
