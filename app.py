from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target = request.form.get('target')
    options = ""

    # if 'il' in request.form:
    #     options += " -iL"
    # if 'ir' in request.form:
    #     options += " -iR"
    # if 'exclude' in request.form:
    #     options += " --exclude"
       # Commanly Used
    if 'ss' in request.form:
        options += " -sS"
    if 'sc' in request.form:
        options += " -sC"
    if 'sv' in request.form:
        options += " -sV"
    if 'p' in request.form:
        options += " -p-"
    if 'vv' in request.form:
        options += " -vv"
    if 'min-rate' in request.form:
        options += " --min-rate=10000"
    
    
    # Nmap Scan Techniques
    if 'ss' in request.form:
        options += " -sS"
    if 'st' in request.form:
        options += " -sT"
    if 'su' in request.form:
        options += " -sU"
    if 'sa' in request.form:
        options += " -sA"
    if 'sw' in request.form:
        options += " -sW"
    if 'sm' in request.form:
        options += " -sM"
    
    # Host Discovery
    if 'sl' in request.form:
        options += " -sL"
    if 'sn' in request.form:
        options += " -sn"
    if 'pn' in request.form:
        options += " -Pn"
    if 'ps' in request.form:
        options += " -PS"
    if 'pa' in request.form:
        options += " -PA"
    if 'pu' in request.form:
        options += " -PU"
    if 'pr' in request.form:
        options += " -PR"
    if 'n' in request.form:
        options += " -n"
    
    # Port Specification
    if 'p' in request.form:
        options += " -p"
    if 'pr' in request.form:
        options += " -p-"
    if 'pu' in request.form:
        options += " -p U:"
    if 'pt' in request.form:
        options += " -p T:"
    
    # Service and Version Detection
    if 'sv' in request.form:
        options += " -sV"
    if 'vi' in request.form:
        options += " --version-intensity"
    if 'vl' in request.form:
        options += " --version-light"
    if 'va' in request.form:
        options += " --version-all"
    
    # OS Detection
    if 'o' in request.form:
        options += " -O"
    if 'ossl' in request.form:
        options += " --osscan-limit"
    if 'ossg' in request.form:
        options += " --osscan-guess"
    if 'maxos' in request.form:
        options += " --max-os-tries"
    
    # Timing and Performance
    if 't' in request.form:
        options += " -T"
    if 'ht' in request.form:
        options += " --host-timeout"
    if 'rtt' in request.form:
        options += " --min-rtt-timeout"
    if 'mh' in request.form:
        options += " --min-hostgroup"
    if 'mp' in request.form:
        options += " --min-parallelism"
    if 'mr' in request.form:
        options += " --min-rate"
    if 'maxr' in request.form:
        options += " --max-rate"
    
    # NSE Scripts
    if 'sc' in request.form:
        options += " -sC"
    if 'script' in request.form:
        options += " --script"
    if 'scriptargs' in request.form:
        options += " --script-args"
    
    # Firewall / IDS Evasion and Spoofing
    if 'f' in request.form:
        options += " -f"
    if 'mtu' in request.form:
        options += " --mtu"
    if 'd' in request.form:
        options += " -D"
    if 's' in request.form:
        options += " -S"
    if 'g' in request.form:
        options += " -g"
    if 'proxies' in request.form:
        options += " --proxies"
    if 'datalength' in request.form:
        options += " --data-length"
    
    # Output
    if 'on' in request.form:
        options += " -oN"
    if 'ox' in request.form:
        options += " -oX"
    if 'ogrep' in request.form:
        options += " -oG"
    if 'oa' in request.form:
        options += " -oA"
    if 'v' in request.form:
        options += " -v"
    if 'd' in request.form:
        options += " -d"
    if 'reason' in request.form:
        options += " --reason"
    if 'open' in request.form:
        options += " --open"
    if 'packet-trace' in request.form:
        options += " --packet-trace"
    if 'iflist' in request.form:
        options += " --iflist"
    if 'resume' in request.form:
        options += " --resume"
    
    cmd = f"nmap {options} {target}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    return render_template('scan_result.html', result=result.stdout)

if __name__ == '__main__':
    app.run(debug=True)
