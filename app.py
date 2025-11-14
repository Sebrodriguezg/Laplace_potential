# app.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from campo_estatico_mdf.solver import LaplaceSolver2D

st.set_page_config(layout="wide")

st.title("Solucionador de Campo Electrostático 2D")
st.write("""
Esta aplicación resuelve la ecuación de Laplace para encontrar el potencial y el campo eléctrico
en una región 2D con condiciones de contorno fijas.
""")

# --- Columnas para la configuración ---
col1, col2 = st.columns(2)

with col1:
    st.header("Configuración de la Simulación")
    N = st.slider("Tamaño de la malla (N x N)", min_value=10, max_value=100, value=30, step=5)
    tolerancia = st.number_input("Tolerancia de convergencia (ε)", min_value=1e-7, max_value=1e-3, value=1e-5, format="%.7f")

    metodo = st.selectbox(
            "Método de Resolución",
            ("Gauss-Seidel", "Jacobi")
    )

with col2:
    st.header("Condiciones de Contorno (Voltaje)")
    V_izq = st.number_input("Frontera Izquierda (V)", value=10.0)
    V_der = st.number_input("Frontera Derecha (V)", value=0.0)
    V_sup = st.number_input("Frontera Superior (V)", value=0.0)
    V_inf = st.number_input("Frontera Inferior (V)", value=0.0)

# --- Botón para ejecutar la simulación ---
if st.button("Resolver y Visualizar"):

    # --- Ejecutar el backend ---
    with st.spinner("Calculando... Esto puede tardar unos segundos."):
        solver = LaplaceSolver2D(N, V_izq, V_der, V_sup, V_inf, tolerancia)
        solver.aplicar_condiciones_contorno()

        if "Jacobi" in metodo:
            V, iteraciones, historial_error = solver.resolver_jacobi()
        else:
            V, iteraciones, historial_error = solver.resolver_gauss_seidel()

        Ex, Ey = solver.calcular_campo_e()


    st.success(f"¡Convergencia alcanzada en {iteraciones} iteraciones con metodo {metodo}!")

    # --- Visualización de resultados ---
    st.header("Resultados de la Simulación")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

    # 1. Heatmap del Potencial
    im = ax1.imshow(V, cmap='viridis', origin='lower')
    fig.colorbar(im, ax=ax1, label='Potencial (V)')
    ax1.set_title('Mapa de Potencial V(x,y)')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')

    # 2. Quiver Plot del Campo Eléctrico
    # Reducimos la densidad de las flechas para una mejor visualización
    skip = max(1, N // 15)
    x = np.arange(N)
    y = np.arange(N)
    ax2.quiver(x[::skip], y[::skip], Ex[::skip, ::skip], Ey[::skip, ::skip], scale=None, scale_units='xy', color='r')
    ax2.set_title('Campo Eléctrico E(x,y)')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_aspect('equal', adjustable='box')

    st.pyplot(fig)

    st.header("Evolución del Error de Convergencia")

    fig_err, ax_err = plt.subplots(figsize=(10,4))
    ax_err.semilogy(historial_error)
    ax_err.set_xlabel('Iteración')
    ax_err.set_ylabel('Error (escala log)')
    ax_err.set_title('Error máximo por iteración')

    st.pyplot(fig_err)

