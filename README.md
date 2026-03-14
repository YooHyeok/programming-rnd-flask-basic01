
## Flask 설치
```bash
pip install flask
```

## 기본 메인 스레드 코드
- Get 방식 루트 요청
  ```py
  from flask import Flask # 웹 애플리케이션 클래스
  app = Flask(__name__) # 웹 애플리케이션 객체 생성 (실행되는 모듈 파일 정보 전달)
  
  @app.route('/') # route: url 경로와 함수를 연결하는 기능 (핸들러 매핑과 유사)
  def gello_world():
      return 'Hello World!'
  
  if __name__ == '__main__':
      app.run() # 웹서버 기동
  ```

## 기동
### 실행
- Pycharm
  ```bash
  Ctrl + Shift + F10
  ```
- VSC
  ```bash
  Ctrl + F5
  ```
### 디버그  
- Pycharm
  ```bash
  Ctrl + Shift + F19
  ```
- VSC
  ```bash
  F5
  ``
  
## 웹 서버 객체 생성과 모듈정보 전달
웹 서버 객체를 생성할 때 전달되는 __name__ 현재 생성되는 Flask 웹 서버 객체가 해당 모듈의 파일 위치를 기준으로  
애플리케이션의 루트 경로를 계산하고, template 및 static 같은 리소스 디렉토리를 찾기 위해 사용된다.  

그렇다면 Flask 객체가 실행되는 모듈이 "__main__"인 메인 모듈일 경우엔 모듈파일을 어떻게 찾아갈까?  
기본적으로 파이썬에서 최초 실행되는 파일은 인터프리터에 의해 내부적으로 실행된 파일의 모듈 객체를 만들고, 그 모듈 이름을 __main__로 지정한다.
### main 모듈 정보 출력 예제
```py
import sys
main_module = sys.modules["__main__"]
print(main_module) # <module '__main__' from '.../test.py'>
print(main_module.__file__) # "/project/app.py"
```

## Get방식 요청 파라미터 전달

### URL Variable (Variable Rule)
웹 서버 객체인 app의 route 데코레이터에 url을 지정할 때 중괄호 사이에 `<파라미터명>` 형태로 지정한다.  
기본적으로 문자열 타입이므로 정수 타입으로 받기 위해서는 파라미터명 앞에 `<int: 파라미터명>` `:` 구분자 기준으로 타입인 int를 지정한다
- string
  ```py
  from flask import Flask
  app = Flask(__name__)
  
  @app.route('/user/<username>')
  def show_user_profile(username):
      return 'User %s' % username
  
  if __name__ == '__main__':
      app.run()
  ```
- int  
  ```py
  from flask import Flask
  app = Flask(__name__)
  
  @app.route('/post/<int:post_id>')
  def show_post(post_id):
      return 'Post %d' % post_id
  
  if __name__ == '__main__':
      app.run()
  ```