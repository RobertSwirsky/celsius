from flask import Flask, jsonify, request, render_template_string, current_app
from celsius import sensor


app = Flask(__name__)
@app.route('/')
def data():
    # Check if client wants JSON or HTML (default to JSON)
    data_list = (current_app.config['celsius']).get_sensor_list()
    # XXX TODO: Put in try block to catch "SensorNotReady" error

    if request.args.get('format') == 'html':
        # Render list as HTML unordered list
        html_content = '<ul>' + ''.join(f'<li>{item.id},&nbsp;{item.get_temperature()}</li>' for item in data_list) + '</ul>'
        return render_template_string(html_content)
    else:
        # Return JSON response
        try:
            return jsonify([ (d.id, d.get_temperature()) for d in data_list ])
        except w1thermsensor.SensorNotReadyError:
            return jsonify([('error', 'SensorNotReady')])


if __name__ == '__main__':
    my_sensor = sensor([4])
    if my_sensor.check_kernel_modules():
        app.config['celsius'] = my_sensor
        app.run(host='0.0.0.0',debug=True)


