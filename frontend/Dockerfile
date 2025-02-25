# syntax=docker/dockerfile:1
FROM node:16-alpine AS base
WORKDIR /src
RUN chown -R node:node /src && chmod -R 770 /src

# --- development for local ---
FROM base AS development
COPY ["package.json", "package-lock.json*", "./"]
# キャッシュディレクトリを指定
RUN \
  --mount=type=cache,target=/root/.npm \
  --mount=type=cache,target=/workspace/node_modules \
  npm install
COPY . .
EXPOSE 3001
ENTRYPOINT ["npm", "run", "start"]

# --- builder ---
FROM base AS builder
COPY --chown=node:node . .
USER node
RUN npm install
RUN npm run build

# --- Production Stage ---
FROM base AS production
LABEL org.label-schema.name="frontend-prod"
ENV NODE_ENV=production
COPY --chown=node:node --from=builder /src/build ./build
COPY --chown=node:node ./package*.json ./
RUN npm install -g serve
USER node
ENTRYPOINT ["serve", "-s", "./build"]
EXPOSE 3001