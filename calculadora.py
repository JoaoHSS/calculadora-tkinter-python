import tkinter as tk
from functools import partial

operacoes = {"+":lambda x,y:x+y,
             "-":lambda x,y:x-y,
             "*":lambda x,y:x*y,
             "/":lambda x,y:x/y}

termo1 = 0
operacao = ""
novoNumero = True
#para fazer operação várias vezes ao clicar repetidamente no "="
operacaoClicada = False

def escrever(n):
    global novoNumero
    if novoNumero:
        resultado["text"] = ""
        novoNumero = False
    resultado["text"] += str(n)

def bt_apagar():
    if len(resultado["text"]) > 0:
        resultado["text"] = resultado["text"][:-1]

def bt_limpar():
    equacao["text"] = ""
    resultado["text"] = ""

def bt_ponto():
    if "." not in resultado["text"]:
        global novoNumero
        if resultado["text"] == "":
            novoNumero = False
            resultado["text"] = "0."
        else:
            if novoNumero:
                resultado["text"] = "0."
            else:
                resultado["text"] += "."

def tratar_erros():
    if operacao == "/":
        if resultado["text"] == "impossível dividir":
            return True
        elif float(resultado["text"]) == .0:
            resultado["text"] = "impossível dividir"
            return True

def bt_igual():
    global operacao, novoNumero, termo1, operacaoClicada

    if resultado["text"]== "" or operacao == "": return
    
    if tratar_erros(): return
    
    novoNumero = True

    if operacaoClicada:
        equacao["text"] += resultado["text"]
        var = operacoes[operacao](termo1, float(resultado["text"]))
        termo1 = float(resultado["text"])
        operacaoClicada = False
    else:
        equacao["text"] = resultado["text"] + operacao + str(termo1)
        var = operacoes[operacao](float(resultado["text"]), termo1)

    if var == int(var):
        var = int(var)
    resultado["text"] = f"{var}"
    
def bt_operacao(sinal):
    if resultado["text"] == "":
        return
    global termo1, operacao, novoNumero, operacaoClicada
    operacao = sinal
    novoNumero, operacaoClicada = True, True
    termo1 = float(resultado["text"])
    equacao["text"] = resultado["text"]+sinal

# --------------------- tkinter ---------------------
janela = tk.Tk(className="Calculadora")
janela.geometry("+800+300")

f = ("Arial", 25)

#não diminui as linhas de código, mas se for alterar algo genérico fica mais de boa
def botao(texto, comando=lambda:None):
    return tk.Button(janela, width=5, text=texto, font=f, command=comando, bg="dark grey")


equacao = tk.Label(janela, width=5, font=f, bg="grey", relief="sunken", border=10)
resultado = tk.Label(janela, width=12, font=f, bg="grey", relief="sunken", border=10)

# botões com funções mais especificas
bt_Limpar = botao("C", bt_limpar)
bt_Apagar = botao("⇽", bt_apagar)
btIgual = botao("=", bt_igual)
btPonto = botao(".", bt_ponto)

# botões de calculo
btSoma = botao("+")
btSoma["command"] = partial(bt_operacao, btSoma["text"])

btSubt = botao("-")
btSubt["command"] = partial(bt_operacao, btSubt["text"])

btMult = botao("*")
btMult["command"] = partial(bt_operacao, btMult["text"])

btDivi = botao("/")
btDivi["command"] = partial(bt_operacao, btDivi["text"])

# botões dos números
numeros = []
for n in range(0,10):
    numeros.append(botao(f"{n}"))
    numeros[n]["command"] = partial(escrever, n)

# posicionamento dos widgets
equacao.grid(row=0, column=0, columnspan=3, sticky="nswe")
resultado.grid(row=1, column=0, columnspan=3, sticky="nswe")

bt_Limpar.grid(row=1, column=3)
bt_Apagar.grid(row=0, column=3)
btIgual.grid(row=5, column=2)
btPonto.grid(row=5, column=1)

btSoma.grid(row=5, column=3)
btSubt.grid(row=4, column=3)
btMult.grid(row=3, column=3)
btDivi.grid(row=2, column=3)

count=9
for n in range(2,5):
    for m in range(2,-1,-1):
        numeros[count].grid(row=n, column=m)
        count-=1
numeros[0].grid(row=5, column=0)

# temanho da janela
janela.update()
a = janela.winfo_height()
b = janela.winfo_width()
janela.maxsize(b,a)
janela.minsize(b,a)
janela.mainloop()