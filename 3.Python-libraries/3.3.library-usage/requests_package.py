import requests

resp = requests.get('http://httpbin.org/ip')
print(resp.content.decode())

# resp.content.decode() converts the raw bytes of the response content into a string using the default encoding (UTF-8, unless otherwise specified) 