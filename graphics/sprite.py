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

# Player sprite, facing down
player0 = Sprite(16, 4, 10, sheet=spritesheet.tiles, colorkey=0xff00ff)
player1 = Sprite(16, 5, 10, sheet=spritesheet.tiles, colorkey=0xff00ff)
player2 = Sprite(16, 4, 11, sheet=spritesheet.tiles, colorkey=0xff00ff)
player3 = Sprite(16, 5, 11, sheet=spritesheet.tiles, colorkey=0xff00ff)
