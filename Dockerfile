# FROM python:3.9-windowsservercore-1809

FROM python:3.9
USER root

RUN pip install --upgrade pip
RUN pip install pycryptodome
RUN pip install pyinstaller

WORKDIR /app
COPY app /app
COPY start.sh /

RUN chmod 755 /start.sh

CMD ["/start.sh"]
