def objective2(x, a):
    alpha, beta, g, eta,w = x
    a0,a1,a2,a3=a
    result=-a3*w**3+a1*w
    return result