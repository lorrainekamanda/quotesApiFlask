from app import app
import urllib.request,json
with urlopen('http://quotes.stormconsultancy.co.uk/random.json') as response:
    source = response.read()

print(source)

