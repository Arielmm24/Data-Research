
import os
import sys
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import asyncio
import json
import aiohttp
from understat import Understat


apartments_list = []
url = 'https://www.madlan.co.il/for-sale/%D7%99%D7%A9%D7%A8%D7%90%D7%9C?marketplace=residential'   #creating url for primary pages
#url = 'https://www.madlan.co.il/'

# Making a GET request
r = requests.get(url)
 
# print request object
print(r)
   
# print status code
print(r.status_code)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())
print("check")
