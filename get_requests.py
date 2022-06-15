import requests

# make a request using get

r = requests.get("https://httpbin.org")

print(r.url)
print("==============")
print(r.status_code)
print("==============")
print(r.content) # Returns the raw html
print("==============")
print(r.headers["content-type"]) # returns 
print("==============")
print(r.text) # returns a pretty formatted of content
print("==============")
print(r.encoding) # returns the enconding used on the site
print("==============")
# print(r.json()) # returns json if any
print("==============")
print(r.raw) # returns an HTTPResponse object
print("==============")

