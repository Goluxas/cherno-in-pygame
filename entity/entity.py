import pygame
from pygame.locals import *

class Entity(object):
	"""
	Abstract class
	"""

	def __init__(self):
		self.x, self.y = 0, 0
		self.removed = False
		self.level = level
	
	# abstract
	def update(self):
		pass

	# abstract
	def render(self, screen):
		pass

	def remove(self):
		# Remove from level
		self.removed = True

	def is_removed(self):
		return self.removed


class Mob(Entity):
	"""
	Abstract class
	"""

	def __init__(self):
		super(Mob, self).__init__()

		self.sprite = None
		self.direction = 0 # 0=N 1=E 2=S 3=W
		self.moving = False

	def move(self, xa, ya):
		# find direction
		if xa > 0: self.direction = 1
		if xa < 0: self.direction = 3
		if ya > 0: self.direction = 2
		if ya < 0: self.direction = 0

		# if there's no collision, move
		if not self.collision():
			self.x += xa
			self.y += ya

	# abstract
	def update(self):
		pass

	# abstract
	def render(self):
		pass

	def collision(self):
		return False
