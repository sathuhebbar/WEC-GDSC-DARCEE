import flask
import subprocess
import json
import sys
import os

# Our app
app = flask.Flask(__name__)

# Load language data from config file
with open('lang-config.json', 'r') as file:
    langs = json.load(file)


@app.route("/")
def display_main_page():

    # When a '/' route is taken, we
    # display the home page, index.html

    # Render the edit.html page, pass the language data
    # for javascript to work on
    return flask.render_template('edit.html', langs=json.dumps(langs))


@app.route('/submit', methods=['POST'])
def submit():

    # Invoked by the form on the main
    # page when the user clicks on 'Run'

    frm = flask.request.form

    # Get source code, language and stdin
    # input from form
    ip, lang, src = frm['input'], frm['lang'], frm['source_code']

    # Write the source code
    with open('docker/temp/sourcecode', 'w') as sfile:
        sfile.write(src)

    # Write the commands corresponding to the language
    with open('docker/temp/commands', 'w') as cfile:
        cfile.write('cp /mnt/sourcecode .\n')
        for cmd in langs[lang]['commands']:
            cfile.write(cmd + '\n')

    # Our docker command
    cmd = ["docker", "run", "-i", "-v", os.getcwd() +"docker/temp:/mnt:", "--rm",
           "darcee_executor_image", "/bin/bash", "/mnt/commands"]

    # Call the command!!!!
    p = subprocess.run(cmd, input=ip, encoding=sys.getdefaultencoding(), stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

    return flask.render_template('result.html', output=p.stdout, error=p.stderr)
