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

def get_product_pages(soup):
    return soup.find_all('a', 'marginal')

def process_website2(root, directory, get_subpage_links, process_subpage, process_document_link):
    soup = get_soup(root + directory)
    link_list = get_subpage_links(soup)
    for i in link_list:
        l = process_subpage(i)
        process_document_link(l)

root = "https://techcenter.lanxess.com"
directory = "/scp/emea/en/products/type/index.jsp?pid=55"

process_website2(root, directory, get_product_pages, process_link, process_pdf_link)
