from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_characters(text):
    h = {}
    for i in text:
        lowercase_string = i.lower()
        for j in lowercase_string:
            if j.isalpha():
                h[j] = h.get(j, 0) + 1

    h = dict(sorted(h.items()))
    return h

def report(char_count_dict):
    report_data = []
    for i, j in char_count_dict.items():
        report_data.append(f"The character '{i}' was found {j} times")
    return report_data

def get_num_words(text):
    words = text.split()
    return len(words)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Generate report
            text = get_book_text(filepath)
            num_words = get_num_words(text)
            char_count_dict = count_characters(text)
            report_data = report(char_count_dict)

            return render_template('report.html', num_words=num_words, report_data=report_data)

    return '''
    <!doctype html>
    <title>Upload a Text File</title>
    <h1>Upload a Text File to Generate Report</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
