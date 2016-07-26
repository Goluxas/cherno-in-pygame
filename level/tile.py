import pygame
from pygame.locals import *

from graphics import sprite

class Tile(object):

	def __init__(self, sprite):
		self.x, self.y = 0, 0
		self.sprite = sprite

	def render(self, x, y, screen):
		pass

	def solid():
		return False


class GrassTile(Tile):

	def __init__(self, sprite):
		super(GrassTile, self).__init__(sprite)

	def render(self, x, y, screen):
		"""
		x, y = pixel coordinates
		screen = main screen object
		"""
		screen.render_tile(x*16, y*16, self)


class VoidTile(Tile):

	def __init__(self, sprite):
		super(VoidTile, self).__init__(sprite)

	def render(self, x, y, screen):
		"""
		x, y = pixel coordinates
		screen = main screen object
		"""
		screen.render_tile(x*16, y*16, self)

# Static Tiles
void_tile = VoidTile(sprite.void_sprite)
grass = GrassTile(sprite.grass)
