import flask
import PortScanner
import webbrowser

url = ('http://localhost:5000/')
app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/button_press', methods=['POST'])
def button_press():
    if 'scan' in flask.request.form:
        # Button was pressed
        PortScanner.scan_ports(str(flask.request.form['ip_start']), str(flask.request.form['ip_end']), int(flask.request.form['port_start']), int(flask.request.form['port_end']), 'output.txt')
        with open('output.txt', 'r') as file:
            data = file.read()
            return data

if __name__ == '__main__':
    webbrowser.open(url)
    app.run(debug=True)
