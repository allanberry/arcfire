#!/bin/sh

# app_admin 
# Usage: ./app_admin { start | stop | restart }
# app_admin is a management script for gunicorn_django.
# It is designed to work on the WebFaction platform with minimal effort.
# The script requires gunicorn installed and enabled within your apps INSTALLED_APPS setting. 
# See http://gunicorn.org/ for instructions on gunicorn_django's use and installtion.

# Activate virtual environment. These 2 lines may be disabled/deleted if you do not use virtualenv.
WORKON_HOME="/home/allanberry/webapps/arcfire/env/py35/"
. $WORKON_HOME/bin/activate

# The server's IP adderess, this should be 127.0.0.1. 
ADDRESS='127.0.0.1'

# The port of your Django app. This will be located within the control panel in the application's details. 
SERVER_PORT='32406'

# Set PYTHON to '/usr/local/bin/python2.X' for a regular deployment and the path of the binary in the virtualenv if you are using one.
PYTHON="/home/allanberry/webapps/arcfire/env/py35/bin/python3.5"

# The path to gunicorn_django
GUNICORN="/home/allanberry/webapps/arcfire/env/py35/bin/gunicorn_django"

# The project location, settings.py, urls.py etc....
PROJECTLOC="/home/allanberry/webapps/arcfire/arcfire_proj/arcfire"

# The default args for gunicorn_django see http://gunicorn.org/configure.html#contents
DEFAULT_ARGS="--workers=3 --settings=core.settings.production"

# Do not edit below this line
BASE_CMD="gunicorn core.wsgi:application $DEFAULT_ARGS"
SERVER_PID="$PROJECTLOC/$SERVER1_PORT.pid"

start_server () {
  if [ -f $1 ]; then
    if [ "$(ps -p `cat $1` | wc -l)" -gt 1 ]; then
       echo "A server is already running on ${ADDRESS}:${2}"
       return
    fi
  fi
  cd $PROJECTLOC
  echo "starting ${ADDRESS}:${2}"
  $BASE_CMD --daemon --bind=$ADDRESS:$SERVER_PORT --pid=$1
}

stop_server (){
  if [ -f $1 ] && [ "$(ps -p `cat $1` | wc -l)" -gt 1 ]; then
    echo "stopping server ${ADDRESS}:${2}"
    kill -9 `cat $1`
    rm $1
  else 
    if [ -f $1 ]; then
      echo "server ${ADDRESS}:${2} not running"
    else
      echo "No pid file found for server ${ADDRESS}:${2}"
    fi
  fi
}

case "$1" in
'start')
  start_server $SERVER_PID $SERVER_PORT 
  ;;
'stop')
  stop_server $SERVER_PID $SERVER_PORT
  ;;
'restart')
  stop_server $SERVER_PID $SERVER_PORT
  sleep 2
  start_server $SERVER_PID $SERVER_PORT
  ;;
*)
  echo "Usage: $0 { start | stop | restart }"
  ;;
esac

exit 0