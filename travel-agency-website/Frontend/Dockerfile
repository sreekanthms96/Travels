FROM nginx:alpine

# Copy custom nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy frontend files
COPY ./src /usr/share/nginx/html/pages

EXPOSE 80
