from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Renderiza la interfaz de nuestro Soroban físico
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)