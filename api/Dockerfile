FROM python:3.9.5-buster

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV UPLOAD_FOLDER=UPLOAD_FOLDER
ENV LOG_LEVEL=DEBUG
ENV PATH_APPEND=/app/src

COPY ./*.png ./
COPY ./*.csv ./
COPY ./src ./src


EXPOSE 5000
CMD ["python",\
 "src/server.py"\
]
