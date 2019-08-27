FROM python:2.7
RUN pip install -U Flask==0.10.1
RUN pip install mysql-connector
COPY app.py /
WORKDIR /
CMD ["python","app.py"]
