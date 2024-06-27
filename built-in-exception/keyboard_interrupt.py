"""
KeyboardInterrupt: Raised when the user hits the interrupt key, During execution,
inherited from BaseException class
"""

from time import sleep

print(issubclass(KeyboardInterrupt, BaseException))
print(issubclass(KeyboardInterrupt, Exception))
while True:
    print("Code is Infinite".center(40, "~"))
    sleep(3)
