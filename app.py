import picam

i = picam.takePhoto()

for i in range(1, 11):
    i.save(os.path.join(os.getcwd(), 'image{}.jpg'.format(i)))
