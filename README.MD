# Instagram clone coding

Django로 Instagram 만들기

## I. 정보

- App : https://localhost:8000 에서 실행가능
- Git : https://github.com/doohong91/Instagram_clone

## II. 사용 라이브러리

- django 3.0.6
- django-bootstrap4 1.1.1
- pillow 7.1.2

`pip install -r requirements.txt`를 통해 설치가능

> 가상환경을 구성하여 위의 명령어를 실행하는 것을 권장합니다.
> (가상환경 관련 참고 [링크](https://dojang.io/mod/page/view.php?id=2470))

## III. 실행방법

Terminal에서 아래와 같은 명령어를 입력하면 APP을 실행할 수 있습니다.

```
# 데이터 베이스 생성
python manage.py migrate

# 장고 서버 실행
python manage.py runserver
```

### III.I Django admin 페이지 접속방법

아래와 같은 명령어를 통해 django admin 페이지에 접속하실 수 있습니다.

```
# 관리자 계정 생성
python manage.py createsuperuser
```

`https://localhost:8000/admin`을 통해 admin 페이지 접속 가능

## IV. Comment

장고를 통해 기본적인 CRUD 기능만 구현하였습니다.
필요시 추가기능을 더하거나 UI를 개선하시면서 공부하시면 좋을 것 같습니다.
