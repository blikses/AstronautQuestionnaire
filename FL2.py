from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" 
                            href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 class="center-text">Анкета претендента на участие в миссии</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" 
                                    placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" 
                                    placeholder="Введите имя" name="name">
                                    <p> </p>
                                    <input type="email" class="form-control" id="email" 
                                    placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Основное общее</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <p> </p>
                                    <p>Какие у вас есть профессии?</p>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="engineerexplorer" 
                                        name="engineerexplorer">
                                        <label class="form-check-label">Инженер-исследователь</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="engineerbuilder" 
                                        name="engineerbuilder">
                                        <label class="form-check-label">Инженер-строитель</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="pilot" 
                                        name="pilot">
                                        <label class="form-check-label">Пилот</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="meteorologist" 
                                        name="meteorologist">
                                        <label class="form-check-label">Метеоролог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="lifesafetyengineer" 
                                        name="lifesafetyengineer">
                                        <label class="form-check-label">Инженер по жизеобеспечению </label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="radiationengineer" 
                                        name="radiationengineer">
                                        <label class="form-check-label">Инженер по радиационной защите</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="doctor" 
                                        name="doctor">
                                        <label class="form-check-label">Врач</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="exobiologist" 
                                        name="exobiologist">
                                        <label class="form-check-label">Экзобиолог</label>
                                    </div>
                                    <p> </p>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" 
                                          value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" 
                                          value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <p> </p>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <p> </p>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <p> </p>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" 
                                        for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <p> </p>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form.get('engineerexplorer'))
        print(request.form.get('engineerbuilder'))
        print(request.form.get('pilot'))
        print(request.form.get('meteorologist'))
        print(request.form.get('lifesafetyengineer'))
        print(request.form.get('radiationengineer'))
        print(request.form.get('doctor'))
        print(request.form.get('exobiologist'))
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form.get('accept'))
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
