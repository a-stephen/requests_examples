# from genericpath import exists
import os
import re
import requests
from datetime import datetime
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
        os.mkdir(data_dir)
    else:
        os.chdir(data_dir)
        with open("{}_data.txt".format(get_date.date()), 'a') as file:
            file.write(get_info.text)
    return
    # return os.getcwd()

def extract():
    """
        
    """
    pass

n_data = write_rcontent("https://mg.co.za/section/news/")

def extract_tags(tag, httpObject):
    """
        return the number of tag in the http response

            tag: string (exple: a, link, p, br)

            if return odd number the tag has only an open-tag else the tag has both the open-tag and close-tag
    """
    
    return len(re.findall(tag, httpObject.text)) + 1

# ab = write_rcontent(r)

# # does not work quiet well yet, can be fixed....
# ra = extract_tags("html", r)

# print(ra)

# print(type(r.text))

def get_data(site):
    # make a get request to the site

    get_request = requests.get(site)

    return get_request.text

# data = get_data(site = "https://mg.co.za/section/news/")
# print(data)