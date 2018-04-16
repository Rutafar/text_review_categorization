import datetime
from run_file_pickling import file_pickling


start = datetime.datetime.now()
print(start)
print("Started converting to pickle...")
file_pickling()
print("File pickling ended")

print(datetime.datetime.now() - start)