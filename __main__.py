from pysheeter.pysheeter import Sheet as SpriteSheet

# Simple PySheeter CLI
def main():
    print("Welcome to the PySheeter CLI")

    # Gather parameters from user input
    folder = str(input("Enter path to folder of sprites:\n"))
    ext = str(input("Enter the file extension of these sprites (without dot, 'png', 'jpg' etc.):\n"))
    size = int(input("What width in pixels do you want each sprite to be? (1:1 aspect ratio):\n"))
    vertical = not bool(input("Do you want a vertical sprite sheet? [Y,n]:\n"))
    dest = str(input("Finally, enter a file name (or path) for the sprite sheet:\n"))

    print("Reading sprites from folder...")
    sheet = SpriteSheet(folder, ext)
    
    print("Creating sprite sheet...")
    sheet.put(dest, (size, size), vertical)
    
    print("Done!")

if __name__ == "__main__":
    main()