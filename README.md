# certificate_blockchain
Using Ethereum Blockchain to digitalize certificate transactions

# Celery
Uses redis as a broker to pass message from django to celery. Check https://redis.io/download for installation of redis

To run
In a separate terminal run
		$ python manage.py runserver

In a separate terminal run 
		$ redis-server --port 8888

In a separate terminal run to create a celery worker to test whether this is working
		$ celery -A ethcert_blockchain worker --loglevel=info

To start worker and the beat NOTE: this is only suitable for development purposes
    $ celery -A ethcert_blockchain worker -l info -B

For deployment we will have to use daemonization

## Reference
https://medium.com/@yehandjoe/celery-4-periodic-task-in-django-9f6b5a8c21c7

