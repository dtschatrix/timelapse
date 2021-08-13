FROM python:3
WORKDIR /timelapse

RUN apt update && apt upgrade -y
ENV PYTHONUNBUFFERED = 1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt install -y build-essential python3-pip python3-dev ffmpeg

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "__main__.py" ]