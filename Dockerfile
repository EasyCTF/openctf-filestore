FROM nginx

RUN apt-get update
RUN apt-get install -y python python-dev python-pip curl
RUN mkdir -p /usr/share/nginx/html/static
RUN touch /usr/share/nginx/html/static/index.html
COPY default.conf /etc/nginx/conf.d/default.conf

RUN mkdir /app
COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 80
EXPOSE 8000
RUN service nginx start