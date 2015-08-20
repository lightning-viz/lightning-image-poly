from lightning import Lightning
from sklearn import datasets

lgn = Lightning()

imgs = datasets.load_sample_images()

lgn.imagepoly(imgs[0])