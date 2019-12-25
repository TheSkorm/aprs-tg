FROM python:3.7-alpine

RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev openssl-dev 

WORKDIR /usr/src/app

# Install requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-m", "aprstg"]