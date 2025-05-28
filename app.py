from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def start():
    return redirect(url_for('form'))

@app.route('/form')
def form():
    return render_template('profileuser.html')  # первая форма с именем и фото

@app.route('/main')
def main():
    return render_template('main_menu.html')  # главное меню

@app.route('/education')
def education():
    return render_template('education.html')  # раздел с обучением

@app.route('/settings')
def settings():
    return render_template('settings.html')  # настройки профиля

@app.route('/wallet')
def wallet():
    return render_template('wallet.html')  # кошелек

@app.route('/profile')
def profile():
    return render_template('profile.html')  # аналитика/личный кабинет

if __name__ == '__main__':
    app.run(debug=True)
