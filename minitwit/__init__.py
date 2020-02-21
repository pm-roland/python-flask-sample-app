from .minitwit import app
pip install --editable .
export FLASK_APP=minitwit.minitwit
export FLASK_DEBUG=1
flask initdb
flask run
