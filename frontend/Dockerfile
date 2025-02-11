# syntax=docker/dockerfile:1
FROM node:16-alpine AS base
WORKDIR /src
RUN chown -R node:node /src && chmod -R 770 /src

# --- development for local ---
FROM base AS builder
COPY ["package.json", "package-lock.json*", "./"]
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3001
ENTRYPOINT ["npm", "run", "start"]

# --- Production Stage ---
FROM base AS production
LABEL org.label-schema.name="backend-prod"
ENV NODE_ENV=production
COPY --chown=node:node --from=builder /src/build ./build
COPY --chown=node:node ./package*.json ./
RUN npm install --only=production
USER node
ENTRYPOINT ["node", "./build/index.html"]
EXPOSE 3001