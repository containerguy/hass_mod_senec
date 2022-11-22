FROM python:3.10
MAINTAINER René Keller rene@familie-keller.info
ARG SENEC_HOST
RUN wget -nc https://dl-ssl.google.com/linux/linux_signing_key.pub
RUN cat linux_signing_key.pub | gpg --dearmor | tee /etc/apt/trusted.gpg.d/linux_signing_key.gpg  >/dev/null
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/chrome.list'
RUN apt update && apt install google-chrome-stable -y
ADD requirements.txt /
RUN pip install --user -r requirements.txt
WORKDIR /app
COPY ./install_webdriver.py /app/
COPY ./trigger_senec.py /app/
RUN chmod a+x *.py
RUN "./install_webdriver.py"
CMD ["python", "/app/trigger_senec.py"]
