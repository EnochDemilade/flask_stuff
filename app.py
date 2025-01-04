from flask import Flask, render_template, request, Response
from flask_cors import CORS
import pandas as pd

app = Flask(__name__, template_folder="templates")
CORS()


@app.route('/', methods=['GET', 'POST', ])
def index():
    if request.method == 'GET':
        return render_template('first.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'Demilade1sc00l' and password == 'Y04 4r3 h0t':
            return '<h1>Success</h1>'
        else:
            return '<h1>Failure</h1>'


@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    if file.content_type == 'text/csv':
        df = pd.read_csv(file)
        return df.to_html()
    elif file.content_type == 'text/plain':
        return file.read().decode()
    else:
        return "<h1>Error Check the file or it may be on our end</h1>"


@app.route('/convert_excel')
def convert_excel():
    file = request.files['file2']
    df = pd.read_csv(file)



app.run(host='0.0.0.0', port=3000, debug=True)
