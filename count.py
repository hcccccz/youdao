import time

def count(current,full):
    minute = (full-current)*5
countt = 600
while countt >=0:
    min = countt // 60
    sec = countt % 60
    print('{}:{}'.format(min,sec))
    time.sleep(1)
    countt -= 1
