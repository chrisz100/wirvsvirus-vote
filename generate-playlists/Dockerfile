FROM python:3-slim
WORKDIR /app
ADD requirements.txt .
RUN pip3 install -r requirements.txt
ADD . .
ENV SECRET=file/client_secret.json VIDEO_MAPPING=file/videos.csv OUTPUT_FILE=file/playlists_out.json
ENTRYPOINT [ "python3" ]
CMD [ "shuffle.py" ]