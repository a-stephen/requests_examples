# from genericpath import exists
import os
import re
import requests
from datetime import datetime
from bs4 import BeautifulSoup as bs


# make a request using get

# r = requests.get("https://www.w3schools.com")

# print(r.url) # return the passed url
# print("==============")
# print(r.status_code) # returns the request status code (199 < status_code < 305)
# print("==============")
# print(r.content) # Returns the raw html
# print("==============")
# print(r.headers["content-type"]) # returns headers: content-type
# print("==============")
# print(r.text) # returns a pretty formatted of content
# print("==============")
# print(r.encoding) # returns the enconding used on the site
# print("==============")
# # print(r.json()) # returns json if any
# print("==============")
# print(r.raw) # returns an HTTPResponse object
# print("==============")

def write_rcontent(website):

    """
        Returns a .txt file populated with the content of the httpObject.

    """
    # make a get request
    get_date = datetime.today()
    get_info = requests.get(website)

    curr_dir = os.getcwd()
    data_dir = os.path.join(curr_dir, 'news_data')

    # make a directory
    if not os.path.exists(data_dir):
        os.chdir(os.mkdir(data_dir))
    else:
        os.chdir(data_dir)
        with open("{}_data.txt".format(get_date.date()), 'a') as file:
            file.write(get_info.text)
    return file
    # return os.getcwd()
def filter_hrefs(href):
    hrefs2search = []
    un_href = ['facebook.com', 'instagram.com', 'twitter.com', 'soundcloud.com', 'pinterest.com', 'youtube.com', 'contact', 'aboutus']
    for _href in un_href:
        f_href = re.findall(_href, href)
        # if len(f_href) == 0: print(href)
        if f_href:
            hrefs2search.append(href)
    return hrefs2search
    
    # return re.findall("(?<=https://)(.*)(?=/)", href)



def company_mentioned(name):
    pass

def extract():
    """
        Return 
    """
    html_r = requests.get("https://citinewsroom.com/")

    bs_soup = bs(html_r.text, 'html.parser')
    a_hrefs = []
    # socios = [facebook]
    body = bs_soup.find('body')
    # print(len(body))
    for link in body.find_all('a'):
        hrefs = link.get('href');
        # print(type(hrefs))
        r_match = filter_hrefs(str(hrefs))
        if len(r_match):
            a_hrefs.append(r_match[0])
    return set(a_hrefs)
    

# n_data = write_rcontent("https://mg.co.za/section/news/")

list_link = extract()

# data = reduce_hrefs(list_link)

print(list_link)