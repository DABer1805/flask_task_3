from flask import Flask, url_for

app = Flask(__name__)

PROMOTION_LIST = [
    'Человечество вырастает из детства.',
    'Человечеству мала одна планета.',
    'Мы сделаем обитаемыми безжизненные пока планеты.',
    'И начнем с Марса!',
    'Присоединяйся!'
]


@app.route('/')
def get_title():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def get_slogan():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def get_promotion():
    return '</br>'.join(PROMOTION_LIST)


@app.route('/image_mars')
def get_image_mars():
    return f'''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Привет, Марс!</title>
      <body>
        <h1>Жди нас, Марс!</h1>
        <img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
        <div>Вот она красная планета</div>
      </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
