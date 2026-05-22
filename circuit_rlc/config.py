"""
config.py — Parámetros del circuito RLC serie.
Modifica estos valores para explorar diferentes configuraciones.
"""

# ── Fuente de voltaje ──────────────────────────────────────────────────────────
Vo  = 10        # Amplitud del voltaje [V]
pVo = 0         # Fase inicial del voltaje [rad]
w   = 4         # Frecuencia angular [rad/s]

# ── Componentes del circuito ───────────────────────────────────────────────────
R = 2           # Resistencia [Ω]
L = 1 / 4       # Inductancia [H]
C = 1 / 8       # Capacitancia [F]

# ── Visualización ─────────────────────────────────────────────────────────────
T_CICLOS  = 2          # Número de ciclos a graficar en el dominio del tiempo
N_PUNTOS  = 500        # Resolución de las curvas temporales
ARROW_LEN = 0.30       # Longitud relativa de las cabezas de flecha en fasores