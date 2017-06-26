from flask import Flask, render_template, redirect, url_for
from ai import tah_pocitace
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/druha_stranka')
def druha_stranka():
    return 'druhá stránka'

@app.route('/users/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/piskvorky/<pole>')
@app.route('/piskvorky/<pole>/<pozice>')
def piskvorky(pole, pozice=None):
    if pozice is None:
        return render_template('piskvorky.html', pole=pole)
    else:
        pozice = int(pozice)
        #pole = tah(pole, pozice, 'x') #naiportuje si tah

        pole = pole[:pozice] + 'X' + pole[pozice+1:]
        if 'XXX' not in pole:
            pole = tah_pocitace(pole, 'O')

        if 'XXX' in pole or 'OOO' in pole:
            return redirect(url_for('hello')) #view - jmenuje se stejne jako funkce hello

        return redirect(url_for('piskvorky', pole=pole))
