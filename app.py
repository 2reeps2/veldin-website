from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static")

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/services')
def services():
    return send_from_directory(app.static_folder, 'services.html')

@app.route('/contact')
def contact():
    return send_from_directory(app.static_folder, 'contact.html')

if __name__ == "__main__":
    app.run(debug=True)