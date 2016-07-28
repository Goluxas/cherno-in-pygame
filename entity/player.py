import pygame
from pygame.locals import *

from entity import Mob
from graphics import sprite

class Player(Mob):

	def __init__(self, inp, x=0, y=0):
		super(Player, self).__init__()

		self.x, self.y = x, y

		self.input = inp

		self.sprite = sprite.player_down

	def update(self):
		xa = ya = 0
		if self.input.up: ya -= 1
		if self.input.down: ya += 1
		if self.input.left: xa -= 1
		if self.input.right: xa += 1

		if xa != 0 or ya != 0:
			self.move(xa, ya)

	def render(self, screen):

		"""
		This silliness is because the UFO sprite
		is an odd number of pixels wide (and therefore
		isn't centered in its cell.) When it flips,
		the whole sprite appears to jump one pixel extra
		to the left. So to compensate, we use 1 fewer
		pixel when offsetting the sprite render.
		"""
		x_offset = 16

		flip = 0
		if self.direction == 0: self.sprite = sprite.player_up
		if self.direction == 1: self.sprite = sprite.player_side
		if self.direction == 2: self.sprite = sprite.player_down
		if self.direction == 3: 
			self.sprite = sprite.player_side
			x_offset = 15
			flip = 1

		# offset to center the sprite, since the player is
		# a 32x32 sprite
		screen.render_player(self.x - x_offset, self.y - 16, self.sprite, flip)
