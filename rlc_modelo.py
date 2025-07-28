import numpy as np

import numpy as np

def sistema_RLC(t, x, R, L, C, tipo_fonte='cc', V0=0, A=0, f=0):
    q, i = x  # q(t): carga no capacitor, i(t): corrente no circuito
    
    if tipo_fonte == 'cc':
        V = V0
    elif tipo_fonte == 'ca':
        omega = 2 * np.pi * f
        V = A * np.sin(omega * t)
    else:
        raise ValueError("tipo_fonte deve ser 'cc' ou 'ca'")
    
    # Equações diferenciais corretas para circuito RLC série:
    dq_dt = i
    di_dt = (V - R*i - q/C) / L
    
    return np.array([dq_dt, di_dt])


def runge_kutta_4(f, x0, t0, tf, h, args=()):
    n = int((tf - t0) / h)
    t = np.linspace(t0, tf, n+1)
    x = np.zeros((n+1, len(x0)))
    x[0] = x0

    for i in range(n):
        k1 = f(t[i], x[i], *args)
        k2 = f(t[i] + h/2, x[i] + h*k1/2, *args)
        k3 = f(t[i] + h/2, x[i] + h*k2/2, *args)
        k4 = f(t[i] + h, x[i] + h*k3, *args)
        x[i+1] = x[i] + h * (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return t, x
