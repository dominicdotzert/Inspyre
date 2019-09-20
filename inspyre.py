import requests
from PIL import Image
from io import BytesIO
from datetime import datetime
import time

URL = "https://inspirobot.me/api"

while (true):
    count = count + 1

    PARAMS = { "generate" : "true"}
    if (datetime.now().month == 12):
        PARAMS["season"] = "xmas"

    r = requests.get(url = URL, params = PARAMS)
    i = requests.get(r.text)
    img = Image.open(BytesIO(i.content))

    img.show()
    
    time.sleep(5)