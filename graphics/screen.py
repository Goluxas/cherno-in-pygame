import random

import pygame
from pygame.locals import *

from graphics import sprite

class Screen(object):
	MAP_SIZE = 8
	MAP_SIZE_MASK = MAP_SIZE - 1

	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.surface = pygame.Surface((self.width, self.height))

		self.x_offset, self.y_offset = 0, 0

		# tile grid is 64x64 and tile size is 32x32
		self.tiles = []

		for i in range(self.MAP_SIZE ** 2):
			self.tiles.append( random.randrange(0xffffff) )

	def clear(self):
		self.surface.fill(0x000000)

	def render_tile(self, xp, yp, tile):
		"""
		xp, yp = x, y offsets (tile position relative to the world)
		"""
		xp -= self.x_offset
		yp -= self.y_offset

		pixels = pygame.PixelArray(self.surface)

		for y in range(tile.sprite.size):
			ya = y + yp # ya = y-absolute, as in position relative to the world
			for x in range(tile.sprite.size):
				xa = x + xp
				if xa < 0 or xa >= self.width or \
				   ya < 0 or ya >= self.width:
					   break
				pixels[xa, ya] = tile.sprite.image.get_at((x, y))

		del pixels

	def set_offset(self, dx, dy):
		self.x_offset = dx
		self.y_offset = dy
