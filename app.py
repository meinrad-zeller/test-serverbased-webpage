from flask import Flask, request, render_template, Response
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
    try:
        with open('log.txt', 'a') as log_file:
            log_entry = f"[{timestamp}] Name: {name}, Message: {message}\n"
            log_file.write(log_entry)
            print(log_entry)  # Optional: Ausgabe in die Render-Logs
    except Exception as e:
        return f"Error while writing to log: {e}", 500
    
    return f"Daten gespeichert: Name - {name}, Message - {message}"

# Route zum Anzeigen der Logdatei
@app.route('/logs', methods=['GET'])
def view_logs():
    try:
        with open('log.txt', 'r') as log_file:
            logs = log_file.read()
        return Response(logs, mimetype='text/plain')
    except FileNotFoundError:
        return "Log file not found.", 404

# Main-Entry-Point
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
