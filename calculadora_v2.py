import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora_v2")

entry = tk.Entry(janela, font=("Arial", 18), justify="right")
entry.config(state="readonly")
entry.grid(row=0, column=0, columnspan=4, sticky="ew")

valor_1 = None
operacao = None
valor_2 = None
resultado_calculado = False

def atualizar_entry(valor, limpar_antes=True): 
    entry.config(state=tk.NORMAL)
    if limpar_antes:
        entry.delete(0, tk.END)
    entry.insert(tk.END, str(valor))
    entry.config(state="readonly")

def clicar_botao(numero):
    global resultado_calculado
    resultado_calculado = False
    atualizar_entry(numero, limpar_antes=False)

def clicar_operacao(op):
    global valor_1, operacao, resultado_calculado
    if not entry.get(): return
    valor_1 = float(entry.get())
    operacao = op
    resultado_calculado = False
    atualizar_entry("", limpar_antes=True)

def clicar_igual():
    global valor_1, operacao, valor_2, resultado_calculado
    if not entry.get(): return
    if resultado_calculado:
        valor_1 = float(entry.get())
    else:
        valor_2 = float(entry.get())
    resultado = None
    if operacao == "+":
        resultado = valor_1 + valor_2
    elif operacao == "-":
        resultado = valor_1 - valor_2
    elif operacao == "*":
        resultado = valor_1 * valor_2
    elif operacao == "/":
        if valor_2 != 0:
            resultado = valor_1 / valor_2
        else:
            resultado = "Não é possível dividir por zero"
    resultado_calculado = True
    atualizar_entry(resultado, limpar_antes=True)

def limpar():
    global valor_1, operacao, resultado_calculado
    atualizar_entry("", limpar_antes=True)
    valor_1 = None
    operacao = None
    resultado_calculado = False

def alterar_sinal():
    if entry.get():
        valor = float(entry.get())
        atualizar_entry(-valor, limpar_antes=True)

def clicar_virgula():
    if "." not in entry.get():
        atualizar_entry(".", limpar_antes=False)

botao_7 = tk.Button(janela, text="7", command=lambda: clicar_botao(7), width=5, height=2, font=("Arial", 14), bg="#EDEAEA")
botao_7.grid(row=1, column=0, sticky="ew",)   

botao_8 = tk.Button(janela, text="8", command=lambda: clicar_botao(8), width=5, height=2, font=("Arial", 14), bg="#EDEAEA")
botao_8.grid(row=1, column=1, sticky="ew")   

botao_9 = tk.Button(janela, text="9", command=lambda: clicar_botao(9), width=5, height=2, font=("Arial", 14), bg="#EDEAEA" )
botao_9.grid(row=1, column=2, sticky="ew")

botao_4 = tk.Button(janela, text="4", command=lambda: clicar_botao(4), width=5, height=2, font=("Arial", 14), bg="#EDEAEA")
botao_4.grid(row=2, column=0, sticky="ew")   

botao_5 = tk.Button(janela, text="5", command=lambda: clicar_botao(5), width=5, height=2, font=("Arial", 14), bg="#EDEAEA")
botao_5.grid(row=2, column=1, sticky="ew")   

botao_6 = tk.Button(janela, text="6", command=lambda: clicar_botao(6), width=5, height=2, font=("Arial", 14), bg="#EDEAEA")
botao_6.grid(row=2, column=2, sticky="ew")

botao_1 = tk.Button(janela, text="1", command=lambda: clicar_botao(1), width=5, height=2, font=("Arial", 14), bg="#EDEAEA")
botao_1.grid(row=3, column=0, sticky="ew")

botao_2 = tk.Button(janela, text="2", command=lambda: clicar_botao(2), width=5, height=2, font=("Arial", 14), bg="#EDEAEA")
botao_2.grid(row=3, column=1, sticky="ew")

botao_3 = tk.Button(janela, text="3", command=lambda: clicar_botao(3), width=5, height=2, font=("Arial", 14), bg="#EDEAEA")
botao_3.grid(row=3, column=2, sticky="ew")

botao_0 = tk.Button(janela, text="0", command=lambda: clicar_botao(0), width=5, height=2, font=("Arial", 14), bg="#EDEAEA")
botao_0.grid(row=4, column=1, sticky="ew")

botao_soma = tk.Button(janela, text="+", command=lambda: clicar_operacao("+"), width=5, height=2, font=("Arial", 14), bg="#CFF5C7")
botao_soma.grid(row=1, column=3, sticky="ew")

botao_subtracao = tk.Button(janela, text="–", command=lambda: clicar_operacao("-"), width=5, height=2, font=("Arial", 14), bg="#CFF5C7")
botao_subtracao.grid(row=2, column=3, sticky="ew")

botao_multiplicacao = tk.Button(janela, text="×", command=lambda: clicar_operacao("*"), width=5, height=2, font=("Arial", 14), bg="#CFF5C7")
botao_multiplicacao.grid(row=3, column=3, sticky="ew")

botao_divisao = tk.Button(janela, text="/", command=lambda: clicar_operacao("/"), width=5, height=2, font=("Arial", 14), bg="#CFF5C7")
botao_divisao.grid(row=4, column=3, sticky="ew")

botao_virgula = tk.Button(janela, text=",", command=lambda: clicar_virgula(), width=5, height=2, font=("Arial", 14), bg="#EDEAEA")
botao_virgula.grid(row=4, column=2, sticky="ew")

botao_sinal = tk.Button(janela, text="±", command=alterar_sinal, width=5, height=2, font=("Arial", 14), bg="#EDEAEA")
botao_sinal.grid(row=4, column=0, sticky="ew")

botao_igual = tk.Button(janela, text="=", command=lambda: clicar_igual(), height=2, font=("Arial", 14), bg="#DEDCDC")
botao_igual.grid(row=5, column=0, columnspan=3, sticky="ew")

botao_limpar = tk.Button(janela, text="C", command=limpar, width=5, height=2, font=("Arial", 14), bg="#F4C8C8")
botao_limpar.grid(row=5, column=3, sticky="ew") 

janela.mainloop()