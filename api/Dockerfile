FROM ubuntu:latest
EXPOSE 1337
WORKDIR /api
RUN apt update && apt upgrade -y

RUN apt install -y build-essential python3-pip python3-dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "python3", "__main__.py" ]