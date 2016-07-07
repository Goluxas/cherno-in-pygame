import pygame
from pygame.locals import *

class Screen(object):

	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.surface = pygame.Surface((self.width, self.height))

	def render(self):
		pixels = pygame.PixelArray(self.surface)

		for y in range(self.height):
			for x in range(self.width):
				pixels[x, y] = 0xff00ff

		del pixels
