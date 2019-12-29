
<div align="center">
<img src="https://github.com/teaglebuilt/PacMan/blob/master/static/pacman.png" width="400" style="margin-bottom: 0;">
  <p style="margin-top: 1em; margin-bottom: 1em; font-size: large;">Swagger & Load Testing in One</p>
    <img src="https://github.com/teaglebuilt/PacMan/workflows/Docker%20Test/badge.svg">
    <img src="https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fteaglebuilt%2FPacMan%2F">
  <div>
    <img src="https://github.com/teaglebuilt/PacMan/blob/master/static/flask.png" width="300">
    <img src="https://github.com/teaglebuilt/PacMan/blob/master/static/vue.png" width="200">
  </div>
</div>





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
