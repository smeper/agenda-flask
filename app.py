from flask import Flask, render_template, request, url_for, flash
from flask_mysqldb import MySQL
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'flaskcontacts'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
mysql = MySQL(app)

#almacenar contenido de la session
app.secret_key = 'mysecretkey'

@app.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute("select * from contactos")
    datos = cur.fetchall()
    return render_template('index.html', contactos = datos)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        name = request.form['nombre']
        phone = request.form['telefono']
        email = request.form['mail']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contactos (nombre, telefono, email) VALUES (%s,%s,%s)", (name, phone, email))
        mysql.connection.commit()
        return redirect(url_for('index'))

@app.route('/editar/<id>', methods = ['POST'])
def editar(id):
    if request.method == 'POST':
        name = request.form['nombre']
        phone = request.form['telefono']
        email = request.form['mail']
        cur = mysql.connection.cursor()
        cur.execute("update contactos set nombre = %s, telefono = %s, email = %s where id= %s", (name, phone, email, id))
        mysql.connection.commit()
        flash("Modificacion realizada correctamente")
        return redirect(url_for('index'))


@app.route('/update/<string:id>')
def update(id):
    cur = mysql.connection.cursor()
    cur.execute("select * from contactos where id = " + id)
    datos = cur.fetchall()
    return render_template("editar.html", contacto = datos[0])


@app.route('/delete/<string:id>')
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("delete from contactos where id=" + id)
    mysql.connection.commit()
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug = True)