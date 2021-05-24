FROM nginx:1.17.5-alpine

COPY nginx.conf /etc/nginx/nginx.conf
COPY src /data/www

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]