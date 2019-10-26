from flask import Flask, render_template, request, make_response, jsonify
from werkzeug.utils import secure_filename
import jwt
import datetime
from functools import wraps
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234JWTAPI'

limiter = Limiter(app, key_func=get_remote_address)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(*args, **kwargs)
    return decorated


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        img = request.files['image']
        try:
            img.save(secure_filename(img.filename))
        except:
            return '<h2>No selected image</h2>'
        return f'<h2>Image Uploaded</h2> Image Name : <mark>{img.filename}</mark>'


@app.route('/api')
@token_required
@limiter.limit('5/minute')
def testAPT():
    return jsonify({'API': 'This is only available for people with valid token.'})


@app.route('/token')
def get_token():
    auth = request.authorization
    if auth and auth.password == 'pass':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                           app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})
    return make_response('could not verify!', 401, {'www-Authenticate': 'Basic realm = "Login Required"'})


if __name__ == '__main__':
    app.run(debug=True)
