FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
RUN pip3 install ./en_core_web_sm-2.1.0.tar.gz
RUN python3 -m spacy download en_core_web_sm
CMD ["python", "app.py"]
