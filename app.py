from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/sitio/home.html')

@app.route('/mi_hospital')
def mi_hospital():
    return render_template('sitio/mi_hospital.html')

@app.route('/blog')
def blog():
    return render_template('sitio/blog.html')

@app.route('/teleconsulta')
def teleconsulta():
    return render_template('sitio/teleconsulta.html')

@app.route('/gin_obs')
def gin_obs():
    return render_template('sitio/gin_obs.html')

@app.route('/videolap')
def videolap():
    return render_template('sitio/videolap.html')

@app.route('/salud_tic')
def salud_tic():
    return render_template('sitio/salud_tic.html')

@app.route('/destacado')
def destacado():
    return render_template('sitio/destacado.html')


if __name__ == '__main__':
    app.run(debug=True)