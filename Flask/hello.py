from flask import Flask, render_template

# Iniciar la aplicación

app = Flask(__name__)

#Definiendo Root path
@app.route('/')
def hello_world():
    return render_template('index.html')



# Ets línea se agrega si se ejecuta el archivo
# directamente con el comando python
#app.run()

