from datetime import date
ano = int(input('Digite um ano para analisar se é Bissexto ou não. Para verificar o ano atual, digite 0: '))
if ano == 0:
    ano = date.today().year  # Pega o ano atual e mostra no console
if (ano%4) == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é Bissexto.')
else:
    print(f'O ano {ano} não é Bissexto.')