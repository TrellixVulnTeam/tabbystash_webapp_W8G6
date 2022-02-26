#!/bin/bash
hostnameOutput=$(hostname -i)
#echo "${hostnameOutput}  api.tabbystash.com" >> /etc/hosts
#exec gunicorn -b $(hostname -i):5000 "app:create_app()"
#exec gunicorn -b $(hostname -i):5000 "app:create_app()"
#exec gunicorn -b 0.0.0.0:5000 "app:create_app()"
exec gunicorn -b 0.0.0.0:5000 --access-logfile - --error-logfile - "app:create_app()"