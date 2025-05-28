from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # если index.html — твоя главная

@app.route('/webapp')  # 👈 вот это добавь
def webapp():
    return render_template('profile.html')  # или webapp.html, как хочешь

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Стартовая страница

@app.route('/webapp')
def webapp():
    return render_template('profileuser.html')  # Первая форма

@app.route('/main')
def main_menu():
    return render_template('main_menu.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/wallet')
def wallet():
    return render_template('wallet.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
    