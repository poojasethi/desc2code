for _ in range(input()):
    try:
        eval(raw_input())
        print 'YES'
    except TypeError:
        print 'YES'
    except:
        print 'NO'