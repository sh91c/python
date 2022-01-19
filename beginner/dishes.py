# 파이썬 Queue에 대해서
# import threading, queue, time
#
# q = queue.Queue()
#
#
# def worker():
#     while True:
#         item = q.get()
#         print(f"Working on {item}")
#         time.sleep(1)
#         print(f"Finished {item}")
#         time.sleep(1)
#         q.task_done()  # 큐에 넣은 작업이 완료되었음
#
#
# # 워커 쓰레드기 turn on
# threading.Thread(target=worker, daemon=True).start()
#
# # 30개 작업 요청을 worker함수에 전달
# for item in range(10):
#     q.put(item)
#
# print('모든 작업 요청 전달 완료\n', end='')
#
# # q.join(): 모든 작업이 완료될 때까지 block 되고있는 상황
# q.join()
#
# print('모든 작업이 완료됨.')

# import multiprocessing as mp
#
#
# def washer(dishes, output):
#     for dish in dishes:
#         print('Washing', dish, 'dish')
#         output.put(dish)
#
#
# def dryer(input):
#     while True:
#         dish = input.get()
#         print('Drying', dish, 'dish')
#         input.task_done()
#
# if __name__ == '__main__':
#     dish_queue = mp.JoinableQueue()
#     dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
#     dryer_proc.daemon = True
#     dryer_proc.start()
#
#     dishes = ['salad', 'bread', 'entree', 'desert']
#     washer(dishes, dish_queue)
#     dish_queue.join()

################################################################

# import threading, queue
# import time
#
#
# def washer(dishes, dish_queue):
#     for dish in dishes:
#         print("Washing", dish, "\n")
#         time.sleep(1)
#         dish_queue.put(dish)
#
#
# def dryer(dish_queue):
#     while True:
#         dish = dish_queue.get()
#         print("Drying", dish, "\n")
#         time.sleep(2)
#         dish_queue.task_done()
#
#
# if __name__ == '__main__':
#     dish_queue = queue.Queue()
#     for n in range(2):
#         dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
#         dryer_thread.start()
#         dishes = ['salad', 'bread', 'entree', 'dessert']
#         washer(dishes, dish_queue)
#         dish_queue.join()
