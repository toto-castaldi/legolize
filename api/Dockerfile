FROM python:3.7-alpine

WORKDIR /app
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Start app
EXPOSE 5000
CMD ["uwsgi",\
 "--lazy",\
 "--http", ":5000",\
 "-w", "src.server",\
 "--processes", "4",\
 "--threads", "16",\
 "--stats", ":5001"\
]
