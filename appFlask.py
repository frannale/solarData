from flask import Flask,render_template,jsonify,url_for,session,request
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
    #busca en el xls ,ejecuta el grafico y retorna el path
    fecha = request.args.get('fecha')
    datos = request.args.get('datos')
    grafico = request.args.get('grafico')
    resultado = getCSV.findFile(fecha,datos)

    return jsonify(path=graficos.barrasSumadas(resultado),res=fecha)
    