import os
import shutil
path = '/'
memory = shutil.disk_usage(path)
total=memory.total
available=memory.free 
used=memory.used
count=(used/total)*100
print(count)

