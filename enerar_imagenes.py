# generar_imagenes.py
import os
import numpy as np
import matplotlib.pyplot as plt
from campo_estatico_mdf.solver import LaplaceSolver2D

# ======================================================================
# CONFIGURACIÓN DE DIRECTORIO DE SALIDA
# ======================================================================

OUTPUT_DIR = "docs/_static/examples/"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ======================================================================
# FUNCIÓN AUXILIAR PARA GUARDAR IMÁGENES
# ======================================================================

def guardar_figura(nombre):
    ruta = os.path.join(OUTPUT_DIR, nombre)
    plt.savefig(ruta, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[OK] Imagen generada: {ruta}")


# ======================================================================
# CASO 1: Potencial trivial (todo en cero)
# ======================================================================

def generar_caso_trivial():
    solver = LaplaceSolver2D(N=30, V_izq=0, V_der=0, V_sup=0, V_inf=0)
    solver.aplicar_condiciones_contorno()
    V, _, _ = solver.resolver_gauss_seidel()

    plt.imshow(V, cmap="viridis", origin="lower")
    plt.colorbar(label="Potencial (V)")
    plt.title("Caso trivial: potencia nulo")
    guardar_figura("caso_trivial.png")


# ======================================================================
# CASO 2: Frontera izquierda a 10 V
# ======================================================================

def generar_caso_lateral_10V():
    solver = LaplaceSolver2D(N=30, V_izq=10, V_der=0, V_sup=0, V_inf=0)
    solver.aplicar_condiciones_contorno()
    V, _, _ = solver.resolver_gauss_seidel()

    plt.imshow(V, cmap="viridis", origin="lower")
    plt.colorbar(label="Potencial (V)")
    plt.title("Potencial con frontera izquierda a 10 V")
    guardar_figura("caso_lateral_10V.png")

    Ex, Ey = solver.calcular_campo_e()
    plt.figure()
    plt.quiver(-Ex, -Ey)
    plt.title("Campo eléctrico generado por frontera izquierda a 10 V")
    guardar_figura("campo_lateral_10V.png")


# ======================================================================
# CASO 3: Campo lineal constante
# ======================================================================

def generar_campo_lineal():
    N = 30
    V_izq, V_der = 10, 0

    solver = LaplaceSolver2D(N=N, V_izq=V_izq, V_der=V_der, V_sup=0, V_inf=0)

    lin = np.linspace(V_izq, V_der, N)
    solver.V = np.tile(lin, (N, 1))

    Ex, Ey = solver.calcular_campo_e()

    plt.figure(figsize=(5, 5))
    plt.quiver(-Ex, -Ey)
    plt.title("Campo eléctrico constante (potencial lineal)")
    guardar_figura("campo_lineal.png")


# ======================================================================
# CASO 4: Simetría (dos lados a 10 V)
# ======================================================================

def generar_caso_simetrico():
    solver = LaplaceSolver2D(N=40, V_izq=10, V_der=10, V_sup=0, V_inf=0)
    solver.aplicar_condiciones_contorno()
    V, _, _ = solver.resolver_gauss_seidel()

    plt.imshow(V, cmap="viridis", origin="lower")
    plt.colorbar(label="Potencial (V)")
    plt.title("Caso simétrico: lados izquierdo y derecho a 10 V")
    guardar_figura("caso_simetrico.png")


# ======================================================================
# CASO 5: Flujo completo (potencial + campo)
# ======================================================================

def generar_flujo_completo():
    solver = LaplaceSolver2D(
        N=50,
        V_izq=5,
        V_der=0,
        V_sup=3,
        V_inf=1
    )

    solver.aplicar_condiciones_contorno()
    V, _, _ = solver.resolver_gauss_seidel()
    Ex, Ey = solver.calcular_campo_e()

    plt.figure(figsize=(5, 5))
    plt.imshow(V, cmap="viridis", origin="lower")
    plt.colorbar(label="Potencial (V)")
    plt.title("Potencial final (flujo completo)")
    guardar_figura("flujo_completo.png")

    plt.figure(figsize=(5, 5))
    plt.quiver(-Ex, -Ey)
    plt.title("Campo eléctrico (flujo completo)")
    guardar_figura("flujo_completo_campo.png")


# ======================================================================
# EJECUCIÓN PRINCIPAL
# ======================================================================

if __name__ == "__main__":
    print("Generando imágenes...")

    generar_caso_trivial()
    generar_caso_lateral_10V()
    generar_campo_lineal()
    generar_caso_simetrico()
    generar_flujo_completo()

    print("Proceso completado.")
