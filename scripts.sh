#!/bin/sh
python manage.py wait_for_db 
python manage.py migrate 
python manage.py test --noinput --failfast -v 0 &&
if [ $? -eq 0 ]; then 
python manage.py runserver 0.0.0.0:8000; 
else 
echo 'Tests failed, server not starting.'; 
exit 1; 
fi