FROM nginx:alpine

# Copy nginx config
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Copy React build
COPY mynotes/build /usr/share/nginx/html

