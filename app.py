from flask import Flask, request
from color_picker import color_picker_class

#class_instance
cp = color_picker_class()

app = Flask(__name__)

@app.route('/api/color_picker_api')
def color_picker_api():
    return cp.color_picker_fun(request.args)

if __name__ == "__main__":
    app.run(debug=True)