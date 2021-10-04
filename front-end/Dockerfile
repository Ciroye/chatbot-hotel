FROM node:alpine AS app-build
WORKDIR /app
COPY . .
RUN npm ci && npm run build

FROM nginx:1.16.0-alpine
COPY --from=app-build /app/build /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]