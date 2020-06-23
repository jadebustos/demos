#!/usr/bin/python

import urllib.request
import string
import random
import ssl
import os

# script to download some pictures from cats and dogs from the internet

DOWNLOAD_DIR='data/predict'

images = ['https://img.europapress.es/fotoweb/fotonoticia_20170622121827-17062170019_800.jpg', 'https://images-na.ssl-images-amazon.com/images/I/917iZaaFOgL._SX425_.jpg',
          'https://static.boredpanda.com/blog/wp-content/uploads/2019/04/adorable-hairless-sphynx-kittens-fb5-png__700.jpg',
	  'https://getleashedmag.com/wp-content/uploads/2017/01/spynh-feature.jpg', 
          'https://i.redd.it/5m71nu9uv7q31.jpg', 
          'https://media.malaymail.com/uploads/articles/2020/2020-06/kitzia0906.jpg',
	  'https://i.pinimg.com/236x/01/80/a7/0180a7d569f6a2a5455b7ff38fb21c10--veronica-lake-amazing-hair.jpg',
	  'https://www.elheraldo.co/sites/default/files/styles/width_860/public/articulo/2018/05/12/perro.jpg?itok=o-V5_DxL', 'https://pictures-of-cats.org/wp-content/uploads/2018/03/Sphynx-cat-by-Helmi-Flick-X.jpg',
	  'https://media.metrolatam.com/2019/01/29/memeperrodrogado-42777b43147e26a68fab3fd0729b24a3-600x400.jpg',
	  'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/American_Eskimo_Dog_1.jpg/245px-American_Eskimo_Dog_1.jpg',
	  'https://www.dogalize.com/wp-content/uploads/2017/05/551-pdengo-portugues-cerdoso-grande.jpg', 'https://d17fnq9dkz9hgj.cloudfront.net/uploads/2018/04/Minskin_01.jpg',
	  'https://cdn.fstoppers.com/styles/large-16-9/s3/lead/2018/12/cat-parody-instagram-removal.jpg',
	  'http://www.sosgalgos.com/wp-content/uploads/2018/04/Puskas01_620x400.jpg']

ssl._create_default_https_context = ssl._create_unverified_context

for image in images:
  random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=15))
  filename = os.path.join(DOWNLOAD_DIR, random_name + '.jpg')
  print("Downloading " + image)
  print("Filename: " + filename)
  print("----")
  urllib.request.urlretrieve (image, filename)
