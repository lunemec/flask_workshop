#!/bin/bash
nginx
uwsgi -s /tmp/uwsgi.sock --manage-script-name --mount /=workshop:app --master --workers 10 --uid www-data --gid www-data --plugin python3