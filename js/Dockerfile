FROM node:20-alpine

ENV NODE_ENV=production

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm ci

COPY . .

CMD ["node", "index.js"]