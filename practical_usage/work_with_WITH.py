try:
    x=1/0
except:
    print("error")
else:
    print("sucessed!")
finally:
    print("finished!")



with 1/0:
    x = 1/0