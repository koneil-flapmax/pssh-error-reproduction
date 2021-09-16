FROM tiangolo/uvicorn-gunicorn:python3.7
WORKDIR /
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "gunicorn", "--log-level", "debug", "-b", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker",  "main:app"]
EXPOSE 8000

