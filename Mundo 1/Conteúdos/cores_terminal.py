'''
    Para colocar uma cor no nosso terminal, precisamos utilizar o comando: \033[style;text;backgroundm
                                                                        Ex: \033[0;33;44m

                style:              Text:                  Back:
                0 = None            30 = Branco            40 = Branco
                1 = Bold            31 = Vermelho          41 = Vermelho
                4 = Underline       32 = Verde             42 = Verde
                7 = Negative        33 = Amarelo           43 = Amarelo
                                    34 = Azul              44 = Azul
                                    35 = Roxo              45 = Roxo
                                    36 = Ciano             46 = Ciano
                                    37 = Cinza             47 = Cinza


Exemplo de como usar:  print('\033[31mOlá mundo!') - Com esse comando, o texto 'Olá mundo' irá ficar da cor vermelha
'''                                        