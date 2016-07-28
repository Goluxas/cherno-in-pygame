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

	def render_player(self, xp, yp, sprite, flip=0):
		"""
		xp, yp = pixel-level coordinates of the player's 
		         sprite's top-left corner
		sprite = sprite to render
		flip   = 2-bit bool: flip_y and flip_x
				 0 = 00 = flip none
		         1 = 01 = flip x
				 2 = 10 = flip y
				 3 = 11 = flip both
		"""
		xp -= self.x_offset
		yp -= self.y_offset

		# I know this is silly since the transform method
		# takes 2 bools so the int saves us nothing, but
		# I'm following Cherno's lead
		flip_x = flip_y = False
		if flip == 1 or flip == 3: flip_x = True
		if flip == 2 or flip == 3: flip_y = True

		reverse = pygame.transform.flip(sprite.image, flip_x, flip_y)
		#self.surface.blit(sprite.image, (xp, yp))
		self.surface.blit(reverse, (xp, yp))

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
