# All blocks on map

import pygame
import globals as globs

from graphics.baseclasses import Surface, Sprite

class Block(Sprite):
	def __init__(self, xy, flags=[], wh=(50,50), bgColor=None, alpha=None):
		Sprite.__init__(self, xy, wh)

		self.bgColor = bgColor

		if not 'uncollidable' in flags:
			globs.currentgame.collidableBlocks.add(self)
			self.collidable = True
		else:
                        self.collidable = False
		if 'climbable' in flags:
			globs.currentgame.climbableBlocks.add(self)
		if 'actionBlock' in flags:
			globs.currentgame.actionBlocks.add(self)
		if 'worldActionBlock' in flags:
			globs.currentgame.worldActionBlocks.add(self)

		if bgColor:
			self.image.fill(self.bgColor)
		if alpha:
			self.image.set_alpha(alpha)

	def blitDecoration(self, xy):
		pass

class Block_000(Block):
	'''
	Stone
	'''
	def __init__(self, xy):
		Block.__init__(self, xy, bgColor=(150,150,150))
		self.image = pygame.image.load(globs.datadir+"/png/blocks/stone.png")
		self.image.convert()

class Block_001(Block):
	'''
	Dirt
	'''
	def __init__(self, xy):
		Block.__init__(self, xy, bgColor=(65,55,40))
		self.image = pygame.image.load(globs.datadir+"/png/blocks/dirt.png")
		self.image.convert()

class Block_002(Block):
	'''
	Grass
	'''
	def __init__(self, xy):
		Block.__init__(self, xy, bgColor=(50,200,50))
		grasswh = (60,25)
		self.image = pygame.image.load(globs.datadir+"/png/blocks/grass.png")
		self.image.convert()
		self.grass = Sprite(self.rect.topleft, grasswh)
		self.grass.image.set_colorkey((255,0,255))
		self.grass.image = pygame.image.load(globs.datadir+"/png/blocks/002_decoration.png")
		self.grass.image.convert()
		self.grass.image.convert_alpha()

	def blitDecoration(self, xy):
		self.grass.rect.topleft = (self.rect.x-5, self.rect.y-20)
		self.grass.worldBlit()

class Block_010(Block):
	'''
	Bush
	'''
	def __init__(self, xy):
		Block.__init__(self, xy, bgColor=(30,150,30), flags=['uncollidable', 'actionBlock'])

class Block_020(Block):
	'''
	Wood
	'''
	def __init__(self, xy):
		Block.__init__(self, xy, bgColor=(90,70,55), flags=['uncollidable'])
		pygame.draw.line(self.image, (0,0,0), (0,0), (50,0))

class Block_021(Block):
	'''
	Wood Vertical
	'''
	def __init__(self, xy):
		Block.__init__(self, xy, bgColor=(70,60,48), flags=['uncollidable'])
		pygame.draw.line(self.image, (0,0,0), (0,0), (0,50))

class Block_022(Block):
	'''
	Wooden Door Top
	'''
	def __init__(self, xy):
		Block.__init__(self, xy, bgColor=(100,75,60), flags=['uncollidable'])
		pygame.draw.line(self.image, (0,0,0), (0,0), (49,0))
		pygame.draw.line(self.image, (0,0,0), (0,0), (0,49))
		pygame.draw.line(self.image, (0,0,0), (49,0), (49,49))
		pygame.draw.circle(self.image, (50,50,50), (40,40), 7)

class Block_023(Block):
	'''
	Wooden Door Bottom
	'''
	def __init__(self, xy):
		Block.__init__(self, xy, bgColor=(100,75,60), flags=['uncollidable', 'action'])
		pygame.draw.line(self.image, (0,0,0), (0,0), (0,49))
		pygame.draw.line(self.image, (0,0,0), (49,0), (49,49))

class Block_025(Block):
	'''
	Collidable Wood
	'''
	def __init__(self, xy):
		Block.__init__(self, xy, bgColor=(70,60,48), flags=['uncollidable'])
		pygame.draw.line(self.image, (0,0,0), (0,0), (50,0))

class Block_026(Block):
	'''
	Collidable Wood Vertical
	'''
	def __init__(self, xy):
		Block.__init__(self, xy, bgColor=(70,60,48), flags=[])
		pygame.draw.line(self.image, (0,0,0), (0,0), (0,50))

class Block_050(Block):
	'''
	Glass
	'''
	def __init__(self, xy):
		Block.__init__(self, xy, bgColor=(255,255,255), alpha=150)

class Block_150(Block):
	'''
	Background Glass
	'''
	def __init__(self, xy):
		Block.__init__(self, xy, bgColor=(255,255,255), alpha=150, flags=['uncollidable'])

class Block_999(Block):
	'''
	Void
	'''
	def __init__(self, xy):
		Block.__init__(self, xy, bgColor=(0,0,0))
