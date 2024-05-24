import pywhatkit as wpp
num = int(input('Escreva apenas o DDD e o número de quem irá receber a mensagem (apenas números): '))
convert = str(num)
numConvert = str('+55' + convert)
msg = str(input('Escreva a mensagem: '))
hour = int(input('Qual hora vai enviar essa mensagem? '))
minute = int(input('Qual o minuto vai enviar essa mensagem? '))
wpp.sendwhatmsg(numConvert, msg, hour,minute)
print('Programa finalizado!')
