from flask import Flask, render_template, request

app = Flask(__name__)

# Пример данных пользователей с разными ролями
users = {
    "admin": {"role": "admin"},
    "moderator": {"role": "moderator"},
    "user": {"role": "user"}
}

@app.route('/')
def index():
    username = request.args.get('username', 'user')
    user = users.get(username, {"role": "user"})
    return render_template('welcome.html', role=user["role"])

if __name__ == '__main__':
    app.run(debug=True)
