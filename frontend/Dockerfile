# syntax=docker/dockerfile:1

FROM node:12.18.1
WORKDIR /src
RUN chown -R node:node /src && chmod -R 770 /src
COPY ["package.json", "package-lock.json*", "./"]
RUN npm install
COPY . .
CMD ["npm", "run", "start"]
