FROM node:12.2.0-alpine

WORKDIR /frontend

ENV PATH /frontend/node_modules/.bin:$PATH
ENV VUE_APP_API_URL http://localhost:5000/api
COPY . .
RUN npm install

CMD ["npm", "run", "serve"]