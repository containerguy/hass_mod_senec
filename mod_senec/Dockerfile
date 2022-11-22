FROM python:alpine
MAINTAINER René Keller rene@familie-keller.info
ARG SENEC_HOST
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" > /etc/apk/repositories && echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories && apk update
RUN apk add chromium
RUN apk add chromium-chromedriver
RUN pip3 install -U selenium
WORKDIR /app
COPY ./trigger_senec.py /app/
COPY ./run.sh /
CMD [ "/run.sh" ]
