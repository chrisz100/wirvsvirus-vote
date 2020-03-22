FROM python:3-slim
WORKDIR /app
ADD requirements.txt .
RUN pip3 install -r requirements.txt
ADD . .
ENV SECRET client_secret.json
ENTRYPOINT [ "python3" ]
CMD [ "google_insert_item.py" ]