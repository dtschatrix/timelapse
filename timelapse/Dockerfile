FROM python:3
WORKDIR /timelapse

RUN apt update && apt upgrade -y
ENV PYTHONUNBUFFERED = 1

RUN apt install -y build-essential python3-pip python3-dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "__main__.py" ]