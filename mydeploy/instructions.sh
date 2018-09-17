cd mydeploy/myapp
virtualenv -p /usr/bin/python2.7 ./venv; wait;
source ./venv/bin/activate
python setup.py develop

# ./venv/bin/python __main__.py
