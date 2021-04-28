# Djfans

- Personal project for Onlyfans clone

### Used skill
- Django
- Docker-compose
- Terraform 
- Jenkins



### Test

git clone https://github.com/jojo-tey/Django_fans.git
cd Django_fans/djfans
python manage.py makemigrations --settings=djfans.local
python manage.py migrate --settings=djfans.local
python manage.py runserver --settings=djfans.local



- 이슈와 해결방법

포스팅이 멀티아규먼트를 뱉어 에러 발생
구독시점보다 전 포스팅 보이지 않음


이슈 확인 - 도커 랑 연동 끝