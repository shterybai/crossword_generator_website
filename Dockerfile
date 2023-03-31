FROM python:3.8-alpine

# Make a working directory in the image and set it as working dir.
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

ENV FLASK_APP=main.py

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]