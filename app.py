from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# 🟢 Перенаправление на форму при старте
@app.route('/')
def start():
    return redirect(url_for('form'))

# 🟢 Форма ввода имени, даты и фото
@app.route('/form')
def form():
    return render_template('profileuser.html')  # форма регистрации

# 🟢 Главное меню
@app.route('/main')
def main():
    return render_template('main_menu.html')  # главное меню

# 🟢 Раздел обучения
@app.route('/education')
def education():
    return render_template('education.html')

# 🟢 Настройки профиля
@app.route('/settings')
def settings():
    return render_template('settings.html')

# 🟢 Личный кабинет / кошелёк
@app.route('/wallet')
def wallet():
    return render_template('wallet.html')

# 🟢 Профиль просмотр
@app.route('/profile')
def profile():
    return render_template('profile.html')

# 🟢 Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
