from typing import Union
from pathlib import Path

from PIL import Image

# Create new sprite
class Sprite:
	def __init__(self, image: str, resize: Union[tuple, list] = None):
		self.image = Image.open(image).convert("RGBA")

		# Resize image if necessary
		if (resize):
			self.resize(resize)

	# Resize image without maintaining aspect ratio
	def resize(self, size: Union[tuple, list], resample = Image.LANCZOS):
		self.image = self.image.resize((size[0], size[1]), resample)

# --------------------------------

# Create new sheet of sprites
class Sheet:
	def __init__(self, folder: str = None):
		self.sprites = []

		# Auto-import PNGs from folder
		if(folder):
			self.path = Path(folder).glob(f"**/*.png")
			self.sprites = [x for x in self.path]

	# Concatinate sprites vertically
	def concat_vertical(self, size: Union[tuple, list]):
		sheet_size = (size[0], size[1] * len(self.sprites))
		sheet = Image.new("RGBA", sheet_size)

		for i, sprite in enumerate(self.sprites):
			sheet.paste(Sprite(sprite, size).image, (0, size[1] * i))

		return sheet

	# Concatinate sprites horizontally
	def concat_horizontal(self, size: Union[tuple, list]):
		sheet_size = (size[0] * len(self.sprites), size[1])
		sheet = Image.new("RGBA", sheet_size)

		for i, sprite in enumerate(self.sprites):
			sheet.paste(Sprite(sprite, size).image, (size[0] * i, 0))

		return sheet

	# Add sprite by path
	def add(self, path: str):
		self.sprites.append(path)

	# Remove sprite by path
	def remove(self, path: str):
		self.sprites.remove(path)

	# Create and save spritesheet
	def put(self, dest: str, size: Union[tuple, list], vertical: bool = True):
		if(vertical):
			sheet = self.concat_vertical(size)
		else:
			sheet = self.concat_horizontal(size)

		sheet.save(dest)