FROM python:3.6.3
MAINTAINER Ankit Saksham "am97811n@pace.edu"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
EXPOSE 5000
