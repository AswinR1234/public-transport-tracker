from flask import Flask, render_template, request, jsonify
import sqlite3
from eta import calculate_eta

app = Flask(__name__)

# Get latest location
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.json
    
    conn = sqlite3.connect('bus.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO location VALUES (?, ?, ?, ?)",
                   (data['bus_id'], data['lat'], data['lon'], data['speed']))
    
    conn.commit()
    conn.close()
    
    return jsonify({"status": "updated"})

@app.route('/get_location')
def get_location():
    conn = sqlite3.connect('bus.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM location ORDER BY rowid DESC LIMIT 1")
    data = cursor.fetchone()
    
    conn.close()
    
    return jsonify({
        "bus_id": data[0],
        "lat": data[1],
        "lon": data[2],
        "speed": data[3]
    })

@app.route('/get_eta', methods=['POST'])
def get_eta_route():
    data = request.json
    eta = calculate_eta(data['distance'], data['speed'])
    return jsonify({"ETA": eta})

if __name__ == '__main__':
    app.run(debug=True)
