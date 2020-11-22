from pysheeter import PySheeter

# Load sprites from 'example/'
spritesheet = PySheeter.Sheet("example")

# Create a vertical spritesheet with the dimensions 16x16
spritesheet.put("example_v1616.png",(16,16))

# Create a horizontal spritesheet with the dimensions 16x32
spritesheet.put("example_h1632.png",(16,32),False)