#introductory practises on dynamic programming

#example 1:factorial problem


#classic way to implement it
def c_factorial(n):
    result = 1
    for i in range (n,0,-1):
        result *= i
    return result

print (c_factorial(5))


#recursive way to implement
def recursive_factorial(n):

    #base case
    if n == 1:
        return 1

    else:
        return ( n *recursive_factorial(n-1))


print(recursive_factorial(5))




#example 2: fibonacci sequence

#classic way to implement

def c_fibonacci(n): # return the fibonacci sequence
    if n == 0:
        return [0]

    elif n ==1:
        return [0, 1]

    fibs = [0, 1] # for n>=2

    for i in range (2,n):
        fibs.append(fibs[-1]+fibs[-2])

    return fibs


print(c_fibonacci(5))


#recursive way to implement

def recursive_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in calculated:
        return calculated[n]
    else:
        calculated[n] = recursive_fib(n-1)+recursive_fib(n-2)
        return calculated[n]

calculated = {} #store fibonnacci sequence
print(recursive_fib(5)) #the nth term in the fibonacci sequence
print(calculated)



#example 3: express a number as sum of square of number

#classic way to implement
def c_minsq(n):
    if n <= 3:  #no square
        return n

    #max num. e.g., 27 = 27 * 1^2
    res = n

    for x in range (1, n+1):
        temp = x**2
        if temp > n:
            break
        else:
            res = min(res, 1+c_minsq(n-temp))
    return res

print(c_minsq(10))


#recursive way to implement
def recursive_minsq(n):
    if n<=3:
        return n

    dp = list(range(n+1))
    print("Original loop:",dp)

    for i in range (4, n+1):
        #loop thru small numbers
        for x in range (1, int(i**0.5)+1):
            #get the min squares by looking at table
            dp[i] = min(dp[i], 1+dp[i-x*2])
            print("At each loop:",dp)
    return dp[n]

print(recursive_minsq(16))