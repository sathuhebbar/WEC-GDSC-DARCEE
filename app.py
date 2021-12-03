import flask
import subprocess
import json
import sys
import pathlib

# SOME CONSTANTS
TIMEOUT = 5

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

    # Create the docker image
    create_cmd = ["docker", "create", "-i", "--memory=256M", "--network", "none",
                  "darcee_executor_image", "/bin/bash", "commands"]
    cprocess = subprocess.run(create_cmd, stdout=subprocess.PIPE,
                              encoding=sys.getdefaultencoding())

    # We don't know the id of the container created
    # The create command would have printed that to stdout
    # The last character is a newline
    cid = cprocess.stdout[:-1]

    # Write the source code
    with open('temp/' + cid + 'sourcecode', 'w') as sfile:
        sfile.write(src)

    # Write the commands corresponding to the language
    with open('temp/' + cid + 'commands', 'w') as cfile:
        for cmd in langs[lang]['commands']:
            cfile.write(cmd + '\n')

    # To prevent conflict, the source and commands files
    # are prefixed with the container id

    # Copying the source file and the set of commands
    # to the home folder of dummy
    subprocess.run(["docker", "cp", "temp/"+cid +
                   "sourcecode", cid + ":/home/dummy/sourcecode"])
    subprocess.run(["docker", "cp", 'temp/' + cid +
                   'commands', cid + ":/home/dummy/commands"])

    # Clean-up the files
    pathlib.Path('temp/' + cid + 'sourcecode').unlink()
    pathlib.Path('temp/' + cid + 'commands').unlink()

    # The key command
    start_cmd = ["docker", "start", "-i", cid]

    out, err = '', ''

    # Start running the container!
    try:
        p = subprocess.run(start_cmd, input=ip, encoding=sys.getdefaultencoding(), stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, timeout=TIMEOUT)
        out, err = p.stdout, p.stderr

    except subprocess.TimeoutExpired:
        err = 'TIME LIMIT EXCEEDED'

    # Delete the container
    subprocess.run(["docker", "stop", cid])
    subprocess.run(["docker", "container", "rm", cid])

    return flask.render_template('result.html', output=out, error=err)
