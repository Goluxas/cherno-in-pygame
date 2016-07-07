import os

import pygame
from pygame.locals import *

from graphics.screen import Screen

BLACK = pygame.Color(  0,   0,   0)
WHITE = pygame.Color(255, 255, 255)
BLUE  = pygame.Color( 80,  80, 200)

class Game(object):
	SCREEN_WIDTH = 300
	SCREEN_HEIGHT = SCREEN_WIDTH / 16 * 9
	SCALE = 3

	SCREEN_CAPTION = 'Rain'

	def __init__(self):
		self.running = False

		self.display = None
		self.size = self.SCREEN_WIDTH * self.SCALE, self.SCREEN_HEIGHT * self.SCALE

		self.screen = Screen(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

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
			self.update()
			self.render()

	def update(self):
		pass

	def render(self):

		self.screen.clear()
		self.screen.render()

		scaled = pygame.transform.scale( self.screen.surface, self.size )
		self.display.blit( scaled, (0,0) )

		pygame.display.update()


if __name__ == '__main__':
	game = Game()
	game.run()
