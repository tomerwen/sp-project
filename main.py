from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'name': request.form.get('name'),
        'email': request.form.get('email'),
        'company': request.form.get('company')
    }
    # Here, you can perform any server-side processing with the form data
    # For simplicity, I'm just printing the data to the console
    print(data)

    return render_template("submitted.html")

if __name__ == '__main__':
    app.run(debug=True)