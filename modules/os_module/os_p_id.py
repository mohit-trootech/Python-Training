import os, signal
from time import sleep

pid = os.fork()

print("Process ID", pid)
sleep(3)
print("Process ID", os.getpid())
sleep(3)
info = os.wait()
print(info)

# if pid > 0:
#     print("\nIn Parent process")
#     info = os.wait()
#
#     sig = os.WTERMSIG(info[1])
#     print("Child exited due to signal no:", sig)
#     print("Signal name:", signal.Signals(sig).name)
#
# else:
#
#     print("In child process")
#     print("Process ID:", os.getpid())
#     print("Hello ! Geeks")
#
#     # Abort the child process
#     # by generating SIGABRT signal
#     # using os.abort() method
#     os.abort()
