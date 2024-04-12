from PIL import Image

def cypherVernamImage(image, start = {}, finish = {}):
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
        return -1
    mode = img.mode
    for x in range(start['x'], finish['x'] + 1):
        for y in range(start['y'], finish['y'] + 1):
            if(mode == "RGB"):
                
            img[[x], [y]]

def main(image, start, finish):
    success = cypherVernamImage(image, start, finish)

if __name__=="__main__":
    main("./resources/barries.jpg", {'x': 25, 'y': 25}, {'x': 125, 'y': 125})
    
