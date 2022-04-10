# to take programming language you are using
FROM python:3.10.2
# creates directory in the container directory of docker
WORKDIR /app
#copies requirement.txt to
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


# to copy all files to docker
COPY . . 
# to run python file
CMD ["python3", "main.py"]


#all things above are instructions. To create docker disk(image) you have to write "docker build ." command in terminal 