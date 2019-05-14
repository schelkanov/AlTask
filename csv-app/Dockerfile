FROM alpine:3.7
EXPOSE 8080
VOLUME /usr/src/app/public
WORKDIR /usr/src/app
RUN apk add --no-cache \
        uwsgi-python \
        python \
        py-pip
COPY . /usr/src/app/
RUN pip install -r requirements.txt
CMD [ "uwsgi", "--socket", "0.0.0.0:8080", \
               "--protocol", "http", \
               "--plugins", "python", \
               "-w", "wsgi"]
