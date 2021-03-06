import pygame

class Tile(pygame.sprite.Sprite):
	def __init__(self, pos = [0,0]):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = pygame.image.load("Resources/Objects/Wall/Tile.png")
		self.rect = self.image.get_rect()
		self.place(pos)
		self.living = True
		
	def place(self, pos):
		self.rect.topleft = pos
		
	def update(*args):
		self = args[0]
