import requests

# make a request using get

r = requests.get("https://httpbin.org")

# print(r.url) # return the passed url
# print("==============")
# print(r.status_code) # returns the request status code (199 < status_code < 305)
# print("==============")
# print(r.content) # Returns the raw html
# print("==============")
# print(r.headers["content-type"]) # returns 
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
    with open('content.txt', 'a') as content:
        content.write(httpObject.text)

    return content



ab = write_rcontent(r)