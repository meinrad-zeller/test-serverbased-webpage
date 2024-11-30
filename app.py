from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

# Route für die Startseite
@app.route('/')
def index():
    return render_template('index.html')

# Route zum Verarbeiten der Eingaben
@app.route('/submit', methods=['POST'])
def submit():
    # Daten aus dem Formular erhalten
    name = request.form.get('name')
    message = request.form.get('message')
    
    # Zeitstempel hinzufügen
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Daten in die Logdatei schreiben
    with open('log.txt', 'a') as log_file:
        log_file.write(f"[{timestamp}] Name: {name}, Message: {message}\n")
    
    return f"Daten gespeichert: Name - {name}, Message - {message}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
