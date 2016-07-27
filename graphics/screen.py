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

		self.x_offset, self.y_offset = 0, 0

		# tile grid is 64x64 and tile size is 32x32
		self.tiles = []

		for i in range(self.MAP_SIZE ** 2):
			self.tiles.append( random.randrange(0xffffff) )

	def clear(self):
		self.surface.fill(0x000000)

	def render_tile(self, xp, yp, tile):
		"""
		xp, yp = pixel-level coordinates of tile's left-top 
		         with screen offsets included
		"""
		# remove the screen offset from tile position
		xp -= self.x_offset
		yp -= self.y_offset

		self.surface.blit(tile.sprite.image, (xp, yp))

	def set_offset(self, dx, dy):
		self.x_offset = dx
		self.y_offset = dy

	"""
	# For archival purposes, this is Cherno's pixel-level
	# render method for tiles, as in Episode 38. This works
	# in Pygame, but is much less efficient than the blit
	# method. (Swapping from this to blit made FPS jump from
	# ~30 to ~730!)
	def render_tile_pixelwise(self, xp, yp, tile):
		# xp, yp = x, y offsets (tile position relative to the world)
		xp -= self.x_offset
		yp -= self.y_offset

		pixels = pygame.PixelArray(self.surface)

		for y in range(tile.sprite.size):
			ya = y + yp # ya = y-absolute, as in position relative to the world
			for x in range(tile.sprite.size):
				xa = x + xp
				if xa < -tile.sprite.size or xa >= self.width or \
				   ya < 0 or ya >= self.height:
					   break
				if xa < 0: xa = 0
				pixels[xa, ya] = tile.sprite.image.get_at((x, y))

		del pixels
	"""
