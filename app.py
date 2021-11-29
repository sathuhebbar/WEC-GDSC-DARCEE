import flask
import os

app = flask.Flask(__name__)


@app.route("/")
def display_main_page():

    # When a '/' route is taken, we
    # display the home page, index.html

    return flask.render_template('edit.html')


@app.route('/submit', methods=['POST'])
def submit():

    # Invoked by the form on the main
    # page when the user clicks on 'Run'.

    frm = flask.request.form

    src = open('docker/vol/source.py', 'w')
    src.write(frm['source_code'])
    src.close()

    inp = open('docker/vol/input.txt', 'w')
    inp.write(frm['input'])
    inp.close()

    cmd = "docker run --rm --name darcee_executor -v $(pwd)/docker/vol:/mnt: darcee_executor_image bash /mnt/commands"

    os.system(cmd)

    out = open('docker/vol/output.txt', 'r')
    output = out.read()
    out.close()

    err = open('docker/vol/error.txt', 'r')
    errlog = err.read()
    err.close()

    return flask.render_template('result.html', output=output, error=errlog)
