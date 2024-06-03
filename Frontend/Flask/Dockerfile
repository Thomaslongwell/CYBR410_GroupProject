FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

RUN apt-get update && apt-get -y upgrade

RUN apt-get -y install pip
RUN apt-get -y install iputils-ping
RUN apt-get -y install netbase
RUN apt-get -y install whois

RUN apt-get -y install python3

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install python3-flask

RUN pip install pymysql
RUN pip install flask-sqlalchemy


RUN apt-get -y install python3-requests






RUN mkdir -p /templates
RUN mkdir -p /static

 
COPY /templates /templates

COPY /static  /static

COPY fServer.py .
EXPOSE 9001

CMD ["python3", "fServer.py"]
