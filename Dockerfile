# start by pulling the python image
FROM python:3.8-alpine

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

ENV time_service_url="https://2vqpmoynvic3tmlaojbdqkrld40ytpod.lambda-url.us-east-1.on.aws/"
ENV time_service_url_docker="https://nzxjy4npdrcwhuvblxx4tkjlvq0racdx.lambda-url.us-east-1.on.aws/"

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]
