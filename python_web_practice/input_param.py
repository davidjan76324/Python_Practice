import getopt
import sys
try:
    #$python3 input_param.py -n 123 -e david_jan76324@hotmail.com --age=18
    # getopt(argv, shortopts, longopts=[])
    # argv：要解析的參數，通常是sys.argv[1:]
    # shortopts：要識別的短格式(-)，其有要求參數後須加:
    # longopts：可選，要識別的長格式(--)，有參數要求加=
    # 
    # Ref: https://smiliu.xyz/posts/15191
    #  #
    opts, args = getopt.getopt(sys.argv[1:], 'n:e:', ["age="])
    """
    -n: name
    -e: email
    --age: age
    """

    #print(opts) #[('-n', '123'), ('-e', 'david_jan76324@hotmail.com'), ('--age', '18')]
    #print(args)
    for i in opts:
        if '-n' in i:
            name = i[1]
        if '-e' in i:
            email = i[1]
        if '--age' in i:
            age = i[1]
    allParam = {"name": name, "email": email, "age": age}
    print(allParam)
except Exception as e:
    print("--Error:{0}".format(e))
    exit()
