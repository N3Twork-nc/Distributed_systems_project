FROM node:14

EXPOSE 3000

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

CMD [ "node", "index.js" ]
