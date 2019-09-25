FROM python:3.7.0
RUN mkdir /steel
COPY /requirements.txt /steel/requirements.txt
RUN cd /steel && pip install -r requirements.txt
