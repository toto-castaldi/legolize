FROM python:3.9.5-buster

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV UPLOAD_FOLDER=/tmp/UPLOAD_FOLDER
ENV LOG_LEVEL=DEBUG
ENV HOST=0.0.0.0
ENV REDIS=redis://redis:6379

COPY ./src ./src
COPY ./*.csv ./src
COPY ./*.png ./src

COPY ./gunicorn.sh ./

EXPOSE 5000

ENTRYPOINT ["./start.sh"]

