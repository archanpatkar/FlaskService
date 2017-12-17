FROM python:3.6-slim

WORKDIR /Service

ADD . /Service

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV NAME World

CMD [ "python","Service.py" ]