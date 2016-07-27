import pygame
from pygame.locals import *

from entity import Mob
from graphics import sprite

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

	def render(self, screen):
		# offsets to center the sprite, since the player is
		# a 2x2 sprite blob
		xx = self.x - 16
		yy = self.y - 16

		screen.render_player(xx,    yy,    sprite.player0)
		screen.render_player(xx+16, yy,    sprite.player1)
		screen.render_player(xx,    yy+16, sprite.player2)
		screen.render_player(xx+16, yy+16, sprite.player3)
