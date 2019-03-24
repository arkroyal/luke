# test backend for docker
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt \
    && apt-get update && apt-get install -y --no-install-recommends \
		git \
	&& rm -rf /var/lib/apt/lists/* \
    && git clone https://github.com/arkroyal/luke.git \
    && mv ./luke/backend/backend.py ./ \
    && rm -rf ./luke

ENTRYPOINT [ "python", "./backend.py"]
EXPOSE 8888/tcp