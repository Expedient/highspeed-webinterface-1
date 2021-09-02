# highspeed-webinterface

install flask "pip install flask"

download and unzip highspeed-webinterface

run the app "python app.py"

This should start a webserver on you local system on port 5000

connect to the web app http://localhost:5000

<em><strong>TURN OFF DEBUGGING</em></strong> in app.py Set "debug=True" to FALSE before you deploy to production.

TODO:
<ul>
  <li>Docker/Container</li>
  <li>load balance</li>
  <li>Nginx deployment/ncbot</li>
</ul>


<h1>uWSGI Deployment Command</h1>
uwsgi --http :9090 -w app:app
