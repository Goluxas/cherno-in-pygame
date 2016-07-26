import pygame
from pygame.locals import *

from graphics import spritesheet

# C for Cherno
class CSprite(object):

	def __init__(self, size, x=0, y=0, sheet=None, color=None):
		self.size = size
		self.image = pygame.Surface((self.size, self.size))

		if sheet is not None:
			self.x = x * size
			self.y = y * size
			self.sheet = sheet

			self._load()

		elif color is not None:
			self.image.fill(color)

	def _load(self):
		"""
		# Cherno's pixelwise method
		# Too slow for pygame
		for y in range(self.size):
			for x in range(self.size):
				self.pixels[x, y] = sheet.pixels[x, y]
		"""
		
		self.image.blit(self.sheet.sheet, (0,0), (self.x, self.y, self.size, self.size))

void_sprite = CSprite(16, color=0x1b87e0)
grass = CSprite(16, 0, 0, sheet=spritesheet.tiles)
