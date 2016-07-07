import random

import pygame
from pygame.locals import *

class Screen(object):
	MAP_SIZE = 8
	MAP_SIZE_MASK = MAP_SIZE - 1

	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.surface = pygame.Surface((self.width, self.height))

		# tile grid is 64x64 and tile size is 32x32
		self.tiles = []

		for i in range(self.MAP_SIZE ** 2):
			self.tiles.append( random.randrange(0xffffff) )

	def clear(self):
		self.surface.fill(0x000000)

	def render(self, x_offset, y_offset):
		pixels = pygame.PixelArray(self.surface)

		for y in range(self.height):
			yy = y + y_offset
			for x in range(self.width):
				xx = x + x_offset
				tile_index = ((xx >> 4) & self.MAP_SIZE_MASK) + ((yy >> 4) & self.MAP_SIZE_MASK) * self.MAP_SIZE
				pixels[x, y] = self.tiles[tile_index]

		del pixels
