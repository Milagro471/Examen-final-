from flask import Flask, jsonify, request
from model import User
from controller import *

app = Flask(__name__)

#Entregar Datos JSON (Get:Obtener Datos, Post:Guardar Datos, Put: Actualizar, Delete: Borrar)


'''@app.route('/User', methods=['GET', 'POST'])
def login(self,User):
    
    try:

        if request.method == "POST":
            attempted_username = request.form['User']
            attempted_password = request.form['Pass']
            
            d = {}
            with open('datos.json', 'r') as outfile:  
                json.load(d, outfile)
                
                d['User']=attempted_username
                d['Pass']=attempted_password

            if request.form['User'] == d['User'] and request.form['Pass'] == d['Pass']:
            #return 'SUCCESSFULLY LOGGEDIN'
                    #error = 'Invalid Credentials. Please try again.'
                return jsonify({"SUCCESSFULLY LOGGEDIN"})
            else:
                return 'invalid '
            return jsonify({"'Invalid Credentials. Please try again.'"})'''

@app.route('/User')
def getList():
    return jsonify({"Lista de Cosas por Hacer": User})


    #Solo uno
@app.route('/User/<string:tarea>')
def getLista(tarea):
    tareaFound = [ListTareas for ListTareas in User if ListTareas['Tarea'] == tarea] #Recorre la lista
    if(len(tareaFound) > 0): #validacion para que no se caiga
        return jsonify({"ListTarea": tareaFound[0]})
    return jsonify({"Message": "Tarea No encontrada..."})

    #(app insomnia->Permite enviar y mostrar Datos a nuestras Rest API)

    #Crear y agregar Datos
@app.route('/User', methods=['POST'])
def addTarea():
    new_tarea = {
        "Tarea": request.json['Tarea'],
        "Dia": request.json['Dia'],
        "Hora": request.json['Hora']
        }
    User.append(new_tarea)
    return jsonify({"Message": "Tarea Agregada...!!!", "Lista de Cosas por Hacer": User})

    #Actualizar Datos
@app.route('/User/<string:tarea>', methods=['PUT'])
def editTarea(tarea):
    tareaFound = [ListTareas for ListTareas in User if ListTareas['Tarea'] == tarea]    
    if(len(tareaFound) > 0):
        tareaFound[0]['Tarea'] = request.json['Tarea']
        tareaFound[0]['Dia'] = request.json['Dia']
        tareaFound[0]['Hora'] = request.json['Hora']
        return jsonify({"Message": "Tarea Actualizada","Lista de Tareas": tareaFound[0]})
    return jsonify({"Message": "Tarea No encontrada..."})

    #Eliminar Datos
@app.route('/User/<string:tarea>', methods=['DELETE'])
def deleteTarea(tarea):
    tareaFound = [ListTareas for ListTareas in User if ListTareas['Tarea'] == tarea]    
    if(len(tareaFound) > 0):
        User.remove(tareaFound[0])
        return jsonify({"Message": "Tarea Eliminada...","Lista de Tareas": User })
    return jsonify({"Message": "Tarea No encontrada..."})

if __name__ == '__main__':
    app.run(debug=True, port=4000)