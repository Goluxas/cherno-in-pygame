import random

import pygame
from pygame.locals import *

import tile

class Level(object):
	
	def __init__(self, width=0, height=0, path=None):
		self.width, self.height = width, height
		self.tiles = [] # flat-indexed list of tiles

		if path is not None:
			# Load a level from a file
			self._load_level(path)
		else:
			# Randomly generate a level
			self.width, self.height = width, height
			self._generate_level()

	def _generate_level(self):
		# Randomly generate a level
		pass

	def _load_level(self, path):
		# Read a level file
		pass

	def get_tile(self, x, y):
		# convert from 2D to flat coordinates
		t = self.tiles[x + y * self.width]

		if t == 0:
			return tile.grass
		else:
			return tile.void_tile

	def update(self):
		# Update entities of the level
		pass

	def time(self):
		# Timers? Not sure
		pass

	def render(self, x_scroll, y_scroll, screen):
		"""
		# Draw the world
		x_scroll, y_scroll = pixel position of the player
		screen = main Screen object
		"""
		screen.set_offset(x_scroll, y_scroll)
		
		# Corner pins
		# converting from pixel-level to tile-level
		x0 = x_scroll / 16                   # left side of the screen
		x1 = (x_scroll + screen.width) / 16  # right
		y0 = y_scroll / 16                   # top 
		y1 = (y_scroll + screen.height) / 16 # bottom 

		for y in range(y0, y1):
			for x in range(x0, x1):
				tile = self.get_tile(x, y)
				tile.render(x, y, screen)


class RandomLevel(Level):

	def __init__(self, width, height):
		super(RandomLevel, self).__init__(width, height)

	def _generate_level(self):
		for y in range(self.height):
			for x in range(self.width):
				self.tiles.append(random.randrange(4))
