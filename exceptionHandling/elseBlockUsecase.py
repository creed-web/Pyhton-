#here I'm going to use try, except and else blocks to handle an basic error
try:
    try:
        a = int(input("Enter an number: "))
        result = a/10
    except ZeroDivisionError as zd:
        print(zd)
    except ValueError as ve:
        print(ve)
    except Exception as ex:
        print(ex)
    else:
        print(f"Your answer is : {result}")
except Exception as ex1:
    print(ex1)
