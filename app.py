from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'clave_secreta' 

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'dbcentromedico'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
       
        rfc = request.form.get('rfc')
        nombre = request.form.get('nombre')
        cedula = request.form.get('cedula')
        correo = request.form.get('correo')
        contraseña = request.form.get('contraseña')
        rol = request.form.get('rol')

        
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO tbmedicos (rfc, nombre, cedula, correo, contraseña, rol) VALUES (%s, %s, %s, %s, %s, %s)",
            (rfc, nombre, cedula, correo, contraseña, rol)
        )
        mysql.connection.commit()
        cursor.close()

        flash('Registro exitoso. Los datos han sido guardados correctamente.', 'success')


        return redirect(url_for('registro'))

    return render_template('registro.html')

@app.route('/consulta')
def consulta():
    return 'Página de consulta (por implementar)'

@app.route('/actualizar')
def actualizar():
    return 'Página de actualización (por implementar)'

@app.route('/eliminar')
def eliminar():
    return 'Página de eliminación (por implementar)'

@app.errorhandler(404)
def paginano(e):
    return 'PÁGINA NO ENCONTRADA', 404

if __name__ == '__main__':
    app.run(port=3000, debug=True)
