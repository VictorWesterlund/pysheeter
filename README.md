# PySheeter
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/VictorWesterlund/pysheeter?include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/VictorWesterlund/pysheeter)
![Maintenance](https://img.shields.io/maintenance/yes/2020)

Lightweight Pillow Python package to create and scale sprite sheets from individual PNGs or whole folders

## Get started / Basic usage
1. Download and install the latest version of [Python 3](https://www.python.org/downloads/) for your architecture
2. Install the latest build of PySheeter with [`pip3`](https://pypi.org/project/pysheeter/)
```bash
$ python3 -m pip install pysheeter
```
### Sprite sheet from folder
1. Import `Sheet` from `pysheeter`
```python
from pysheeter import PySheeter
```
2. Initialize the class with a path to your PNG-folder
```python
spritesheet = PySheeter.Sheet("example/")
```
3. Create a sprite sheet with `put()`
```python
spritesheet.put("example_v1616.png",(16,16)) 
# Creates a vertical spritesheet named 'example_v1616.png' with the dimensions 16x16px (scaled automatically)
```

__Example usage:__
```python
# from 'example.py'
from pysheeter import PySheeter

# Load sprites from './files/' (all sprites are 64x64)
spritesheet = PySheeter.Sheet("example")

# Create a vertical spritesheet with the dimensions 16x16 (scaled)
spritesheet.put("example_v1616.png",(16,16))

# Create a horizontal spritesheet with the dimensions 16x32 (scaled & stretched)
spritesheet.put("example_h1632.png",(16,32),False)
```
![Example 1](https://storage.googleapis.com/public.victorwesterlund.com/github/VictorWesterlund/pysheeter/1example_v1616.png)
![Example 2](https://storage.googleapis.com/public.victorwesterlund.com/github/VictorWesterlund/pysheeter/1example_h1632.png)
### Sprite sheet from individual PNG-images
1. Import `Sheet` from `pysheeter`
```python
from pysheeter import PySheeter
```
2. Initialize the class without any arguments
```python
spritesheet = PySheeter.Sheet()
```
3. Add PNG-images with `add()`
```python
spritesheet.add("example/1.png")
spritesheet.add("example/2.png")
spritesheet.add("example/3.png")
...
```
4. Remove PNG-images with `remove()`
```python
spritesheet.remove("example/2.png")
```
5. Create a sprite sheet with `put()`
```python
spritesheet.put("example_v1616.png",(16,16)) 
# Creates a vertical spritesheet named 'example_v1616.png' with the dimensions 16x16px (scaled automatically)
```

__Example usage:__
```python
from pysheeter import PySheeter

# Load sprites from 'example/'
spritesheet = PySheeter.Sheet()

# Add PNG-images
spritesheet.add("example/1.png")
spritesheet.add("example/2.png")
spritesheet.add("example/3.png")
spritesheet.add("example/7.png")
spritesheet.add("example/5.png")
spritesheet.add("example/9.png")

# Create a vertical spritesheet with the dimensions 16x16
spritesheet.put("example_v1616.png",(16,16))

# Create a horizontal spritesheet with the dimensions 16x32
spritesheet.put("example_h1632.png",(16,32),False)
```
![Example 1](https://storage.googleapis.com/public.victorwesterlund.com/github/VictorWesterlund/pysheeter/2example_v1616.png)
![Example 2](https://storage.googleapis.com/public.victorwesterlund.com/github/VictorWesterlund/pysheeter/2example_h1632.png)
