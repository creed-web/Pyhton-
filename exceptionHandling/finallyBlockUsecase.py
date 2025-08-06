#The finally block is used to run the code wether there is an error or not the finally blocks runs regardless of anything

try:
    a = bcf
except Exception as ex:
    print(ex)
finally:
    print("The code ran regardless of the error!!")