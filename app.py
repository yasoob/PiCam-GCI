import picam
import os

for i in range(1, 11):
    pic = picam.takePhoto()
    pic.save(os.path.join(os.getcwd(), 'image{}.jpg'.format(i)))
