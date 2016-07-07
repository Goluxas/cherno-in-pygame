import os

import pygame
from pygame.locals import *

class Game(object):
	SCREEN_WIDTH = 300
	SCREEN_HEIGHT = SCREEN_WIDTH / 16 * 9
	SCALE = 3

	SCREEN_CAPTION = 'Rain'

	def __init__(self):
		self.running = False

		self.display = None
		self.size = self.SCREEN_WIDTH * self.SCALE, self.SCREEN_HEIGHT * self.SCALE

	def setup(self):
		os.environ['SDL_VIDEO_CENTERED'] = '1' # should make the window pop up centered

		pygame.init()

		self.display = pygame.display.set_mode( self.size )
		pygame.display.set_caption( self.SCREEN_CAPTION )

		self.running = True

	def stop(self):
		self.running = False

	def run(self):
		self.setup()

		while self.running:
			print 'Running...'

if __name__ == '__main__':
	game = Game()
	game.run()
