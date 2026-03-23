print("Hello, World")
#CALCULADORA
def culacao(x,y,operacao):
    opera={
        '-' : x-y,
        '+' : x+y,
        '//':x//y,
        '*' : x*y,
        '/' : x/y,   }
    if operacao in opera:
        print(f'{x}{operacao}{y} = {opera[operacao]}')
    else: print("operação invalida")



x= int(input('Digite o primeiro numero : '))
operacao=(input('Digite a operacao que deseja (*= veses, /= divisao) : '))
y= int(input('Digite o segundo numero : '))
culacao(x,y,operacao)