from flask import Flask, jsonify, request
import cv2
import numpy as np
import urllib

def rgb2hex(b, g, r):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def unique_count_app(a):
    a=a.reshape(-1,a.shape[-1])
    colors, count = np.unique(a, axis=0, return_counts=True)
    out={"logo_border":rgb2hex(*a[-1]),"dominant_color":rgb2hex(*colors[count.argmax()])}
    return out

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"
@app.route('/api/test')
def test():
    args = request.args
    url=args['url']
    url_response = urllib.urlopen(url)
    img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)
    return unique_count_app(img[:,:,:3])

if __name__ == "__main__":
    app.run(debug=True)