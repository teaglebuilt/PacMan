
<div class="text-center">
  <h1>PAC MAN</h1>
  <p>Integrating Vue & Flask</p>
</div>

![Flask](https://github.com/teaglebuilt/PacMan/blob/master/static/flask.jpg){ height="36px" width="36px" }
![Vue](https://github.com/teaglebuilt/PacMan/blob/master/static/vue.png){ height="36px" width="36px" }

![Github CI](https://github.com/teaglebuilt/PacMan/workflows/Docker%20Test/badge.svg)
![Tweet](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fteaglebuilt%2FPacMan%2F)


## Dependencies

* Python: 3.6.6 or greater
* Vue.js: 2.5.2
* vue-router: 3.0.1
* axios: 0.16.2


https://petstore.swagger.io/v2/swagger.json

## Build Setup

####  With Docker

```
docker-compose up -d

```

####  Local


``` bash
# install front-end
cd frontend
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production/Flask with minification
npm run build


# install back-end
cd ../backend
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

# serve back-end at localhost:5000
FLASK_APP=run.py flask run
```
