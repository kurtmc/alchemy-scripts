#!/usr/bin/env python3
from bs4 import BeautifulSoup
import urllib.request
from lxml import html
import os
import re

def get_soup(url):
    return BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')


def is_pdf(href):
        return href and re.compile("pdf").search(href)

def process_link(link):
        product_soup = get_soup(root + link.get("href"))
        return product_soup.find_all(href=is_pdf)[0].get("href")

def process_pdf_link(link):
    split_str = re.compile("[/?]").split(link)
    nice_name = split_str[6]
    print("Downloading", nice_name)
    os.system("wget " + root + link + " -O " + nice_name)

def get_pdf_link(soup):
    return subpage.find_all(href=is_pdf)[0].get("href")

def process_website(root_url, directory, subpage_query, document_query, process_document_link):
    root_page = get_soup(root_url + directory)

    sublinks = root_page.find_all(subpage_query)

    for sublink in sublinks:
        subpage = get_soup(root + sublink.get("href"))
        document_link = document_query(subpage)
        process_document_link(document_link)

def process_website2(root, directory, process_subpage, process_document_link):
    soup = get_soup(root + directory)
    link_list = soup.find_all('a', 'marginal')
    for i in link_list:
        l = process_subpage(i)
        process_document_link(l)

root = "https://techcenter.lanxess.com"
directory = "/scp/emea/en/products/type/index.jsp?pid=55"

#process_website(root, directory, ('a', 'marginal'), get_pdf_link, process_pdf_link)
process_website2(root, directory, process_link, process_pdf_link)
exit()

pdf_list = []
soup = get_soup(root + directory)
link_list = soup.find_all('a', 'marginal')
for i in link_list:
    l = process_link(i)
    pdf_list.append(l)
    process_pdf_link(l)
