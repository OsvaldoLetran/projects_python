# """
# Programa para calcular la corriente en un circuito RLC, en construccion
# """
import cmath as c
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, Function, dsolve # , sin


Vo = 10   # voltaje inicial
pVo = 0   # fase o desplazamiento angular
w = 4    # frecuencia angular
R = 2    # resistencia
L = 1/4    # inductancia
C = 1/8    # capacitancia


print('Ecuacion diferencial de corriente')
t = symbols('t')    # definimos variable
i = Function('i')(t)    # definimos Funcion
ip = i.diff(t)
ipp = ip.diff(t)
eq = L*ipp + R*ip + (1/C)*i    # - Vo*sin(w*t + pVo)    # definimos la ED
result = dsolve(eq, i)
print(eq)
print(result)
print('-' * 30)


Z = R + (1j*w*L) - (1j/(w*C))     # impedancia
modulo_Z = abs(Z)
pZ = c.phase(Z)

Io = Vo/Z     # corriente inicial
modulo_Io = abs(Io)
pIo = c.phase(Io)

Ve = Vo + 1j*Z     # ecuacion fasorial
modulo_Ve = abs(Ve)
pVe = c.phase(Ve)


# Fasorial
print("Fasor estatico")
print('Ve real: %5.3f' % Ve.real)
print('Ve imag: %5.3f' % Ve.imag)
print('-' * 30)
print('Fasores     Modulo    Fase')
print('Impedancia: %5.3f  %5.3f' % (modulo_Z, pZ*180/(c.pi)))
print('Voltaje:    %5.3f  %5.3f' % (Vo, pVo*180/(c.pi)))
print('Corriente:  %5.3f  %5.3f' % (modulo_Io, pIo*180/(c.pi)))
print('Ve fasor:   %5.3f  %5.3f' % (modulo_Ve, pVe*180/(c.pi)))


s = np.linspace(0, 1)
s1 = np.linspace(0, 0.3)  # se generan 50 datos en s y s1
t1 = np.linspace(-2*c.pi, 2*c.pi, 200)


# fasores
def v_real(s):
    return (s*Vo).real


def v_imag(s):
    return (s*Vo).imag


def v_realf1(s1):
    return (Vo + s1*c.exp(1j*(pVo + 5*(c.pi)/6))).real


def v_imagf1(s1):
    return (Vo + s1*c.exp(1j*(pVo + 5*(c.pi)/6))).imag


def v_realf2(s1):
    return (Vo + s1*c.exp(1j*(pVo -5*(c.pi)/6))).real


def v_imagf2(s1):
    return (Vo + s1*c.exp(1j*(pVo -5*(c.pi)/6))).imag


def i_real(s):
    return (s*Io).real


def i_imag(s):
    return (s*Io).imag


def i_realf1(s1):
    return (Io + s1*c.exp(1j*(pIo + 5*(c.pi)/6))).real


def i_imagf1(s1):
    return (Io + s1*c.exp(1j*(pIo + 5*(c.pi)/6))).imag


def i_realf2(s1):
    return (Io + s1*c.exp(1j*(pIo - 5*(c.pi)/6))).real


def i_imagf2(s1):
    return (Io + s1*c.exp(1j*(pIo - 5*(c.pi)/6))).imag


def z_real(s):
    return (s*Z).real


def z_imag(s):
    return (s*Z).imag


def z_realf1(s1):
    return (Z + s1*c.exp(1j*(pZ + 5*(c.pi)/6))).real


def z_imagf1(s1):
    return (Z + s1*c.exp(1j*(pZ + 5*(c.pi)/6))).imag


def z_realf2(s1):
    return (Z + s1*c.exp(1j*(pZ - 5*(c.pi)/6))).real


def z_imagf2(s1):
    return (Z + s1*c.exp(1j*(pZ - 5*(c.pi)/6))).imag


def ve_real(s):
    return (s*Ve).real


def ve_imag(s):
    return (s*Ve).imag


def ve_realf1(s1):
    return (Ve + s1*c.exp(1j*(pVe + 5*(c.pi)/6))).real


def ve_imagf1(s1):
    return (Ve + s1*c.exp(1j*(pVe + 5*(c.pi)/6))).imag


def ve_realf2(s1):
    return (Ve + s1*c.exp(1j*(pVe - 5*(c.pi)/6))).real


def ve_imagf2(s1):
    return (Ve + s1*c.exp(1j*(pVe - 5*(c.pi)/6))).imag


# En el tiempo t
def v(t1):
    return [(Vo*c.exp(1j*(w*element + pVo))).imag for element in t1]


def current(t1):
    return [((Vo/modulo_Z)*c.exp(1j*(w*element + pIo))).imag for element in t1]


def q(t1):
    return [((Vo/modulo_Z)*(-1/w)*c.cos(w*element + pIo)).real for element in t1]


fig, ax = plt.subplots()
ax.plot(v_real(s), v_imag(s), 'b-')
ax.plot(v_realf1(s1), v_imagf1(s1), 'b-')
ax.plot(v_realf2(s1), v_imagf2(s1), 'b-')

ax.plot(i_real(s), i_imag(s), 'r-')
ax.plot(i_realf1(s1), i_imagf1(s1), 'r-')
ax.plot(i_realf2(s1), i_imagf2(s1), 'r-')

ax.plot(z_real(s), z_imag(s), 'g-')
ax.plot(z_realf1(s1), z_imagf1(s1), 'g-')
ax.plot(z_realf2(s1), z_imagf2(s1), 'g-')

ax.plot(ve_real(s), ve_imag(s), 'm-')
ax.plot(ve_realf1(s1), ve_imagf1(s1), 'm-')
ax.plot(ve_realf2(s1), ve_imagf2(s1), 'm-')

ax.set_xlabel('Real')
ax.set_ylabel('Imaginario')
ax.set_title('Voltaje: Azul;  Corriente: Rojo;  Impedancia: Verde;  Ve: Magenta')
ax.grid(True)
plt.show()


print('-' * 30)
print("Fasor giratorio")
print(f'V(t): {Vo}*sin({w}*t)')
print(f'I(t): {(Vo / modulo_Z):.2f}*sin({w:.2f}*t + {pIo:.2f})')
print(f'Q(t): -{(Vo / (modulo_Z * w)):.2f}*cos({w:.2f}*t + {pIo:.2f})')

fig, axs = plt.subplots()
axs.plot(t1, v(t1), 'b-')
axs.plot(t1, current(t1), 'r-')
axs.plot(t1, q(t1), 'k-')

axs.set_xlabel('t')
axs.set_ylabel('V(t), I(t), Q(t)')
axs.set_title('Voltaje: Azul;  Corriente: Rojo;  Carga: Negro')
axs.grid(True)
plt.show()
