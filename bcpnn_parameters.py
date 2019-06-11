import math

def gamma_fucn(a, b, c, d,g11,alp,bet,alp1,bet1):
    N = a + b + c + d
    numerato = (N + alp) * (N + bet)
    denomo = (b + alp1) * (c + bet1)
    # print(b)
    # print(alp1)
    # print(c)
    # print(bet1)
    val = numerato / denomo
    val = g11 * val
    return val


def expectation(a, b, c, d,g11,alp,bet,alp1,bet1):
    N = a + b + c + d
    # print(type(g11))
    # print(type(alp))
    # print(type(bet))
    # print(type(N))
    # print(type(a))
    numearto = (a + g11) * (N + alp) * (N + bet)
    denomo = (N + gamma_fucn(a, b, c, d,g11,alp,bet,alp1,bet1)) * (a + b + alp1) * (a + c + bet1)
    val = numearto / denomo
    return math.log((val), 2)


def variance_function(a, b, c, d,g11,alp,bet,alp1,bet1):
    logValue = 1/(math.log(2, math.e)**2)
    N = a + b + c + d
    gam = gamma_fucn(a, b, c, d,g11,alp,bet,alp1,bet1)
    numerator = (N - a + gam - g11)
    d1 = (a + g11) * (1 + N + gam)
    d2num = (N - a - b + alp - alp1)
    d2den = (a + b + alp1) * (1 + N + alp)
    d2 = d2num / d2den
    d3num = (N - a - c + bet - bet1)
    d3den = (a + c + bet1) * (1 + N + bet)
    d3 = d3num / d3den  
    denom = d1 + d2 + d3
    val = numerator / denom
    val = val * logValue
    return val


def standard_deviation(value):
    return math.sqrt((value))

def signal_output(a,b,c,d,g11,alp,bet,alp1,bet1):
    exp = expectation(a, b, c, d,g11,alp,bet,alp1,bet1)
    var = variance_function(a, b, c, d,g11,alp,bet,alp1,bet1)
    std = standard_deviation(var)
    ans = exp - (2 * std)
    # print(ans)
    # input()
    if 0 < ans <= 1.5:
        return("Weak Signal")
    elif 1.5 < ans <= 3.0:
        return("Medium Signal")
    elif ans > 3.0:
        return("Strong Signal")
    else:
        return("Negative Signal")
    # else:
    #     print("Not valid")
    #     raise ValueError
