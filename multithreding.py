from concurrent.futures import Executor, ThreadPoolExecutor
import threading
import time

def fun(seconds):
    print(f"Sleeping for {seconds} sec")
    time.sleep(seconds)

# fun(4)
# fun(2)
# fun(3)
def main():
    time1 = time.perf_counter()

# in the bellow code target is the function which we are going to call and args is the arguments which we are going to provide

    t1 = threading.Thread(target=fun, args=[4])
    t2 = threading.Thread(target=fun, args=[2])
    t3 = threading.Thread(target=fun, args=[3])


    t1.start()
    t2.start()
    t3.start()

    # t1.join()
    # t2.join()
    # t3.join()

    time2 = time.perf_counter()

    print(time2 - time1)
    
def poolingDemo():
    with ThreadPoolExecutor(max_workers=4) as executor:
    #     future = executor.submit(fun,4)
    #     print(future.result())
        
    #     future1 = executor.submit(fun,1)
    #     print(future1.result())
    #     future2 = executor.submit(fun,3)
    #     print(future2.result())
        l = [3,5,4,8,12,10]
        results = executor.map(fun,l)
        for result in result:
            print(result)
    
poolingDemo()