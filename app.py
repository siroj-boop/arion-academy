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
