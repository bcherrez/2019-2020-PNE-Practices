from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    apache = request.form['apache']
    saps = request.form['saps']
    charlson = request.form['charlson']
    institucionalizado = request.form['institucionalizado']
    estadoc = request.form['estadoc']
    fechaing = request.form['fechaing']
    fechauci = request.form['fechauci']
    fechahosp = request.form['fechahosp']
    sintomaf = request.form.getlist('sintomaf')
    dificultadr = request.form['dificultadr']
    sintomas = request.form.getlist('sintomas')
    sintoma = request.form.getlist('sintoma')
    sintomab = request.form.getlist('sintomab')
    sintomact = request.form.getlist('sintomact')
    observaciones = request.form['observaciones']
    deficitn = request.form['deficitn']
    otross = request.form['otross']
    seguimiento = request.form['seguimiento']

    return render_template('submit.html', name=name, age=age, gender=gender, apache=apache, saps=saps,
                           charlson=charlson,
                           institucionalizado=institucionalizado, estadoc=estadoc, fechaing=fechaing, fechauci=fechauci,
                           fechahosp=fechahosp, sintomaf=sintomaf, dificultadr=dificultadr,
                           sintomas=sintomas, sintoma=sintoma, sintomab=sintomab, sintomact=sintomact,
                           observaciones=observaciones, deficitn=deficitn, otross=otross, seguimiento=seguimiento)


if __name__ == '__main__':
    app.run(debug=True)
