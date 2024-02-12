from flask import Flask, render_template, request

app = Flask(__name__, template_folder='capstone_project', static_url_path='/static')

sensor_data = {"humidity": "대기 중", "temperature": "대기 중", "dust": "대기 중", "warning": ""}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_sensor_data', methods=['GET'])
def send_sensor_data():
    global sensor_data
    humidity = request.args.get('humidity')
    temperature = request.args.get('temperature')
    dust = request.args.get('dust')

    # 여기에서 온도가 25도 이상이면 경고 메시지를 설정
    if float(temperature) >= 23:
        sensor_data["warning"] = "주의: 온도가 25도를 넘었습니다."

    sensor_data = {"humidity": humidity, "temperature": temperature, "dust": dust, "warning": sensor_data["warning"]}
    print(f"Received new sensor data - Humidity: {humidity}, Temperature: {temperature}, Dust: {dust}")
    return 'Sensor data received successfully!'

@app.route('/get_sensor_data', methods=['GET'])
def get_sensor_data():
    global sensor_data
    return {'sensorData': sensor_data}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
