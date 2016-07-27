import pygame
from pygame.locals import *

from entity import Mob

class Player(Mob):

	def __init__(self, inp, x=0, y=0):
		self.x, self.y = x, y

		self.input = inp

	def update(self):
		xa = ya = 0
		if self.input.up: ya -= 1
		if self.input.down: ya += 1
		if self.input.left: xa -= 1
		if self.input.right: xa += 1

		if xa != 0 or ya != 0:
			self.move(xa, ya)

	def render(self):
		pass
