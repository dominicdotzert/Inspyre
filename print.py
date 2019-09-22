import requests
from PIL import Image
from io import BytesIO

filename = ''

with open(filename, 'r') as f:
    links = f.readlines()
	
for link in links:
    i = requests.get(link.strip())
    img = Image.open(BytesIO(i.content))
    img.show()