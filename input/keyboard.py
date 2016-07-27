import pygame
from pygame.locals import *

class Keyboard(object):

	def __init__(self):
		self.keys = {} # k, v = event.key OR ord(c), True if pressed
		self.up = self.down = self.left = self.right = False

	def update(self):
		# read inputs
		for event in pygame.event.get(KEYDOWN):
			self.keys[event.key] = True

		for event in pygame.event.get(KEYUP):
			self.keys[event.key] = False

		# process inputs
		self.quit = self.keys.get(K_ESCAPE, False)

		self.up = self.keys.get(K_UP, False) or self.keys.get(K_w, False)
		self.down = self.keys.get(K_DOWN, False) or self.keys.get(K_s, False)
		self.left = self.keys.get(K_LEFT, False) or self.keys.get(K_a, False)
		self.right = self.keys.get(K_RIGHT, False) or self.keys.get(K_d, False)

		# for fun
		for key in self.keys:
			if self.keys[key]:
				print "KEY: %s" % key
