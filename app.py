import streamlit as st
st.image("Captura de pantalla 2025-04-22 123200.png")
# Constante universal de los gases ideales
R = 0.0821  # L·atm/mol·K

st.title("Calculadora de la Ecuación de los Gases Ideales")
st.write("Usa la ecuación: PV = nRT")

# Selección del valor a calcular
opcion = st.selectbox(
    "¿Qué variable deseas calcular?",
    ("Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)")
)

if opcion == "Presión (P)":
    V = st.number_input("Volumen (L)", min_value=0.001, step=0.1)
    T = st.number_input("Temperatura (K)", min_value=0.001, step=1.0)
    n = st.number_input("Número de moles (mol)", min_value=0.001, step=0.1)
    if st.button("Calcular presión"):
        P = (n * R * T) / V
        st.success(f"La presión es {P:.3f} atm")

elif opcion == "Volumen (V)":
    P = st.number_input("Presión (atm)", min_value=0.001, step=0.1)
    T = st.number_input("Temperatura (K)", min_value=0.001, step=1.0)
    n = st.number_input("Número de moles (mol)", min_value=0.001, step=0.1)
    if st.button("Calcular volumen"):
        V = (n * R * T) / P
        st.success(f"El volumen es {V:.3f} L")

elif opcion == "Temperatura (T)":
    P = st.number_input("Presión (atm)", min_value=0.001, step=0.1)
    V = st.number_input("Volumen (L)", min_value=0.001, step=0.1)
    n = st.number_input("Número de moles (mol)", min_value=0.001, step=0.1)
    if st.button("Calcular temperatura"):
        T = (P * V) / (n * R)
        st.success(f"La temperatura es {T:.2f} K")

elif opcion == "Número de moles (n)":
    P = st.number_input("Presión (atm)", min_value=0.001, step=0.1)
    V = st.number_input("Volumen (L)", min_value=0.001, step=0.1)
    T = st.number_input("Temperatura (K)", min_value=0.001, step=1.0)
    if st.button("Calcular número de moles"):
        n = (P * V) / (R * T)
        st.success(f"El número de moles es {n:.4f} mol")
