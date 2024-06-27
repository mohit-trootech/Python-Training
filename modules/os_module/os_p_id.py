# Python program to explain os.abort() method

# importing os module
import os, signal

# Create a child process
# using os.fork() method
pid = os.fork()


# pid greater than 0
# indicates the parent process
if pid > 0:
    # Parent process
    print("\nIn Parent process")

    # Wait for the completion
    # of child process and get
    # its pid and exit status indication
    # using os.wait() method
    info = os.wait()

    sig = os.WTERMSIG(info[1])
    print("Child exited due to signal no:", sig)
    print("Signal name:", signal.Signals(sig).name)

else :

    # child process
    print("In child process")
    print("Process ID:", os.getpid())
    print("Hello ! Geeks")

    # Abort the child process
    # by generating SIGABRT signal
    # using os.abort() method
    os.abort()
