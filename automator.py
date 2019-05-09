from datetime import datetime
from threading import Timer
import sign_in
import time

x = datetime.today()
y = x.replace(day=x.day+1, hour=2, minute=30, second=0, microsecond=0)
delta_t = y - x


secs = delta_t.seconds + 1


count = 0
def hello_world():
	global count
	while count < 5400:
		flag = sign_in.main()
		if flag:
			break
		count += 5
		time.sleep(5)


t = Timer(secs, hello_world)
t.start()
