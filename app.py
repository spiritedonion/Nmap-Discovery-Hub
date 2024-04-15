from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

commonly_used_options = ["-sS", "-sC", "-sV", "-O", "-vv", "--min-rate=10000", "-p-", "-oA", "-sU", "-sA", "-Pn"]

# Define Nmap options
nmap_options = [
    "-iL",
    "-iR",
    "--exclude",
    "-sS",
    "-sT",
    "-sU",
    "-sA",
    "-sW",
    "-sM",
    "-sL",
    "-sn",
    "-Pn",
    "-PS",
    "-PA",
    "-PU",
    "-PR",
    "-n",
    "-p",
    "-F",
    "--top-ports",
    "-p-",
    "-p0-",
    "-p",
    "-sV",
    "--version-intensity",
    "--version-light",
    "--version-all",
    "-O",
    "--osscan-limit",
    "--osscan-guess",
    "--max-os-tries",
    "-T0",
    "-T1",
    "-T2",
    "-T3",
    "-T4",
    "-T5",
    "--host-timeout",
    "--min-rtt-timeout",
    "--min-hostgroup",
    "--min-parallelism",
    "--max-retries",
    "--min-rate",
    "--max-rate",
    "-sC",
    "--script",
    "--script-args",
    "-f",
    "-mtu",
    "-D",
    "-S",
    "-g",
    "--proxies",
    "--data-length",
    "-oN",
    "-oX",
    "-oG",
    "-oA",
    "-v",
    "-d",
    "--reason",
    "--open",
    "--packet-trace",
    "--iflist",
    "--resume",
    "-6",
    "-h"
]

@app.route('/')
def index():
    return render_template('index.html', options=nmap_options)

@app.route('/scan', methods=['POST'])
def scan():
    selected_options = request.form.getlist('option')
    targets = request.form['targets']
    command = ['nmap'] + selected_options + [targets]
    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        return render_template('result.html', result=result)
    except subprocess.CalledProcessError as e:
        return f"Error executing Nmap: {e.output}"

if __name__ == '__main__':
    app.run(debug=False)
