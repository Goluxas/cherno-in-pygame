import pygame
from pygame.locals import *

class SpriteSheet(object):

	def __init__(self, path, size):
		self.path = path
		self.size = size # used to initialize Cherno's pixel array, which we don't use

		self.sheet = None

		self._load()

	def _load(self):
		#try:
			self.sheet = pygame.image.load(self.path).convert()
		#except:
			#print 'Failed to load spritesheet: %s' % self.path
			#raise SystemExit

tiles = SpriteSheet('assets/spritesheet.png', 256)
