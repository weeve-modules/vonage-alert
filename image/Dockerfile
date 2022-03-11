FROM python:3.8-slim
COPY . /app
WORKDIR /app
RUN pip install -r image/requirements.txt
SHELL ["/bin/bash", "-c"]
COPY ./image/entrypoint.sh /entrypoint.sh
RUN ["chmod", "+x", "/entrypoint.sh"]
ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 80
