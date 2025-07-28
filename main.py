from rlc_modelo import sistema_RLC, runge_kutta_4
from relatorio import gerar_relatorio_pdf
from configuracao import R as R_padrao, L as L_padrao, C as C_padrao
from configuracao import tipo_fonte as tipo_padrao, V0, A, f
from configuracao import t0 as t0_padrao, tf as tf_padrao, h as h_padrao, x0

def solicitar_float(texto, padrao):
    try:
        return float(input(f"{texto} (padrão: {padrao}): ") or padrao)
    except ValueError:
        print("[ERRO] Entrada inválida. Usando valor padrão.")
        return padrao

def main():
    print("=== Simulação de Circuito RLC com Runge-Kutta 4ª Ordem ===")

    R = solicitar_float("Resistência R [Ohms]", R_padrao)
    L = solicitar_float("Indutância L [H]", L_padrao)
    C = solicitar_float("Capacitância C [F]", C_padrao)

    tipo_fonte = input(f"Tipo de fonte (cc ou ca) [padrão: {tipo_padrao}]: ").strip().lower() or tipo_padrao
    while tipo_fonte not in ['cc', 'ca']:
        tipo_fonte = input("Por favor, digite 'cc' ou 'ca': ").strip().lower()

    if tipo_fonte == 'cc':
        V = solicitar_float("Tensão constante V0 [V]", V0)
        A_entrada, f_entrada = 0, 0
    else:
        A_entrada = solicitar_float("Amplitude da fonte senoidal [V]", A)
        f_entrada = solicitar_float("Frequência da fonte senoidal [Hz]", f)
        V = 0

    t0 = solicitar_float("Tempo inicial t0 [s]", t0_padrao)
    tf = solicitar_float("Tempo final tf [s]", tf_padrao)
    h = solicitar_float("Passo de simulação h [s]", h_padrao)

    # Argumentos do sistema
    # Corrigir esta linha:
    args = (R, L, C, tipo_fonte, V) if tipo_fonte == 'cc' else (R, L, C, tipo_fonte, 0, A_entrada, f_entrada)
    print("\n=== Iniciando simulação... ===")
    t, x = runge_kutta_4(sistema_RLC, x0, t0, tf, h, args=args)
    print(f"Corrente no início: {x[0][0]:.4f} A")
    print(f"Corrente ao final (t = {t[-1]:.2f}s): {x[-1][0]:.4f} A")
    print(f"Tipo da fonte: {tipo_fonte}")
    print(f"V0 = {V}, A = {A_entrada}, f = {f_entrada}")
    print(f"Usando condições iniciais x0 = {x0}")

    # Gerar relatório PDF
    gerar_relatorio_pdf(t, x[:, 0], R, L, C, tipo_fonte, V, A_entrada, f_entrada)

if __name__ == '__main__':
    main()
