# https://rurukblog.com/post/Python-threading-file-monitor/
import threading
import time
import os
import math

class file_monitor:
	def __init__(self):
		# flag for Loop
		self.Loop = True
		# monitor file name and path
		self.file_path = os.getcwd() + "/monitor_dir/test.txt"

	def main(self):
		print("start monitoring")

		file_monitor = threading.Thread(target=self.file_monitor_execute)
		file_create = threading.Thread(target=self.file_create, args=(5,))

		# run thread
		file_monitor.start()
		file_create.start()

		# run else process
		print("measure process time")
		start_time = time.time()
		while self.Loop:
			time.sleep(2)
			exec_time = time.time()
			print(f"process time : {math.floor(exec_time - start_time)} s")
		print("End monitor process")

	def file_monitor_execute(self):
        # check seton file in monitor_dir each 3s
        while self.Loop:
            print("monitoring file")
            time.sleep(3)

            if os.path.isfile(self.file_path):
                print("seton file")
                self.Loop=False

    def file_create(self, second):
        time.sleep(second)
        f = open(self.file_path, "w")
        print("create file")
        f.write("")
        f.close()


if __name__ == "__main__":
    file_monitor = file_monitor()
    file_monitor.main()
