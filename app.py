from flask import Flask, request, jsonify
import csv
from datetime import datetime

app = Flask(__name__)

LOG_FILE = "log.csv"

@app.route('/log', methods=['POST'])
def log_action():
    data = request.json

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    row = [
        data['userName'],
        date,
        time,
        data['buttonType'],
        data['postalCode'],
        data['city'],
        data['street'],
        data['houseNumber']
    ]

    if data['buttonType'] == 'Auftrag':
        row.extend([data.get('name', ''), data.get('phone', ''), data.get('email', '')])

    with open(LOG_FILE, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(row)

    return jsonify({"message": "Action logged successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
