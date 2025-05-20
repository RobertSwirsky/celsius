from flask import Flask, jsonify, request, render_template_string, current_app
from celsius import sensor
from  datetime import datetime, timezone
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from collections import deque



app = Flask(__name__)
@app.route('/')
def data():
    import w1thermsensor
    # Check if client wants JSON or HTML (default to JSON)
    data_list = (current_app.config['celsius']).get_sensor_list()
    
    # get deques for all the sensors
    sensor_dict = (current_app.config['logTemps']).sensor_dict


    if request.args.get('format') == 'html':
        # Render list as HTML unordered list
        html_content = "<ul>"
        for k in sensor_dict:
            newest = (sensor_dict[k])[-1]
            html_content = html_content + "<li>" + k + ", " +  newest[0] + ", " + newest[1] + "</li>"
        html_content = html_content + "</ul>"
        return render_template_string(html_content)
    else:
        # Return JSON response
        result = []
        for k in sensor_dict:
            newest = (sensor_dict[k])[-1]
            result.append((k, newest[0], newest[1]))
        return jsonify(result)

        
class logTemperatures:
    def __init__(self, sensor):
        self.sensor = sensor
        self.sensor_dict = {}           # empty dict to hold last "n" readings
    
    def job(self):
        data = self.sensor.get_sensor_list()
        now_utc_str = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

        for d in data:
            if not d.id in self.sensor_dict:
                self.sensor_dict[d.id] = deque(maxlen=100)
            self.sensor_dict[d.id].append( (now_utc_str, d.get_temperature() ))

if __name__ == '__main__':
    my_sensor = sensor([4])
    if my_sensor.check_kernel_modules():
        logTemps = logTemperatures(my_sensor)
        logTemps.job()
        app.config['celsius'] = my_sensor
        app.config['logTemps'] = logTemps
        scheduler = BackgroundScheduler()
        scheduler.add_job(func=logTemps.job, trigger='interval', minutes=1)
        scheduler.start()
        atexit.register(lambda: scheduler.shutdown())
        app.run(host='0.0.0.0',debug=True)


