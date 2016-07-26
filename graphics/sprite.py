import pygame
from pygame.locals import *

from graphics import spritesheet

# C for Cherno
class CSprite(object):

	def __init__(self, size, x, y, sheet):
		self.size = size
		self.x = x * size
		self.y = y * size
		self.sheet = sheet

		self.image = pygame.Surface((self.size, self.size))
		
		self._load()

	def _load(self):
		"""
		# Cherno's pixelwise method
		# Too slow for pygame
		for y in range(self.size):
			for x in range(self.size):
				self.pixels[x, y] = sheet.pixels[x, y]
		"""
		
		self.image.blit(self.sheet.sheet, (0,0), (self.x, self.y, self.size, self.size))

grass = CSprite(16, 0, 0, spritesheet.tiles)
