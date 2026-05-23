"""
circuito_rlc.py — Análisis fasorial y temporal de un circuito RLC serie.

Uso:
    from circuito_rlc import CircuitoRLC
    c = CircuitoRLC(Vo = 10, w = 4, R = 2, L = 0.25, C = 0.125)
    c.resumen()
"""

import cmath
import numpy as np
from sympy import symbols, Function, dsolve, exp as sym_exp


class CircuitoRLC:
    """Circuito RLC serie excitado con una fuente sinusoidal."""

    # ── Constructor ────────────────────────────────────────────────────────────
    def __init__(self, Vo: float, w: float, R: float, L: float, C: float,
                pVo: float = 0.0):
        self.Vo  = Vo
        self.pVo = pVo
        self.w   = w
        self.R   = R
        self.L   = L
        self.C   = C
        self._calcular()

    # ── Cálculos fasores ───────────────────────────────────────────────────────
    def _calcular(self):
        w, R, L, C = self.w, self.R, self.L, self.C
        Vo, pVo    = self.Vo, self.pVo

        # Impedancia compleja
        self.Z        = R + 1j * w * L - 1j / (w * C)
        self.modulo_Z = abs(self.Z)
        self.fase_Z   = cmath.phase(self.Z)

        # Corriente fasorial
        self.Io        = Vo / self.Z
        self.modulo_Io = abs(self.Io)
        self.fase_Io   = cmath.phase(self.Io)

        # Tensión equivalente (fasorial compuesta)
        self.Ve        = Vo + 1j * self.Z
        self.modulo_Ve = abs(self.Ve)
        self.fase_Ve   = cmath.phase(self.Ve)

        # Reactancias individuales
        self.X_L = w * L
        self.X_C = 1 / (w * C)
        self.X   = self.X_L - self.X_C          # Reactancia neta

        # Factor de potencia y ángulo de desfase
        self.cos_phi = R / self.modulo_Z         # Factor de potencia
        self.phi     = cmath.phase(self.Z)       # Ángulo de desfase V-I

        # Frecuencia de resonancia
        self.w0 = 1 / np.sqrt(L * C)

        # Factor de calidad Q y ancho de banda BW
        self.Q  = self.w0 * L / R
        self.BW = R / L

    # ── Señales en el tiempo ───────────────────────────────────────────────────
    def voltaje(self, t: np.ndarray) -> np.ndarray:
        """v(t) = Vo · sin(wt + pVo)"""
        return self.Vo * np.sin(self.w * t + self.pVo)

    def corriente(self, t: np.ndarray) -> np.ndarray:
        """i(t) = Io · sin(wt + phi_I)"""
        return self.modulo_Io * np.sin(self.w * t + self.fase_Io)

    def carga(self, t: np.ndarray) -> np.ndarray:
        """q(t) = -Io/w · cos(wt + phi_I)"""
        return -(self.modulo_Io / self.w) * np.cos(self.w * t + self.fase_Io)

    def potencia_instantanea(self, t: np.ndarray) -> np.ndarray:
        """p(t) = v(t) · i(t)"""
        return self.voltaje(t) * self.corriente(t)

    # ── Ecuación diferencial de corriente ─────────────────────────────────────────
    def ecuacion_diferencial(self, mostrar: bool = True):
        t = symbols('t')    # definimos variable
        i = Function('i')(t)    # definimos Funcion
        ip  = i.diff(t)
        ipp = ip.diff(t)
        eq  = self.L * ipp + self.R * ip + (1 / self.C) * i
            #-Vo*sin(w*t + pVo)    # definimos la ED
        sol = dsolve(eq, i)
        if mostrar:
            print("Ecuación diferencial homogénea (i): ")
            print(f"  {eq} = 0")
            print("Solución general: ")
            print(f"  {sol}")
        return eq, sol

    # ── Resumen en consola ─────────────────────────────────────────────────────
    def resumen(self):
        sep = "─" * 46
        print(sep)
        print(" CIRCUITO RLC SERIE — Análisis fasorial")
        print(sep)
        print(f" Parámetros : R = {self.R} Ω , L = {self.L} H , C = {self.C} F")
        print(f" Fuente     : {self.Vo} V · sin({self.w}·t + {self.pVo:.3f})")
        print(sep)
        print(f"  {'Fasor':<12} {'Módulo':>10} {'Fase (°)':>10}")
        print(f"  {'Impedancia':<12} {self.modulo_Z:>10.4f} {np.degrees(self.fase_Z):>10.4f}")
        print(f"  {'Voltaje':<12} {self.Vo:>10.4f} {np.degrees(self.pVo):>10.4f}")
        print(f"  {'Corriente':<12} {self.modulo_Io:>10.4f} {np.degrees(self.fase_Io):>10.4f}")
        print(f"  {'Ve':<12} {self.modulo_Ve:>10.4f} {np.degrees(self.fase_Ve):>10.4f}")
        print(sep)
        print(f"  Reactancia inductiva  X_L = {self.X_L:.4f} Ω")
        print(f"  Reactancia capacitiva X_C = {self.X_C:.4f} Ω")
        print(f"  Reactancia neta       X   = {self.X:.4f} Ω")
        print(f"  Factor de potencia cos<phi> = {self.cos_phi:.4f}")
        print(sep)
        print(f"  Frecuencia de resonancia w_o = {self.w0:.4f} rad/s")
        print(f"  Factor de calidad        Q   = {self.Q:.4f}")
        print(f"  Ancho de banda           BW  = {self.BW:.4f} rad/s")
        print(sep)
        print(f"  v(t) = {self.Vo:.3f} · sin({self.w}·t)")
        print(f"  i(t) = {self.modulo_Io:.4f} · sin({self.w}·t + {self.fase_Io:.4f})")
        print(f"  q(t) = {-(self.modulo_Io/self.w):.4f} · cos({self.w}·t + {self.fase_Io:.4f})")
        print(sep)


# ── Ejecución directa ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    import config
    circuito = CircuitoRLC(
        Vo = config.Vo, w = config.w, R = config.R, L = config.L, C = config.C, pVo = config.pVo
    )
    circuito.resumen()
    circuito.ecuacion_diferencial()