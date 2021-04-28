# Djfans

![Image](/images/skills.png)


## Personal project for Onlyfans clone

I created a simple onlyfans site using Django. During the deployment process, it was containerized through Docker. I linked the NGINX server and Django application server through Docker Compose. I created AWS resources using Terraform. Build automation was done through the linkage between Docker Hub and GitHub.
I plan to automate deployment by running Jenkins containers on the server.

---

## [Demopage Link](https://taeheejo.link)
- ID : tester
- PW : tester

## Test command

1. git clone https://github.com/jojo-tey/Django_fans.git
2. cd Django_fans/djfans
3. Disable product part in settings.py 
```
########################################
# Disable this part for local running

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.environ['DEBUG']
....
....
....
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
########################################
```
4. python manage.py makemigrations --settings=djfans.local
5. python manage.py migrate --settings=djfans.local
6. python manage.py runserver --settings=djfans.local


## Focused point

### Development

- Subscription & Post 
Configured to update the news feed only as subscribed users post

- Direct Message 
User can message to subscribed user

- Notification 
Notify users when new subscriptions occur

- Static & Media 
Static file and media file management using S3 bucket as a backend 


### Deployment

- Webserver 
Integration of nginx web server and Django application through gunicorn

- Database : AWS RDS
Minimize database design and management resources using AWS RDS

- Backend – S3
Integrated management of staticfile and mediafile through S3 bucket as backend

- Dockerize : Build automation
Packaging the app in container, build automation by linking github and docker hub


### Server management

![Image](/images/diagram.png)

- Secret value management
By setting the environment variable reference in the container, it is possible to manage secret value management on the server side at once. 

- VPC and Security group
Secure data storage by separating the database and the S3 bucket from the EC2 instance and placing it in a different security group.

- Infrastructure as code
Resource management through Terraform makes it easy to increase/decrease, version control, and reuse servers.

- CI/CD automation (Working on it)
Stage-by-stage setup through the pipeline.
Set to automatically build and deploy at the same time as commit.


### Screenshot

![Image](/images/index.png)
![Image](/images/profile.png)
![Image](/images/notification.png)
![Image](/images/subscription.png)
![Image](/images/followinglist.png)
![Image](/images/fanlist.png)
![Image](/images/chat.png)