#!/usr/bin/python3

# Script created by glavstroy
# Thanks to @reewardius

RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m' 
CYAN = "\033[36m"
END = "\033[0m"

banner = f"""
██████╗  ██████╗ ██████╗ ██╗  ██╗███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║  ██║██║   ██║██████╔╝█████╔╝ █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██║  ██║██║   ██║██╔══██╗██╔═██╗ ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║  ██║██║  ██╗██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝"""
print(banner)
print(f'\n')

import requests
from bs4 import BeautifulSoup
import url_list
import time
import random
import os
import urllib.parse

def main():
    print(f"\033[1m{YELLOW}[WARNING]{END}\033[0m \033[1mIt's very important not to stress the Google during usage of dork payloads. \nThat's why I cause about 60 seconds delay between requests. Just be patient...\033[0m")
    url_count = 0
    requests_before_delay = 25
    sent_requests_count = 0
    
    #clean output file
    file_path = 'output.txt'
    if os.path.exists(file_path):
        os.remove("output.txt")

    for url in url_list.urls:
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
        
        #check if the -t flag is specified before sending requests and analyzing them
        if url_list.cli:
            r = requests.get('https://www.google.com/search?q='+urllib.parse.quote(url), headers=headers, timeout=95)
            if r.status_code == 200:
                html = r.text
                soup = BeautifulSoup(html, 'html.parser')
                links = soup.find_all('h3')
            elif r.status_code == 429:
                print(f"{RED}You've got a captcha from Google. Try again later or use an another proxy{END}")
                break
            else:
                print(f'{RED}Unknown error{END}')
                break

            if url_count == 0:
                print(f'{CYAN}Broad domain search with negative search{END}')

            if len(links) >= 1:
                url_found = url
                print(f'{BLUE}[+]{END} {url_found}   {CYAN}======>{END}  {GREEN}Found{END}')
                #print all dorks to output.txt file
                if url_list.args.output:
                    with open('output.txt', 'a', encoding='utf-8') as output_file:
                        output_file.write(f'[+] {url_found}\n')
            else:
                print(f'{BLUE}[!]{END} {url}   {CYAN}======>{END}  {RED}Not found{END}')

            time.sleep(random.randint(58,66))
            
            sent_requests_count += 1
            if sent_requests_count % requests_before_delay == 0:
                print(f'{BLUE}[INFO]{END} {CYAN}{sent_requests_count}/{len(url_list.urls)} requests have been completed...{END}')

            url_count += 1
            if url_count == 1:
                print(f'{CYAN}SQL Injection Errors{END}')
            elif url_count == 2:
                print(f'{CYAN}PHP extension with parameters{END}')
            elif url_count == 3:
                print(f'{CYAN}Java extension with parameters{END}')
            elif url_count == 4:
                print(f'{CYAN}NET extension with parameters{END}')
            elif url_count == 5:
                print(f'{CYAN}Disclosed XSS and Open Redirects{END}')
            elif url_count == 6:
                print(f'{CYAN}Juicy Extensions{END}')
            elif url_count == 140:
                print(f'{CYAN}App frameworks and their exposures{END}')
            elif url_count == 146:
                print(f'{CYAN}Code Leaks{END}')
            elif url_count == 175:
                print(f'{CYAN}Cloud Storage{END}')
            elif url_count == 189:
                print(f'{CYAN}XSS prone parameters{END}')
            elif url_count == 190:
                print(f'{CYAN}Open Redirect prone parameters{END}')
            elif url_count == 192:
                print(f'{CYAN}SQLi Prone Parameters{END}')
            elif url_count == 194:
                print(f'{CYAN}SSRF Prone Parameters{END}')
            elif url_count == 195:
                print(f'{CYAN}LFI Prone Parameters{END}')
            elif url_count == 197:
                print(f'{CYAN}RCE Prone Parameters{END}')
            elif url_count == 199:
                print(f'{CYAN}High % inurl keywords{END}')
            elif url_count == 201:
                print(f'{CYAN}Sensitive Parameters{END}')
            elif url_count == 232:
                print(f'{CYAN}Bug Bounty programs and Vulnerability Disclosure Programs{END}')
            elif url_count == 233:
                print(f'{CYAN}Apache Server Status Exposed{END}')
            elif url_count == 234:
                print(f'{CYAN}WordPress{END}')
            elif url_count == 235:
                print(f'{CYAN}Drupal{END}')
            elif url_count == 236:
                print(f'{CYAN}Joomla{END}')
            

try:
    main()
except KeyboardInterrupt:
    print(f'\nInterrupted')
    exit()
