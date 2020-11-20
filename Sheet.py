import json
from PIL import Image
from pathlib import Path

# Create new sprite
class Sprite:

	def __init__(self,image,size):
		self.image = Image.open(image).convert("RGBA")

		# Resize image to size[width,height] if nessesary
		if(self.image.width != size[0] or self.image.height != size[1]):
			self.resize()

	# Resize image without maintaining aspect ratio
	def resize(self,resample=Image.BICUBIC):
		rw = self.image.width
		rh = self.image.height

		# Scale image width
		if(rw != size[0]):
			rw = int(self.image.height * self.image.width / size[0])

		# Scale image height
		if(rh != size[1]):
			rh = int(self.image.width * size[1] / self.image.height)

		self.image = self.image.resize((rw,rh),resample)

# --------------------------------

# Create new sheet of sprites
class Sheet:

	def __init__(self,folder = None):
		self.sprites = []

		# Auto-import sprite folder
		if(folder):
			self.path = Path(folder).glob("**/*.png")
			self.sprites = [x for x in self.path]

	# Concatinate sprites vertically
	def concat(self,size):
		sheet = Image.new("RGBA",(size[0],size[1] * len(self.sprites)))

		for i, sprite in enumerate(self.sprites):
			sheet.paste(Sprite(sprite,size).image,(0,size[1] * i))

		return sheet

	# Add sprite by path
	def add(self,path):
		self.sprites.append(path)

	# Create and save spritesheet
	def put(self,dest,size):
		sheet = self.concat(size)
		sheet.save(dest)
		
		print(len(self.sprites))