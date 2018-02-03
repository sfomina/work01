

def create(img):
    color = "0 0 0 "
    for i in range(500):
        if i % 50 == 0:
            if color == "0 0 0 ":
                color = "255 255 255 "
            else :
                color = "0 0 0 "
        for x in range(500):
            img.write(color)
            if x % 50 == 0:
                if color == "0 0 0 ":
                    color = "255 255 255 "
                else :
                    color = "0 0 0 "








f = open("image.ppm", "w")
f.write("P3\n500 500\n255\n")
create(f)
f.close() 
