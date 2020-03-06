from flask import Flask,render_template,jsonify,url_for,session
import graficos
import getCSV 
# run
app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/')
def hello_world():
    #trae el archivo y lo guarda en session
    getCSV.getFile()
    return render_template('home.html')

@app.route('/cambiarGrafico')
def cambiarGrafico():
    #ejecuta el grafico y retorna el path    
    return jsonify(path=graficos.barrasSumadas())
    