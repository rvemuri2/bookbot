from flask import Flask, request, render_template, redirect, url_for, jsonify
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
    lowercase_string = text.lower()
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
        if 'file' not in request.files:
            return redirect("/")
        file = request.files['file']
        if file.filename == '':
            return redirect("/")
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            text = get_book_text(filepath)
            num_words = get_num_words(text)
            char_count_dict = count_characters(text)
            report_data = report(char_count_dict)

            return render_template('report.html', num_words=num_words, report_data=report_data)

    return render_template('upload.html')

@app.route('/delete-all', methods=['POST'])
def delete_all_files():
    folder = app.config['UPLOAD_FOLDER']
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                print(f"Deleted file: {file_path}")  
            else:
                print(f"Not a file: {file_path}")  
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")
            return jsonify({'status': 'Error deleting files'}), 500

    return jsonify({'status': 'All files deleted successfully'}), 200

if __name__ == "__main__":
    app.run(debug=True)
