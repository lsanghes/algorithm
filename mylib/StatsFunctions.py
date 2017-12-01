def mean(A):
    return sum(A)/len(A)

def median(A):
    n = len(A)
    return A[(n-1)//2] if n%2!=0 else (A[n//2-1]+A[n//2])/2

def mode(A):
    counter = Counter(A)
    _,maxcount = counter.most_common(1)[0]
    return sorted([k for k,v in counter.items() if v == maxcount])[0]

def weighted_mean(As, Bs):
    return sum([a*b for a,b in zip(As,Bs)]) / sum(Bs)

def first_quatile(A):
    return median(A[:len(A)//2])

def third_quatile(A):
    return median(A[(len(A)+1)//2:])

def standard_devivation(A):
    n = len(A)
    u = sum(A) / n
    return (sum([(a-u)**2 for a in A])/n)**0.5

def nCk(n, k):
    return math.factorial(n) / math.factorial(k) / math.factorial(n-k)

def binomial(k, n, p):
    return nCk(n, k) * p**k * (1-p)**(n-k)

def poisson(lambd, k):
    return lambd**k * math.exp(lambd*-1) / math.factorial(k)

def normal_cdf(x, u, sd):
    return (1+ math.erf((x-u) / sd / math.sqrt(2))) / 2

def normal_cdf(x, u, sd):
    from scipy.stats import norm
    d = norm(u, sd)
    return d.cdf(x)


