import easyocr #pytesseract #pyautogui, keyboard
import pandas as pd
import numpy as np

from glob import glob
from tqdm.notebook import tqdm

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from PIL import Image

img_fn = glob('/home/darren/Documents/projects/AnthemFillout/Example*')

reader = easyocr.Reader(['en'], gpu = False)

results = reader.readtext(img_fn[0])

print(pd.DataFrame(results))

#print(img_fn[0])

#print(plt.imshow(plt.imread(img_fn[0])))


# with cbook.get_sample_data('/home/darren/Documents/projects/AnthemFillout/Example.png') as image_file:
#     image = plt.imread(image_file)
#     print(image)
#print(pytesseract.image_to_string(img_fn[0], lang='eng'))

