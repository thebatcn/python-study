from concurrent.futures import process
from multiprocessing import Process
from time import sleep, time

def display(str, nums):
    for n in range(0, nums):
        print(str)
    sleep(5)


def main():
    str1 = "Don't cry because it's over, smile because it happened."
    str2 = "Alrighty, this is a very uncommon barnyard baby."

    start = time()
       
    p1 = Process(target=display,args=(str1,100,))
    p1.start()
    p2 = Process(target=display, args=(str2,100,))
    p2.start()
    p1.join()
    p2.join()

    end = time()
    print(end-start)

def main1():
    start = time()
    sleep(5)
    for i in range(0,100):
        print("Don't cry because it's over, smile because it happened.")
    sleep(5)
    for i in range(0,100):
        print("Alrighty, this is a very uncommon barnyard baby.")
    end = time()
    print(end-start)

if __name__ == "__main__":
    main()