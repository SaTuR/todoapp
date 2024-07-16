from flask import Flask,render_template,session, redirect,url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "Saturnino"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tododb.sqlite"

db = SQLAlchemy(app)
# base de datos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    nombre = db.Column(db.Text, nullable=False)    

class Tareas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.Text, nullable=False)
    estado = db.Column(db.Text, nullable=False,default='Pediente')
    email = db.Column(db.Text, nullable=False)
 
with app.app_context():
    db.create_all()
    # user = Usuario(
    #         email='jscordovaa@gmail.com',
    #         password='12345',nombre='Jose Cordova')
    # db.session.add(user)
    # db.session.commit()


@app.route("/",methods=['GET','POST'])
def index():
    if session:
        if request.method=='POST':
            name = request.form.get('name')
            if name:
                obj = Tareas(nombre=name,email=session['email'] )
                db.session.add(obj)
                db.session.commit()
                lista_tareas = Tareas.query.all()
            return render_template('index.html',lista_tareas = lista_tareas)

        else:
            lista_tareas = Tareas.query.all()
            return render_template('index.html',session=session,lista_tareas = lista_tareas)
            # return render_template('index.html',lista_tareas = lista_tareas)
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

@app.route("/update/<id>")
def update_task(id):
    obj = Tareas.query.filter_by(id = id).first()
    if obj.estado == "Hecho":
        obj.estado = "Pendiente"
    else:
        obj.estado = "Hecho"
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/delete/<id>")
def delete_task(id):
    obj= Tareas.query.filter_by(id=id).first()
    db.session.delete(obj)
    db.session.commit()
    return redirect(url_for('index'))

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
    obj = Usuario(email='jscordovaa@gmail.com',password="12345",nombre='Jose Cordova')
    db.session.add(obj)
    db.session.commit()
    return redirect(url_for('login'))






# Punto de Entrada
if __name__ == "__main__":
    app.run(debug=True)