from flask import Flask, render_template, request, jsonify
from auth import add_to_database

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/registration', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        if request.is_json: # Проверяем, что данные пришли в формате JSON
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            
            if username is None or password is None:
                return jsonify({'error': 'Missing username or password'}), 400
            
            try:
                add_to_database(username, password)
                return jsonify({'message': f'User {username} successfully registered.'}), 200
            except Exception as e:
                return jsonify({'error': str(e)}), 500
        else:
            return jsonify({'error': 'Invalid JSON format'}), 400

@app.route('/login', methods=['POST', 'GET'])
def auth():
    return render_template('log_in.html')

if __name__ == '__main__':
    app.run(debug=True)