"""
graficas.py — Visualizaciones del circuito RLC serie.

Genera 3 figuras:
  1. Diagrama fasorial (con flechas reales usando Axes.annotate)
  2. Señales en el tiempo: v(t), i(t), q(t) y p(t)
  3. Diagrama de Bode simplificado: |Z(ω)| y φ(ω)

Uso:
    python graficas.py
"""

import cmath
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec

import config
from circuit_rlc import CircuitoRLC

# ── Estilo global ──────────────────────────────────────────────────────────────
plt.rcParams.update({
    "figure.facecolor":  "#0f1117",
    "axes.facecolor":    "#0f1117",
    "axes.edgecolor":    "#444",
    "axes.labelcolor":   "#ccc",
    "xtick.color":       "#888",
    "ytick.color":       "#888",
    "grid.color":        "#2a2a2a",
    "grid.linestyle":    "--",
    "text.color":        "#ddd",
    "font.family":       "monospace",
})

COLORES = {
    "voltaje":    "#4fc3f7",   # azul claro
    "corriente":  "#ef5350",   # rojo
    "carga":      "#66bb6a",   # verde
    "potencia":   "#ffa726",   # naranja
    "impedancia": "#ab47bc",   # púrpura
    "Ve":         "#ec407a",   # rosa
}


def _flecha(ax, origen, destino, color, label, lw = 2):
    """Dibuja una flecha de fasor con etiqueta."""
    ax.annotate(
        "", xy = destino, xytext = origen,
        arrowprops = dict(arrowstyle = "-|>", color = color, lw = lw,
                        mutation_scale = 15),
    )
    # Etiqueta en el punto medio
    mx = (origen[0] + destino[0]) / 2
    my = (origen[1] + destino[1]) / 2
    ax.text(mx, my, f" {label}", color = color, fontsize = 9,
            va = "center", ha = "left")


# ═══════════════════════════════════════════════════════════════════════════════
# 1. DIAGRAMA FASORIAL
# ═══════════════════════════════════════════════════════════════════════════════
def grafica_fasores(circ: CircuitoRLC):
    fig, ax = plt.subplots(figsize = (7, 7))
    fig.suptitle("Diagrama Fasorial — RLC Serie", fontsize = 13, color = "#eee", y = 0.97)

    fasores = {
        "V":  (circ.Vo,        circ.pVo,     COLORES["voltaje"]),
        "I":  (circ.modulo_Io, circ.fase_Io, COLORES["corriente"]),
        "Z":  (circ.modulo_Z,  circ.fase_Z,  COLORES["impedancia"]),
        "Ve": (circ.modulo_Ve, circ.fase_Ve, COLORES["Ve"]),
    }

    for nombre, (mod, fase, color) in fasores.items():
        dx = mod * np.cos(fase)
        dy = mod * np.sin(fase)
        _flecha(ax, (0, 0), (dx, dy), color, nombre, lw = 2.2)

    # Círculo de referencia (radio = Vo)
    theta = np.linspace(0, 2 * np.pi, 300)
    ax.plot(circ.Vo * np.cos(theta), circ.Vo * np.sin(theta),
            color = "#333", lw = 1, ls = ":")

    ax.axhline(0, color="#555", lw = 0.8)
    ax.axvline(0, color="#555", lw = 0.8)
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginario")
    ax.set_aspect("equal")
    ax.grid(True)

    parches = [mpatches.Patch(color = v[2], label = k) for k, v in fasores.items()]
    ax.legend(handles = parches, loc = "upper right", framealpha = 0.15)

    plt.tight_layout()
    return fig


