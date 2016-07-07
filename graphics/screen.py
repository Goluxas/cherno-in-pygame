import pygame
from pygame.locals import *

class Screen(object):

	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.surface = pygame.Surface((self.width, self.height))

		self.counter = 0
		self.time = 0

	def clear(self):
		self.surface.fill(0x000000)

	def render(self):
		self.counter += 1
		if self.counter % 20 == 0:
			self.time += 1

		pixels = pygame.PixelArray(self.surface)

		for y in range(self.height):
			for x in range(self.width):
				pixels[self.time, self.time] = 0xff00ff

		del pixels
