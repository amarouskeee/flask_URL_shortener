import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # получает строки из БД
    return conn

app = Flask(__name__)
app.config['SECRET_KEY'] = 'try-to-guess'


@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()  # подключаемся к БД
    if request.method == 'POST':  # если форма отправляется
        url = request.form['url']  # сохраняю урл из формы в переменную
        if not url:  # если поле передали пустым
            flash('The URL is required!')
            return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(adress='0.0.0.0')
