from PIL import Image
import random

def cypherColoredImage(image, start, finish, keysImg):
    copiedImg = image.copy()
    pixels = copiedImg.load()
    keyPixels = keysImg.load()
    for x in range(start['x'], finish['x']):
        for y in range(start['y'], finish['y']):
            keyR = random.randrange(0, 256)
            keyG = random.randrange(0, 256)
            keyB = random.randrange(0, 256)
            keyPixels[x - start['x'], y - start['y']] = (keyR, keyG, keyB)
            r, g , b = pixels[x, y]
            cypheredR = r ^ keyR
            cypheredG = g ^ keyG
            cypheredB = b ^ keyB
            pixels[x, y] = (cypheredR, cypheredG, cypheredB)
    copiedImg.save("generated-content/cypheredImage.png")
    keysImg.save("generated-content/cypherKeys.png")

def decypherColoredImage(cyphImage, start, finish, keysImg):
    copiedCyphImg = cyphImage.copy()
    pixels = copiedCyphImg.load()
    keyPixels = keysImg.load()
    for x in range(start['x'], finish['x']):
        for y in range(start['y'], finish['y']):
            keyR, keyG, keyB = keyPixels[x - start['x'], y - start['y']]
            r, g , b = pixels[x, y]
            decypheredR = r ^ keyR
            decypheredG = g ^ keyG
            decypheredB = b ^ keyB
            pixels[x, y] = (decypheredR, decypheredG, decypheredB)
    copiedCyphImg.save("generated-content/decypheredImage.png")

def cypherMonochromaticImage(image, start, finish, keysImg):
    copiedImg = image.copy()
    pixels = copiedImg.load()
    keyPixels = keysImg.load()
    for x in range(start['x'], finish['x']):
        for y in range(start['y'], finish['y']):
            key = random.randrange(0, 256)
            keyPixels[x - start['x'], y - start['y']] = key
            pixel = pixels[x, y]
            cypheredPixel = pixel ^ key
            pixels[x, y] = cypheredPixel
    copiedImg.save("generated-content/cypheredImage.png")
    keysImg.save("generated-content/cypherKeys.png")

def decypherMonochromaticImage(cyphImage, start, finish, keysImg):
    copiedCyphImg = cyphImage.copy()
    pixels = copiedCyphImg.load()
    keyPixels = keysImg.load()
    for x in range(start['x'], finish['x']):
        for y in range(start['y'], finish['y']):
            key = keyPixels[x - start['x'], y - start['y']]
            pixel = pixels[x, y]
            decypheredPixel = pixel ^ key
            pixels[x, y] = decypheredPixel
    copiedCyphImg.save("generated-content/decypheredImage.png")

def vernamImage(image, start = {}, finish = {}):
    img = Image.open(image)
    width, height = img.size
    s = start
    f = finish
    if(len(s) == 0):
        s = {'x': 0, 'y': 0}
    if(len(f) == 0):
        f = {'x': width, 'y': height}    
    if(s['x'] > width 
       or s['y'] > height
       or f['x'] > width 
       or f['y'] > height 
       or s['x'] > f['x'] 
       or s['y'] > f['y']
    ):
        print("Start coords must be positive numbers and finish coords must be less or equal than (x: %d, y: %d" %(width, height))
        return -1
    mode = img.mode
    if(mode == "RGB"):
        # Cypher begins
        coloredKeys = Image.new(mode="RGB", size=(f['x'] - s['x'], f['y'] - s['y']))
        cypherColoredImage(img, s, f, coloredKeys)
        # Decypher begins
        cypheredColoredImg = Image.open("generated-content/cypheredImage.png")
        fullColoredKeys = Image.open("generated-content/cypherKeys.png")
        decypherColoredImage(cypheredColoredImg, s, f, fullColoredKeys)
    elif(mode == "L"):
        # Cypher begins
        monoKeys = Image.new(mode="L", size=(f['x'] - s['x'], f['y'] - s['y']))
        cypherMonochromaticImage(img, s, f, monoKeys)
        # Decypher begins
        cypheredMonoImg = Image.open("generated-content/cypheredImage.png")
        fullMonoKeys = Image.open("generated-content/cypherKeys.png")
        decypherMonochromaticImage(cypheredMonoImg, s, f, fullMonoKeys)

def main(image, start = {}, finish = {}):
    vernamImage(image, start, finish)

if __name__=="__main__":
    main("./resources/lena.bmp", {'x': 25, 'y': 25}, {'x': 225, 'y': 225})
    
