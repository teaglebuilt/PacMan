FROM node:12.2.0-alpine

WORKDIR /frontend

ENV PATH /frontend/node_modules/.bin:$PATH

COPY package.json /app/package.json
RUN npm install

CMD ["npm", "run", "serve"]