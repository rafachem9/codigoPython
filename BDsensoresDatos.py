import mysql.connector as mysql
import matplotlib.pyplot as plt #para hacer gráficos

#Conexión a la BD
db= mysql.connect(host="192.168.1.25", user="roger", passwd="1234",database="datosArduino")
cursor = db.cursor()

#Seleccionar elementos de la BD
query= "SELECT * FROM sensores"
cursor.execute(query)
resultados = cursor.fetchall()
db.commit()

#Cerrar cursor y DB
cursor.close()
db.close()
print(resultados)

ejex=[]
ejetemp=[]
ejeluz=[]
for x in resultados:
    #Transformamos el tiempo para poder representarlo
    hora=int(x[1][:2])
    min=int(x[1][3:5])/60
    tiempo= hora + min
    ejex.append(tiempo)
    ejetemp.append(x[3])
    ejeluz.append(x[4])

#Hacer un gráfico con los valores de la BD
plt.plot(ejex, ejetemp, label="Temperatura")
#plt.plot(ejex, ejeluz, label="Luminosidad")
plt.ylim(20,30)
plt.legend()
plt.xlabel("Tiempo")
plt.ylabel("Temperatura (ºC)")
plt.title("Temperatura")
plt.show()
