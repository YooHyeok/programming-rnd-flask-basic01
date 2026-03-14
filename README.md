
## Flask 설치
```bash
pip install flask
```

## 기본 메인 스레드 코드
```py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def gello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
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