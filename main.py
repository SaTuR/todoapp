from flask import Flask,render_template,session, redirect,url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "Saturnino"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tododb.sqlite"

db = SQLAlchemy(app)
# base de datos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    nombre = db.Column(db.Text, nullable=False)    

class Tareas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.Text, nullable=False)
    estado = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
 
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    if session:
        return render_template('index.html',session=session)
    else:
        return redirect(url_for('login'))


# Rutas Seguras
@app.route("/change_password")
def change_password():
    session.clear()
    return redirect(url_for('login'))

@app.route("/add")
def add_task():
    pass

@app.route("/update")
def update_task():
    pass

@app.route("/delete")
def delete_task():
    pass

#rutas No seguras 
@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # valida usuario y clave
        session['name'] = 'Nelson Sanchez'
        session['email'] = 'nelsonsanchezestrada@gmail.com'
        return redirect(url_for('index'))
    else:
        return render_template('login.html')


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route("/register")
def register():
    pass






# Punto de Entrada
if __name__ == "__main__":
    app.run(debug=True)