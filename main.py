from flask import Flask, request, render_template, url_for

app = Flask(__name__)
last_image = None

professions = [
    'инженер-исследователь',
    'пилот',
    'строитель',
    'экзобиолог',
    'врач',
    'инженер по терраформированию',
    'климатолог',
    'специалист по радиационной защите',
    'астрогеолог',
    'гляциолог',
    'инженер жизнеобеспечения',
    'метеоролог',
    'оператор марсохода',
    'киберинженер',
    'штурман',
    'пилот дронов'
]

planets_data = {
    'Марс': [
        'Эта планета близка к Земле;',
        'На ней много необходимых ресурсов;',
        'На ней есть вода и атмосфера;',
        'На ней есть небольшое магнитное поле;',
        'Наконец, она просто красива!'
    ],
    'Венера': [
        'Ближайшая планета к Земле;',
        'По размеру похожа на Землю;',
        'Имеет плотную атмосферу;',
        'Яркий объект на небе;',
        'Можно изучать с Земли!'
    ],
    'Юпитер': [
        'Самая большая планета;',
        'Защищает Землю от астероидов;',
        'Имеет много спутников;',
        'Газовый гигант;',
        'Уникальная атмосфера!'
    ],
    'Сатурн': [
        'Планета с красивыми кольцами;',
        'Вторая по величине планета;',
        'Много интересных спутников;',
        'Уникальная структура;',
        'Легко найти на небе!'
    ],
    'Луна': [
        'Ближайшее космическое тело;',
        'Уже были экспедиции;',
        'Можно использовать как базу;',
        'Близко к Земле;',
        'Отличный старт для освоения!'
    ]
}

alert_colors = ['alert-light', 'alert-success', 'alert-secondary', 'alert-warning', 'alert-danger']

@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'

@app.route('/index/<title>')
def index(title='Заготовка'):
    return render_template('index.html', title=title)


@app.route('/promotion')
def promotion():
    promo = (
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    )
    return '</br>'.join(promo)


@app.route('/image_mars')
def return_sample_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                  <meta charset="utf-8">
                  <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="https://img.freepik.com/premium-psd/psd-file-image-planet-mars-transparent-background-3_515427-3362.jpg">
                    <p>Вот она какая красная планета</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html> 
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="https://img.freepik.com/premium-psd/psd-file-image-planet-mars-transparent-background-3_515427-3362.jpg">
                    <div class="alert alert-secondary" role="alert">Человечество вырастает из детства.</div>
                    <div class="alert alert-success" role="alert">Человечеству мала одна планета.</div>
                    <div class="alert alert-secondary" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</div>
                    <div class="alert alert-warning" role="alert">И начнем с Марса!</div>
                    <div class="alert alert-danger" role="alert">Присоединяйся!</div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def survey():
    if request.method == 'GET':
        return f'''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Анкета астронавта</title>
                  </head>
                  <body>
                    <h1>Анкета отбора астронавтов</h1>
                    <form class="login_form" method="post" enctype="multipart/form-data">
                        <input type="text" class="form-control" placeholder="Фамилия" name="surname"><br>
                        <input type="text" class="form-control" placeholder="Имя" name="name"><br>
                        <input type="email" class="form-control" placeholder="Email" name="email"><br>
                        
                        <label for="education">Образование</label>
                        <select class="form-control" id="education" name="education">
                          <option value="school">Среднее</option>
                          <option value="college">Среднее специальное</option>
                          <option value="bachelor">Бакалавр</option>
                          <option value="master">Магистр</option>
                          <option value="phd">Кандидат наук</option>
                        </select><br>
                        
                        <label>Какие у Вас профессии?</label><br>
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" name="profession" id="prof1" value="engineer_researcher">
                          <label class="form-check-label" for="prof1">Инженер-исследователь</label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" name="profession" id="prof2" value="pilot">
                          <label class="form-check-label" for="prof2">Пилот</label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" name="profession" id="prof3" value="builder">
                          <label class="form-check-label" for="prof3">Строитель</label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" name="profession" id="prof4" value="exobiologist">
                          <label class="form-check-label" for="prof4">Экзобиолог</label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" name="profession" id="prof5" value="doctor">
                          <label class="form-check-label" for="prof5">Врач</label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" name="profession" id="prof6" value="terraforming_engineer">
                          <label class="form-check-label" for="prof6">Инженер по терраформированию</label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" name="profession" id="prof7" value="climatologist">
                          <label class="form-check-label" for="prof7">Климатолог</label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" name="profession" id="prof8" value="radiation_specialist">
                          <label class="form-check-label" for="prof8">Специалист по радиационной защите</label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" name="profession" id="prof9" value="astrogeologist">
                          <label class="form-check-label" for="prof9">Астрогеолог</label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" name="profession" id="prof10" value="glaciologist">
                          <label class="form-check-label" for="prof10">Гляциолог</label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" name="profession" id="prof11" value="life_support_engineer">
                          <label class="form-check-label" for="prof11">Инженер жизнеобеспечения</label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" name="profession" id="prof12" value="meteorologist">
                          <label class="form-check-label" for="prof12">Метеоролог</label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" name="profession" id="prof13" value="rover_operator">
                          <label class="form-check-label" for="prof13">Оператор марсохода</label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" name="profession" id="prof14" value="cyber_engineer">
                          <label class="form-check-label" for="prof14">Киберинженер</label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" name="profession" id="prof15" value="navigator">
                          <label class="form-check-label" for="prof15">Штурман</label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="checkbox" name="profession" id="prof16" value="drone_pilot">
                          <label class="form-check-label" for="prof16">Пилот дронов</label>
                        </div><br>
                        
                        <label>Пол</label><br>
                        <div class="form-check">
                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                          <label class="form-check-label" for="male">Мужской</label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                          <label class="form-check-label" for="female">Женский</label>
                        </div><br>
                        
                        <label for="motivation">Почему Вы хотите принять участие в миссии?</label>
                        <textarea class="form-control" id="motivation" rows="3" name="motivation"></textarea><br>
                        
                        <label for="photo">Приложите фотографию</label>
                        <input type="file" class="form-control-file" id="photo" name="file"><br><br>
                        
                        <div class="form-check">
                          <input type="checkbox" class="form-check-input" id="stay" name="stay" value="yes">
                          <label class="form-check-label" for="stay">Готов остаться на Марсе?</label>
                        </div><br>
                        
                        <button type="submit" class="btn btn-primary">Отправить</button>
                    </form>
                  </body>
                </html>'''
    elif request.method == 'POST':
        print(request.form.get('surname'))
        print(request.form.get('name'))
        print(request.form.get('email'))
        print(request.form.get('education'))
        print(request.form.getlist('profession'))
        print(request.form.get('sex'))
        print(request.form.get('motivation'))
        print(request.form.get('stay'))
        f = request.files.get('file')
        if f:
            print(f.filename)
        return "Анкета отправлена"

