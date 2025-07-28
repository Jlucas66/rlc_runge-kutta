import matplotlib.pyplot as plt

def salvar_grafico_png(t, i, caminho='grafico_corrente.png'):
    plt.figure(figsize=(10, 5))
    plt.plot(t, i, label='Corrente i(t)')
    plt.title('Corrente no Circuito RLC')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Corrente (A)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(caminho)
    plt.close()
    print(f"[INFO] Gráfico salvo como imagem em: {caminho}")
