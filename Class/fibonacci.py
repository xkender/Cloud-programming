def fibonacci(n):
    f = [0,1,1]
    for i in xrange(3,n):
        f.append(f[i-1] + f[i-2])
    return 'The %.0fth fibonacci number is: %.0f' % (n,f[-1])
