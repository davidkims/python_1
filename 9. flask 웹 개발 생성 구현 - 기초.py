from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from wtforms import FileField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class UploadForm(FlaskForm):
    file = FileField()

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.file.data
        filename = secure_filename(f.filename)
        f.save(filename)
        return 'File saved'
    return render_template('upload.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
