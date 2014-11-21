from flask import Flask, request, abort
import subprocess
import os
from config import *
app = Flask(__name__)


@app.route('/vhost/', methods=['POST'])
def addProxyPass():
    apikey = request.headers.get('Authorization')
    if not Authenticated(apikey):
        return abort(401)
    port = request.args.get('port')
    host = request.args.get('host')
    client_id = request.args.get('clientid')
    vhost = request.args.get('vhost')
    generate_config(host, port, vhost, client_id)
    reload_nginx()
    return "added vhost"


@app.route('/vhost/<string:clientid>', methods=['DELETE'])
def deleteProxyPass(clientid):
    apikey = request.headers.get('Authorization')
    if not Authenticated(apikey):
        return abort(401)
    os.remove(clientid)
    return "%s removed" % clientid


def Authenticated(apikey):
    if (apikey == API_KEY):
        return True
    else:
        return False


def reload_nginx():
    command = ['/usr/sbin/service', 'nginx', 'reload']
    subprocess.call(command, shell=False)


def generate_config(host, port, vhost, filename):
    with open('%s/%s' % (SITE_ENABLED_DIR, filename), "w") as config:
        config.write("location /%s/ {" % vhost)
        config.write("\n    proxy_set_header Host $host;")
        config.write("\n    proxy_set_header X-Real-IP $remote_addr;")
        config.write("\n    proxy_pass http://%s:%s/; }" % (host, port))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
