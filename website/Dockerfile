FROM python
EXPOSE 5000
MAINTAINER Ankit Saksham "am97811n@pace.edu"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python","app.py"]
