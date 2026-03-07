# Use the official Nginx image as the base
# This image already has Nginx installed and configured to run
FROM nginx:latest

# Copy the front-end static files (HTML, CSS, JS) to the container
# We place them in /var/www/html/ so Nginx can serve them
COPY ./softy-pinko-front-end /var/www/html/softy-pinko-front-end

# Copy our custom Nginx configuration file
# This replaces the default config to use our specific settings (like port 9000)
COPY ./softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf
