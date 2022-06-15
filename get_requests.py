from genericpath import exists
import os
import sys
import re
import requests

# make a request using get

r = requests.get("https://www.w3schools.com")

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

def write_rcontent(httpObject):

    """
        Returns a .txt file populated with the content of the httpObject.
    """
    if 'content.txt' not in os.listdir():
        with open('content.txt', 'a') as content:
            content.write(httpObject.text)
    else: print("the file already exists")
    return

def extract_tags(tag, httpObject):
    """
        return the number of tag in the http response

            tag: string (exple: a, link, p, br)

            if return odd number the tag has only an open-tag else the tag has both the open-tag and close-tag
    """
    
    return len(re.findall(tag, httpObject.text)) + 1

ab = write_rcontent(r)

# does not work quiet well yet, can be fixed....
ra = extract_tags("html", r)

print(ra)

# print(type(r.text))