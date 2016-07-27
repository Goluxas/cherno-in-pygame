import os, sys

import pygame
from pygame.locals import *

# NOTE: Game-related classes are imported
#       during Game.setup() because they require
#       pygame.init() to have been called

BLACK = pygame.Color(  0,   0,   0)
WHITE = pygame.Color(255, 255, 255)
BLUE  = pygame.Color( 80,  80, 200)

class Game(object):
	SCREEN_WIDTH = 300
	SCREEN_HEIGHT = SCREEN_WIDTH / 16 * 9
	SCALE = 3

	SCREEN_CAPTION = 'Rain'

	FRAMERATE = 60.0

	def __init__(self):
		self.running = False

		self.display = None
		self.size = self.SCREEN_WIDTH * self.SCALE, self.SCREEN_HEIGHT * self.SCALE

		self.clock = None
		self.screen = None
		self.keyboard = None

		self.level = None

		self.player = None

	def setup(self):
		os.environ['SDL_VIDEO_CENTERED'] = '1' # should make the window pop up centered

		pygame.init()

		self.display = pygame.display.set_mode( self.size )

		# imports (since they require pygame.init())
		from graphics.screen import Screen
		from input.keyboard import Keyboard
		from level.level import RandomLevel
		from entity.player import Player

		pygame.display.set_caption( self.SCREEN_CAPTION )

		self.clock = pygame.time.Clock()
		self.screen = Screen(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
		self.keyboard = Keyboard()

		self.level = RandomLevel(64, 64)

		self.player = Player(self.keyboard)

		self.running = True

	def stop(self):
		pygame.quit()
		sys.exit(0)

	def run(self):
		self.setup()

		delta = 0
		frames = 0
		updates = 0
		timer = 0

		while self.running:

			dt = self.clock.tick() 				  # dt    = time since last tick() in ms
			delta += dt / 1000.0 * self.FRAMERATE # delta = % of time till next frame
			timer += dt							  # timer = accumulated ms
			while delta >= 1:
				self.update()
				updates += 1
				delta -= 1

			self.render()
			frames += 1

			if timer > 1000:
				print '%d ups, %d fps' % (updates, frames)
				pygame.display.set_caption( '%s | %d ups, %d fps | X: %d, Y: %d' % ( self.SCREEN_CAPTION, updates, frames, self.player.x, self.player.y ) )
				updates = frames = 0
				timer -= 1000

		self.stop()

	def update(self):

		self.keyboard.update()
		if self.keyboard.quit:
			self.stop()

		self.player.update()

		for event in pygame.event.get():
			if event.type == QUIT:
				self.stop()

	def render(self):

		self.screen.clear()

		x_scroll = self.player.x - self.screen.width / 2
		y_scroll = self.player.y - self.screen.height / 2
		self.level.render(x_scroll, y_scroll, self.screen)

		self.player.render(self.screen)

		scaled = pygame.transform.scale( self.screen.surface, self.size )
		self.display.blit( scaled, (0,0) )

		pygame.display.update()


if __name__ == '__main__':
	game = Game()
	game.run()
