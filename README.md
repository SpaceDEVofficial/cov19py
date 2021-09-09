# cov19py
a corona api python wrapper

이 레페는 공공데이터포털에서 제공하는 코로나 바이러스 확진 데이터 api를 사용하여 만든 파이썬 레퍼입니다.

## 설치(파이썬 3.8이상을 지원합니다.)
```cmd
pip install cov19py
```

## 예제
```py
import cov19py
import asyncio


async def run():
    crn = cov19py.Client('Your API Key')
    data = await crn.todayCorona()
    print(data['response'])


asyncio.run(run())
```
