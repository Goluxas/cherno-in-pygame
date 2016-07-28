import pygame
from pygame.locals import *

from graphics import spritesheet

# Custom sprite class with Cherno functionality added
class Sprite(pygame.sprite.Sprite):

	def __init__(self, size, x=0, y=0, sheet=None, color=None, colorkey=None):
		# pygame Sprite constructor
		super(Sprite, self).__init__()

		self.size = size
		self.image = pygame.Surface((self.size, self.size))

		if sheet:
			self.x = x * size
			self.y = y * size
			self.sheet = sheet

			self._load()

			if colorkey:
				self.image.set_colorkey(colorkey)

		elif color:
			self.image.fill(color)
			
		self.rect = self.image.get_rect()

	def _load(self):
		"""
		# Cherno's pixelwise method
		# Too slow for pygame
		for y in range(self.size):
			for x in range(self.size):
				self.pixels[x, y] = sheet.pixels[x, y]
		"""
		
		self.image.blit(self.sheet.sheet, (0,0), (self.x, self.y, self.size, self.size))

void_sprite = Sprite(16, color=0x1b87e0)
grass = Sprite(16, 0, 0, sheet=spritesheet.tiles)

# player sprites
player_up    = Sprite(32, 0, 5, sheet=spritesheet.tiles, colorkey=0xff00ff)
player_side = Sprite(32, 1, 5, sheet=spritesheet.tiles, colorkey=0xff00ff)
player_down  = Sprite(32, 2, 5, sheet=spritesheet.tiles, colorkey=0xff00ff)
