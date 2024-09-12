from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('keyboard.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    input_text = data.get('inputText')
    
    # Do something with the input (e.g., process it)
    processed_text = f"You typed: {input_text}"

    return jsonify(result=processed_text)

if __name__ == '__main__':
    app.run(debug=True)
