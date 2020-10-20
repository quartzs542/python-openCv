from Sketch_model import Sketch

for i in range(1,8):
    car = Sketch("images/{}.jpg".format(i),"sketches","car{}.jpg".format(i))
    car.sketchit()
