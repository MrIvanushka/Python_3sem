import numpy as np
from PIL import Image


for i in range(1, 4):
    data = np.array(Image.open('pics/lunar0' + str(i) + '_raw.jpg'))
    updated_data = (data - data.min()) * int(255/(data - data.min()).max())
    res_img = Image.fromarray(updated_data)
    res_img.save('pics/res/res0' + str(i) + '.jpg')