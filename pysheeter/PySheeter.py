import json
from PIL import Image
from pathlib import Path

# Create new sprite
class Sprite:

	def __init__(self,image,size):
		self.image = Image.open(image).convert("RGBA")

		# Resize image to size[width,height] if nessesary
		if(self.image.width != size[0] or self.image.height != size[1]):
			self.resize(size)

	# Resize image without maintaining aspect ratio
	def resize(self,size,resample=Image.LANCZOS):
		self.image = self.image.resize((size[0],size[1]),resample)

# --------------------------------

# Create new sheet of sprites
class Sheet:

	def __init__(self,folder = None):
		self.sprites = []

		# Auto-import sprite folder
		if(folder):
			self.path = Path(folder).glob("**/*.png")
			self.sprites = [x for x in self.path]

			print(f"Loaded {len(self.sprites)} sprites")

	# Concatinate sprites vertically
	def concatV(self,size):
		sheet = Image.new("RGBA",(size[0],size[1] * len(self.sprites)))

		for i, sprite in enumerate(self.sprites):
			sheet.paste(Sprite(sprite,size).image,(0,size[1] * i))

		return sheet

	# Concatinate sprites horizontally
	def concatH(self,size):
		sheet = Image.new("RGBA",(size[0] * len(self.sprites),size[1]))

		for i, sprite in enumerate(self.sprites):
			sheet.paste(Sprite(sprite,size).image,(size[0] * i,0))

		return sheet

	# Add sprite by path
	def add(self,path):
		self.sprites.append(path)

	# Remove sprite by path
	def remove(self,path):
		self.sprites.remove(path)

	# Create and save spritesheet
	def put(self,dest,size,vertical = True):
		if(vertical):
			sheet = self.concatV(size)
		else:
			sheet = self.concatH(size)

		sheet.save(dest)
		print(f"Saved spritesheet to '{dest}'")