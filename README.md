# django-demo-app
django small app using rest 

## Step wise instruction for running this demo app
Here assumed that docker, docker-compose and git is installed<br>

To install Docker: https://www.docker.com <br>
To install Docker-Compose: https://docs.docker.com/compose/install/ <br>

### step1: Clone the repo
$ git clone https://github.com/KrishnaSindhur/django-demo-app <br>

### step2: get inside the cloned repo 
$ cd django-demo-app <br>

### step3: Run for migrate
$ docker-compose run web python src/manage.py migrate <br>
optional to see the docker build this should have taken place in previous step<br>
$ docker-compose build

### step4: setup database for app and also load inital data
$ docker-compose run web python src/manage.py makemigrations <br>

$ docker-compose run web python src/manage.py migrate <br>

### step5: Now start a webserver
$ docker-compose up

### API to check:
for data in db:<br>
http://localhost:8080/one <br>
Response: {"key": "one","value": 1} <br>

for data not in db:<br>
http://localhost:8080/ten <br>
Response: {"key":"","value": null} <br>







