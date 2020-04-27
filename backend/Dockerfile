# use python container image
From python:3.6-stretch

# set the working directory of the image filesystem 
WORKDIR /backend

# copy current directory to the working directory 
ADD requirements.txt /backend

ADD . /backend

RUN ls

# Install the python dependencies on container
RUN pip install -r requirements.txt


# start the uWSGI
CMD ["python", "MonitorService.py"]
