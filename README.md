# RadioDecrypt 

O programa analisa transmissões de rádio acima de 100 MHz para identificar e extrair mensagens inimigas . Ele processa os sinais captados pelo espião Kni, interpretando os dados recebidos e transformando-os em uma mensagem compreensível, exemplo:

90c87esd67uj,./';*&^120lin87uj101gu87km102a77jh150gem..&


Onde, da esquerda para direita:
● 90 é a frequência em Mhz.
● c é o código lido na frequência de 90Mhz.
● 87 é a frequência do próximo código.
● esd é o código lido na frequência de 87Mhz
● 67 é a frequência do próximo código.
● uj é o código lido na frequência de 67Mhz
● ,./';&^ foi uma interferência que ocorreu quando lia-se o código da frequência de 67Mhz.
Assim, no fragmento acima, a mensagem transmitida acima de 100Mhz foi: linguagem,
pois, lin foi transmitido a 120Mhz, gu a 101Mhz, a a 102Mhz e gem a 150Mhz.
● A frequência estará sempre entre 1 e 200Mhz;
● Toda interferência será ignorada. Considera-se interferência todo caractere
diferente de uma letra ou um número;
● O tamanho máximo da mensagem é de 100 caracteres.

Resumindo :
O programa é capaz de receber uma cadeia codificada de no máximo 250 caracteres e retornar a
mensagem transmitida acima de 100Mhz.

Linguaguem : Python <br>
IDE : vscode <br>
Feito por : Lucas Frotte Lafin <br>
Fonte : Prof. Adonai Medrado https://bit.ly/3ZzhTLr <br>
