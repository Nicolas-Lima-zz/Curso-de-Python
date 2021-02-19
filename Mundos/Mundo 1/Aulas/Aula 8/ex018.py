from math import cos,sin,tan, radians
ang = float(input('Informe o ângulo: '))
rad = radians(ang)
seno = sin(rad)
cos = cos(rad)
tan = tan(rad)
print('Valores:\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(seno,cos,tan))