from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    pass
# Rutas Seguras
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
@app.route("/login")
def login():
    pass

@app.route("/logout")
def logout():
    pass

@app.route("/register")
def register():
    pass










# Punto de Entrada
if __name__ == "__main__":
    app.run(debug=True)