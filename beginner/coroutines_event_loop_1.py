# 코루틴(coroutines)
# 다양한 지점에서 일시 중지되는 함수
# 이벤트 루프(event loop)
# 코루틴을 예약하고 실행

# 일반적인 멀티 태스킹은
# 운영체제가 여러 프로세스에 작업을 수행하는 것
# 운영체제는 어떤 프로세스가 CPU를 많이 차지하는지,
# 언제 I/O를 개방할 것인지 등의 작업을 공정하게 처리될 수 있도록 한다.

# 그러나,
# 이벤트 루프는 코루틴이 언제 시작하고, 중지될 수 있는지 표시되는
# 협동적인 멀티태스킹을 제공한다.

# 단일 스레드에서 실행되므로, 잠재적인 문제가 없다.

import asyncio
from timeit import timeit


# async def wicked():
#     print('Surrender')
#     await asyncio.sleep(2)
#     print("Dorothy!")
#
#
# check_time = timeit("asyncio.run(wicked())", globals=globals(), number=1)
#
# print(check_time)

async def say(phrase, seconds):
    print(phrase)
    await asyncio.sleep(seconds)  # 1. 호출 자체는 코루틴, API 호출처럼 시간이 많이 걸리는 곳에 사용한다.


async def wicked():
    task_1 = asyncio.create_task(say("Surrender,", 2))  # 3. time.sleep(2)에서 2초 동안 블록되지 않고
    task_2 = asyncio.create_task(say("Dorothy!", 0))  # 3.1. 별도의 작업이기 때문에 바로 출력되는 것을 알 수 있음 / task_1의 영향이 미치지 않았음
    await task_1
    await task_2


asyncio.run(wicked())  # 2. 동기식 파이썬 코드로 코루틴을 실행했음