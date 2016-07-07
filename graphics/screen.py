import random

import pygame
from pygame.locals import *

class Screen(object):

	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.surface = pygame.Surface((self.width, self.height))

		# tile grid is 64x64 and tile size is 32x32
		self.tiles = []

		for i in range(64 * 64):
			self.tiles.append( random.randrange(0xffffff) )

	def clear(self):
		self.surface.fill(0x000000)

	def render(self):
		pixels = pygame.PixelArray(self.surface)

		for y in range(self.height):
			if y < 0 or y >= self.height: break
			for x in range(self.width):
				if x < 0 or x >= self.width: break
				tile_index = (x >> 4) + (y >> 4) * 64
				pixels[x, y] = self.tiles[tile_index]

		del pixels
