import requests
from PIL import Image
from io import BytesIO
from datetime import datetime
import time
import pygame

URL = "https://inspirobot.me/api"
DELAY = 15

pygame.init()
pygame.mouse.set_visible(False)

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

screen_height = screen.get_height()
screen_width = screen.get_width()
img_offset = (screen_width - screen_height) / 2

filename = str(datetime.now()).replace(':', '.') + '.txt'
t = time.time()
t = t - DELAY
done = False

with open(filename, 'a+') as f:
	while (not done):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					done = True
					
		if (time.time() - t > DELAY):
			PARAMS = { "generate" : "true"}
			if (datetime.now().month == 12):
				PARAMS["season"] = "xmas"

			r = requests.get(url = URL, params = PARAMS)
			f.write(r.text + '\n')
			i = requests.get(r.text)
			img = pygame.image.load(BytesIO(i.content))
			img = pygame.transform.scale(img, (screen_height, screen_height))

			screen.blit(img, (img_offset,0))
			pygame.display.flip()
			
			t = time.time()