def objective1(x, a):
    alpha, beta, g, eta, w = x
    a0, a1, a2, a3 = a
    result = w**4 - a2*w**2 + a0
    return result