# test backend for docker
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ../../backend/backend.py ./

ENTRYPOINT [ "python", "./backend.py"]
