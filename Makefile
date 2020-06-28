.PHONY: prepare run test clean

install-requirements:
	apt-get install -y python3.8 python3-pip python3.8-venv;

# https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
install-mongo-db:
	sudo apt-get update; \
	sudo apt-get install gnupg; \
	wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -; \
	echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list; \
	sudo apt-get update;\
	sudo apt-get install -y mongodb-org; \
	echo "mongodb-org hold" | sudo dpkg --set-selections; \
	echo "mongodb-org-server hold" | sudo dpkg --set-selections; \
	echo "mongodb-org-shell hold" | sudo dpkg --set-selections; \
	echo "mongodb-org-mongos hold" | sudo dpkg --set-selections; \
	echo "mongodb-org-tools hold" | sudo dpkg --set-selections

start-mongo-db:
	sudo systemctl start mongod

prepare:
	python3.8 -m venv venv; \
	. venv/bin/activate; \
	pip install -r requirements.txt;

run:
	. venv/bin/activate; \
	export PYTHONPATH=$PYTHONPATH:$(pwd); \
	python3.8 server.py --process=1 --log_level=DEBUG

test:
	. venv/bin/activate; \
    python -m unittest discover -s test -p test*.py;

clean: 
	py3clean .

get-minio:
	docker pull minio/minio

run-minio:
	docker run -p 9000:9000 minio/minio server /data