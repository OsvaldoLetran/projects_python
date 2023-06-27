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
def Vr(s):
    return (s*Vo).real


def Vi(s):
    return (s*Vo).imag


def Vrf1(s1):
    return (Vo + s1*c.exp(1j*(pVo + 5*(c.pi)/6))).real


def Vif1(s1):
    return (Vo + s1*c.exp(1j*(pVo + 5*(c.pi)/6))).imag


def Vrf2(s1):
    return (Vo + s1*c.exp(1j*(pVo -5*(c.pi)/6))).real


def Vif2(s1):
    return (Vo + s1*c.exp(1j*(pVo -5*(c.pi)/6))).imag


def Ir(s):
    return (s*Io).real


def Ii(s):
    return (s*Io).imag


def Irf1(s1):
    return (Io + s1*c.exp(1j*(pIo + 5*(c.pi)/6))).real


def Iif1(s1):
    return (Io + s1*c.exp(1j*(pIo + 5*(c.pi)/6))).imag


def Irf2(s1):
    return (Io + s1*c.exp(1j*(pIo - 5*(c.pi)/6))).real


def Iif2(s1):
    return (Io + s1*c.exp(1j*(pIo - 5*(c.pi)/6))).imag


def Zr(s):
    return (s*Z).real


def Zi(s):
    return (s*Z).imag


def Zrf1(s1):
    return (Z + s1*c.exp(1j*(pZ + 5*(c.pi)/6))).real


def Zif1(s1):
    return (Z + s1*c.exp(1j*(pZ + 5*(c.pi)/6))).imag


def Zrf2(s1):
    return (Z + s1*c.exp(1j*(pZ - 5*(c.pi)/6))).real


def Zif2(s1):
    return (Z + s1*c.exp(1j*(pZ - 5*(c.pi)/6))).imag


def Ver(s):
    return (s*Ve).real


def Vei(s):
    return (s*Ve).imag


def Verf1(s1):
    return (Ve + s1*c.exp(1j*(pVe + 5*(c.pi)/6))).real


def Veif1(s1):
    return (Ve + s1*c.exp(1j*(pVe + 5*(c.pi)/6))).imag


def Verf2(s1):
    return (Ve + s1*c.exp(1j*(pVe - 5*(c.pi)/6))).real


def Veif2(s1):
    return (Ve + s1*c.exp(1j*(pVe - 5*(c.pi)/6))).imag


# En el tiempo t
def v(t1):
    return [(Vo*c.exp(1j*(w*element + pVo))).imag for element in t1]


def i(t1):
    return [((Vo/modulo_Z)*c.exp(1j*(w*element + pIo))).imag for element in t1]


def q(t1):
    return [((Vo/modulo_Z)*(-1/w)*c.cos(w*element + pIo)).real for element in t1]


fig, ax = plt.subplots()
ax.plot(Vr(s), Vi(s), 'b-')
ax.plot(Vrf1(s1), Vif1(s1), 'b-')
ax.plot(Vrf2(s1), Vif2(s1), 'b-')

ax.plot(Ir(s), Ii(s), 'r-')
ax.plot(Irf1(s1), Iif1(s1), 'r-')
ax.plot(Irf2(s1), Iif2(s1), 'r-')

ax.plot(Zr(s), Zi(s), 'g-')
ax.plot(Zrf1(s1), Zif1(s1), 'g-')
ax.plot(Zrf2(s1), Zif2(s1), 'g-')

ax.plot(Ver(s), Vei(s), 'm-')
ax.plot(Verf1(s1), Veif1(s1), 'm-')
ax.plot(Verf2(s1), Veif2(s1), 'm-')

ax.set_xlabel('Real')
ax.set_ylabel('Imaginario')
ax.set_title('Voltaje: Azul;  Corriente: Rojo;  Impedancia: Verde;  Ve: Magenta')
ax.grid(True)
plt.show()


print('-' * 30)
print("Fasor giratorio")
print(f'V(t): {Vo}*sin({w}*t)')
print(f'I(t): {(Vo/modulo_Z):.2f}*sin({w:.2f}*t + {pIo:.2f})')
print(f'Q(t): -{(Vo / (modulo_Z * w)):.2f}*cos({w:.2f}*t + {pIo:.2f})')

fig, axs = plt.subplots()
axs.plot(t1, v(t1), 'b-')
axs.plot(t1, i(t1), 'r-')
axs.plot(t1, q(t1), 'k-')

axs.set_xlabel('t')
axs.set_ylabel('V(t), I(t), Q(t)')
axs.set_title('Voltaje: Azul;  Corriente: Rojo;  Carga: Negro')
axs.grid(True)
plt.show()