# ═══════════════════════════════════════════════════════════════════════════════
# 2. SEÑALES EN EL TIEMPO
# ═══════════════════════════════════════════════════════════════════════════════
def grafica_tiempo(circ: CircuitoRLC):
    T = 2 * np.pi / circ.w                              # Período
    t = np.linspace(0, config.T_CICLOS * T, config.N_PUNTOS)

    v = circ.voltaje(t)
    i = circ.corriente(t)
    q = circ.carga(t)
    p = circ.potencia_instantanea(t)

    fig = plt.figure(figsize = (12, 8), layout = "constrained")
    fig.suptitle("Señales en el tiempo — RLC Serie", fontsize = 13,
                 color = "#eee", y = 0.98)

    gs = GridSpec(2, 2, figure = fig, hspace = 0.45, wspace = 0.35)
    axes_data = [
        (gs[0, 0], v, COLORES["voltaje"],    "v(t)  [V]",    "Voltaje"),
        (gs[0, 1], i, COLORES["corriente"],  "i(t)  [A]",    "Corriente"),
        (gs[1, 0], q, COLORES["carga"],      "q(t)  [C]",    "Carga"),
        (gs[1, 1], p, COLORES["potencia"],   "p(t)  [W]",    "Potencia"),
    ]

    for spec, señal, color, ylabel, titulo in axes_data:
        ax = fig.add_subplot(spec)
        ax.plot(t, señal, color = color, lw = 1.8)
        ax.axhline(0, color = "#555", lw = 0.7)
        # Línea punteada del promedio (solo para potencia)
        if titulo == "Potencia":
            prom = np.mean(señal)
            ax.axhline(prom, color = "#ffa726", lw = 1, ls = "--",
                       label = f"<p> = {prom:.2f} W")
            ax.legend(fontsize = 8, framealpha = 0.2)
        ax.set_title(titulo, color = color, fontsize = 10)
        ax.set_xlabel("t [s]", fontsize = 8)
        ax.set_ylabel(ylabel, fontsize = 8)
        ax.grid(True)

    return fig


# ═══════════════════════════════════════════════════════════════════════════════
# 3. DIAGRAMA DE BODE (|Z| y fase)
# ═══════════════════════════════════════════════════════════════════════════════
def grafica_bode(circ: CircuitoRLC):
    w_arr = np.logspace(-1, 3, 600)
    Z_arr = circ.R + 1j * w_arr * circ.L - 1j / (w_arr * circ.C)
    modZ  = np.abs(Z_arr)
    faseZ = np.degrees(np.angle(Z_arr))

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (9, 6), sharex = True)
    fig.suptitle("Diagrama de Bode — Impedancia Z(ω)", fontsize = 13,
                 color = "#eee", y = 0.98)

    # Módulo
    ax1.semilogx(w_arr, 20 * np.log10(modZ),
                 color = COLORES["impedancia"], lw = 2)
    ax1.axvline(circ.w0, color = "#ffa726", lw = 1.2, ls = "--",
                label = f"ω₀ = {circ.w0:.2f} rad/s")
    ax1.axvline(circ.w,  color = "#4fc3f7", lw = 1.2, ls = ":",
                label = f"ω  = {circ.w} rad/s")
    ax1.set_ylabel("|Z(ω)|  [dB Ω]")
    ax1.legend(fontsize = 9, framealpha = 0.2)
    ax1.grid(True, which = "both")

    # Fase
    ax2.semilogx(w_arr, faseZ, color = COLORES["Ve"], lw = 2)
    ax2.axvline(circ.w0, color = "#ffa726", lw = 1.2, ls = "--")
    ax2.axvline(circ.w,  color = "#4fc3f7", lw = 1.2, ls = ":")
    ax2.axhline(0, color = "#555", lw = 0.8)
    ax2.set_ylabel("∠Z(ω)  [°]")
    ax2.set_xlabel("ω  [rad/s]")
    ax2.grid(True, which = "both")

    plt.tight_layout()
    return fig


# ── Main ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    circ = CircuitoRLC(
        Vo = config.Vo, w = config.w, R = config.R,
        L = config.L, C = config.C, pVo = config.pVo,
    )
    circ.resumen()

    fig1 = grafica_fasores(circ)
    fig2 = grafica_tiempo(circ)
    fig3 = grafica_bode(circ)

    #plt.show()
    fig1.savefig("grafica1.png", dpi = 150)
    fig2.savefig("grafica2.png", dpi = 150)
    fig3.savefig("grafica3.png", dpi = 150)