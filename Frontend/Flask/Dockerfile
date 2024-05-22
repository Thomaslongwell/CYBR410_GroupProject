FROM ubuntu
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install iputils-ping
RUN apt-get -y install whois

RUN apt -y install python3
RUN apt -y install python3-flask

RUN apt-get -y install python3-requests






RUN mkdir -p /templates
RUN mkdir -p /static

 
COPY /templates/index.html /templates
COPY /templates/address_search.html /templates
COPY /templates/address_output.html /templates
COPY /templates/weather_output.html /templates
COPY /templates/weather_search.html /templates
COPY /static . /static

COPY fServer.py .
EXPOSE 9001
CMD ["python3", "fServer.py"]
