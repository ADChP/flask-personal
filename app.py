'''
Aplicativo 'Maqueta'
Hecho por Andrés David Chavarría-Palma
2023
'''

from flask import Flask, render_template, redirect, url_for, request, session, flash

# create the application object
app = Flask(__name__)

# Evita que al darle al botón de regresar se vuelva a ver la sesión abierta.
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response

# config
app.secret_key = 'my precious'

# route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    if 'logged_in' in session:
        return redirect(url_for('inicio'))
    else:
        error = None
        if request.method == 'POST':
            if request.form['usuario'] != 'admin' or request.form['contrasena'] != 'admin':
                error = 'Credenciales inválidas. Por favor intente de nuevo.'
            else:
                session['logged_in'] = True
                flash('Haz iniciado sesión. ¡Bienvenido!')
                return redirect(url_for('inicio'))
        return render_template('login.html', error=error)
    
# use decorators to link the function to a url
@app.route('/inicio')
def inicio():
    if 'logged_in' in session:
        return render_template('index.html')  # render a template
    else:
        return redirect(url_for('login'))
    # return "Hello, World!"  # return a string

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Haz cerrado sesión. ¡Hasta la próxima!')
    return redirect(url_for('login'))


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)