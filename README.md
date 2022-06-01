## Docker on ec2

Pushed the flask app image to Amazon ECR repository and pull it in ec2.

Configured ports, installed docker and then run it.

http://ec2-100-26-135-0.compute-1.amazonaws.com/


<u>*Sample request*</u>

`curl --location --request GET 'http://ec2-100-26-135-0.compute-1.amazonaws.com'`

`http://ec2-100-26-135-0.compute-1.amazonaws.com`


##### Notes

`docker image build -t working_hours_service .`

`aws ecr create-repository --repository-name working_hours_service --region us-east-1`

`docker tag working_hours_service 468601951624.dkr.ecr.us-east-1.amazonaws.com/working_hours_service`

`docker push 468601951624.dkr.ecr.us-east-1.amazonaws.com/working_hours_service`

`docker run -p 80:80 -d 468601951624.dkr.ecr.us-east-1.amazonaws.com/working_hours_service`
