from PIL import Image
im = Image.open('westbrook.jpg')
w = im.size[0]
h = im.size[1]
Q2 = Image.new("RGB", (w, h))
def fun(x):
    return x*0.5

Q2 = Image.eval(im, fun)
Q2.save('Q2.jpg')
Q2.show()