@app.route('/choice/<planet_name>')
def choice(planet_name):
    arguments = planets_data.get(planet_name, [
        'Интересный выбор!',
        'Требует изучения;',
        'Много возможностей;',
        'Перспективное направление;',
        'Начнем освоение!'
    ])
    
    html = f'''<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
    <title>Выбор планеты</title>
  </head>
  <body>
    <h1 class="p-3">Мое предложение: {planet_name}</h1>
'''
    
    for i, arg in enumerate(arguments):
        color_class = alert_colors[i % len(alert_colors)]
        html += f'    <div class="alert {color_class} m-0 rounded-0" role="alert">{arg}</div>\n'
    
    html += '''  </body>
</html>'''
    
    return html


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    html = f'''<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
    crossorigin="anonymous">
    <title>Результаты отбора</title>
  </head>
  <body>
    <h1 class="p-3">Результаты отбора</h1>
    <h2 class="px-3">Претендента на участие в миссии {nickname}:</h2>
    <div class="alert alert-success m-0 rounded-0" role="alert">
      Поздравляем! Ваш рейтинг после {level} этапа отбора составляет {rating}!
    </div>
    <div class="alert alert-warning m-0 rounded-0" role="alert">
      Желаем удачи!
    </div>
  </body>
</html>'''
    
    return html

@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    global last_image
    
    if request.method == 'POST':
        f = request.files['file']
        if f and f.filename:
            last_image = f.filename
            f.save(f'static/img/{f.filename}')
        return "Фотография загружена"
    
    return render_template('load_photo.html', image=last_image)

@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    return render_template('list_prof.html', 
                          title='Список профессий',
                          list_type=list_type, 
                          professions=professions)

@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    param = {}
    param['title'] = 'Анкета'
    param['surname'] = 'Watny'
    param['name'] = 'Mark'
    param['education'] = 'выше среднего'
    param['profession'] = 'штурман марсохода'
    param['sex'] = 'male'
    param['motivation'] = 'Всегда мечтал застрять на Марсе!'
    param['ready'] = 'True'
    
    return render_template('auto_answer.html', **param)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')