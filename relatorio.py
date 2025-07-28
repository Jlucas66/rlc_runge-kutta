from fpdf import FPDF
from plotagem import salvar_grafico_png

def gerar_relatorio_pdf(t, i, R, L, C, tipo_fonte, V0, A, f, nome_pdf='relatorio_rlc.pdf'):
    caminho_imagem = 'grafico_corrente.png'
    salvar_grafico_png(t, i, caminho_imagem)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Relatório da Corrente no Circuito RLC", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    
    # Usar "Ohms" em vez do símbolo Ω
    pdf.multi_cell(0, 10, f"Parâmetros do circuito:\n"
                          f"R = {R} Ohms\nL = {L} H\nC = {C} F\n"
                          f"Tipo de fonte: {tipo_fonte}\n")
    
    if tipo_fonte == 'cc':
        pdf.multi_cell(0, 10, f"Tensão DC: {V0} V")
    else:
        pdf.multi_cell(0, 10, f"Fonte AC: Amplitude = {A} V, Frequência = {f} Hz")
    
    pdf.ln(5)
    pdf.image(caminho_imagem, w=180)
    pdf.output(nome_pdf)
    print(f"[INFO] Relatório PDF gerado: {nome_pdf}")
