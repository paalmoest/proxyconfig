Add proxy pass config to nginx with http.

Configurate your proxy passes with http POST call.

###Usage
    sudo python server.py

Create a new reverse proxy pass
        curl -XPOST -H "Authorization: <super-secret-key>"            
        http://localhost:5000?port=1337&host=localhost&filename=webapp/some-id&vhost=webapp

Now you can access your webapp at http://localhost/webapp/

###Config 

use some tool to generate an super secret api-key for your config.py.


### DISCLAIMER

For this POC the server.py needs to run as sudo. You probably what this running inside a trusted environment. 
