import flask
import mysql.connector as mysql

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Bienvenido a la página de la finca</h1>

<p>Por ahora solo puedes acceder a los datos desde: </p>
<p>/finca/all </p>'''


@app.route('/index/', methods=['GET'])
def index():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
   <h1>Welcome to FlaskBlog</h1>
</body>
</html>
'''


@app.route('/finca/all', methods=['GET'])
def acceso_datos():
    #Conexión a la BD
    db = mysql.connect(host="192.168.0.16", user="roger", passwd="1234",database="datosArduino")
    cursor = db.cursor()

    #Seleccionar elementos de la BD
    query = """SELECT * 
                FROM sensores2
                order by FechaActualizacion desc"""
    cursor.execute(query)
    resultados = cursor.fetchall()
    db.commit()

    #Cerrar cursor y DB
    cursor.close()
    db.close()
    datos_dict = {}
    for row in resultados:
        datos_dict[row[0]] = {'Fecha Actualización': row[1],
                              'Temperatura': row[2],
                              'Luminosidad': row[3],
                              }

    return datos_dict


@app.route('/finca/now', methods=['GET'])
def datos_actuales():
    #Conexión a la BD
    db = mysql.connect(host="192.168.0.16", user="roger", passwd="1234",database="datosArduino")
    cursor = db.cursor()

    #Seleccionar elementos de la BD
    query = """select *
                from sensores2
                where FechaActualizacion = (SELECT MAX(FechaActualizacion)
                                            from sensores2)
                order by FechaActualizacion desc
                """
    cursor.execute(query)
    resultados = cursor.fetchall()
    db.commit()

    #Cerrar cursor y DB
    cursor.close()
    db.close()
    datos_dict = {}
    for row in resultados:
        datos_dict[row[0]] = {'Fecha Actualización': row[1],
                              'Temperatura': row[2],
                              'Luminosidad': row[3],
                              }

    return datos_dict

app.run()


