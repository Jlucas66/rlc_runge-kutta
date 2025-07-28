# Parâmetros do circuito
R = 100       # Ohms
L = 0.5       # Henry
C = 1e-3      # Farads

# Fonte
tipo_fonte = 'ca'  # 'cc' ou 'ca'
V0 = 10            # se tipo_fonte = 'cc'
A = 10             # Amplitude (CA)
f = 60             # Frequência (Hz)

# Simulação
x0 = [0, 0]        # Condição inicial: [i(0), di/dt(0)]
t0 = 0             # tempo inicial (s)
tf = 0.1           # tempo final (s)
h = 1e-5           # passo
