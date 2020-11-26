from pysheeter import PySheeter

# Load sprites from './files/' (all sprites are 64x64)
spritesheet = PySheeter.Sheet("files")

# Create a vertical spritesheet with the dimensions 16x16 (scaled)
spritesheet.put("example_v1616.png",(16,16))

# Create a horizontal spritesheet with the dimensions 16x32 (scaled & stretched)
spritesheet.put("example_h1632.png",(16,32),False)