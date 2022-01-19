# datetime과 같은 모듈을 사용하여
# 객체를 인코딩 혹은 디코딩하는 도중에
# 예외가 발생하는 경우
import datetime
import json


now = datetime.datetime.utcnow()
print(now)

json_now = json.dumps(now, default=str)
print(json_now)