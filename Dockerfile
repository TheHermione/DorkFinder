FROM python:3.11-slim

WORKDIR /app

COPY dorkfinder.py url_list.py requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python", "./dorkfinder.py" ]
CMD [ "-h" ]
