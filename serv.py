from flask import Flask, render_template, request, jsonify, url_for
from auth import add_to_database, check_user, connect
from dialog import add_to_dialog_session
import hashlib as h
# import bcrypt as bc

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        if request.is_json: # Проверяем, что данные пришли в формате JSON
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')

            username_hash = h.sha256(username.encode()).hexdigest()
            password_hash = h.sha256(password.encode()).hexdigest()
            
            if username is None or password is None:
                return jsonify({'error': 'Missing username or password'}), 400
            
            try:
                connect(add_to_database(username_hash, password_hash))
                return jsonify({'message': f'User {username} successfully registered.'}), 200
            except Exception as e:
                return jsonify({'error': str(e)}), 500
        else:
            return jsonify({'error': 'Invalid JSON format'}), 400

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('log_in.html')
    elif request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            username = data['username']
            password = data['password']

            usr_hash = h.sha256(username.encode()).hexdigest()
            pswrd_hash = h.sha256(password.encode()).hexdigest()

            if username is not None and password is not None:
                if check_user(usr_hash, pswrd_hash):
                   return jsonify({'url': url_for('account')})
                else:
                    return 'Попробуйте еще раз'

@app.route('/Welcome')
def account():
    return render_template('welcome.html')

@app.route('/work', methods=['GET', 'POST'])
def work():
    if request.method == 'GET':
        return render_template('work.html')
    elif request.method == 'POST':
        if request.json:
            data = request.get_json()
            message = data['message']
            add_to_dialog_session(message)
            return jsonify({'message': f'{message}'})

if __name__ == '__main__':
    app.run(debug=True)