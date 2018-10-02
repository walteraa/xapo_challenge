FROM python:3.5.6-jessie

# Create workdir directory
RUN mkdir /app
WORKDIR /app

# Copy the pip dependency file to the container 
COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt 

COPY src/ /app/

EXPOSE 9000
ENTRYPOINT [ "python"]
CMD ["app.py"]
