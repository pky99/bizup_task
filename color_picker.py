import cv2
import numpy as np
import urllib


class color_picker_class:
    def color_picker_fun(self, url_args):
        '''url_args: url attribute given to api '''

        #retrieve image from url
        url = url_args['url']
        url_response = urllib.urlopen(url)
        img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, -1)

        #logo_border
        logo_border=self.major_color(img[:, :, :3])

        #dominant_color
        dominant_color=self.major_color(img[:, :, :3])

        #output
        out = {"logo_border": self.bgr2hex(*logo_border) , "dominant_color": self.bgr2hex(*dominant_color)}
        return out

    def border_color(self, img):
        '''img: the image for which border color is needed'''
        return img[0][0]

    def bgr2hex(self, b, g, r):
        '''function to convert bgr color codes to hexadecimal format'''

        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    def major_color(self, a):
        '''function to find major/dominant color of an image
            a: image given'''

        a = a.reshape(-1, a.shape[-1])
        colors, count = np.unique(a, axis=0, return_counts=True)
        return colors[count.argmax()]
