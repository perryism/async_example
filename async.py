from urllib import request

def add(x, y, sleep=0):
    if sleep > 0: print("Sleep for %s seconds"%sleep)
    with request.urlopen('http://localhost:5555/add?x=%s&y=%s&sleep=%s'%(x,y,sleep)) as f:
        return int(f.read())

def multiply(x, y, sleep=0):
    if sleep > 0: print("Sleep for %s seconds"%sleep)
    with request.urlopen('http://localhost:5556/multiply?x=%s&y=%s&sleep=%s'%(x,y,sleep)) as f:
        return int(f.read())

import concurrent.futures

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    a = executor.submit(add, 3, 4, 0)
    m = executor.submit(multiply,  4, 4)
    while a.running() or m.running():
        import time
        time.sleep(1)
        print("waiting...")

print(a.result() + m.result())
