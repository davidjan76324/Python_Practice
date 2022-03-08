





try:
    runboob()
except:
    print("--- runboob is Error!")
else:
    try:
        frr = open('SQL_connect.txt', "r+")
        for line in frr:
            print(line)
    except:
        print('---Read File Error!')
finally:
    print("-- alwayse print !")


try:
    print("Use raise!")
    raise
except:
    print("-- Use raise, this is Error!")


x = 10
# if x>5:
#     raise Exception("The x can't bigger than {0}".format(x))


try:
    raise NameError('HiThere') #NameError: HiThere
except ValueError:
    print('An exception flew by!')
#except NameError:
#    print("An exception for NameError!")