from flask import Flask, request, render_template, send_file

app = Flask(__name__)
out_file = 'output.txt'

def write_file(filename, text):
    with open(filename, "w") as f:
        f.write(text)
    return True


@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')


@app.route('/text', methods=['POST'])
def write_file_from_text():
    res_json = request.get_json()
    res_text = res_json['text']
    print('res_text:', res_text)
    write_file(out_file, res_text)
    return send_file(out_file, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
