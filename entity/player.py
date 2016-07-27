import pygame
from pygame.locals import *

from entity import Mob

class Player(Mob):

	def __init__(self, inp, x=0, y=0):
		self.x, self.y = x, y

		self.input = inp

	def update(self):
		if self.input.up: self.y -= 1
		if self.input.down: self.y += 1
		if self.input.left: self.x -= 1
		if self.input.right: self.x += 1

	def render(self):
		pass
