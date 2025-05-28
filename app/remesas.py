import streamlit as st
import pandas as pd
from utils import cargar_datos_json, guardar_datos_json

REMESAS_FILE = "remesas.json"

def registrar_remesa():
    st.title("Registrar nueva remesa")
    monto = st.number_input("Monto a enviar", min_value=1.0)
    moneda = st.selectbox("Moneda fiat de origen", ["COP", "USD", "EUR", "MXN"])
    pais_origen = st.selectbox("Desde dónde envías", ["Colombia", "México", "USA", "España"])
    pais_destino = st.selectbox("A dónde quieres enviar", ["Colombia", "México", "USA", "España"])

    if st.button("Enviar remesa"):
        remesas = cargar_datos_json(REMESAS_FILE)
        if remesas.empty:
            remesas = pd.DataFrame(columns=["usuario", "monto", "moneda", "origen", "destino", "estado", "id"])

        nueva = pd.DataFrame([{
            "usuario": st.session_state.usuario,
            "monto": monto,
            "moneda": moneda,
            "origen": pais_origen,
            "destino": pais_destino,
            "estado": "Pendiente",
            "id": len(remesas) + 1
        }])
        remesas = pd.concat([remesas, nueva], ignore_index=True)
        guardar_datos_json(remesas, REMESAS_FILE)
        st.success("Remesa registrada correctamente.")

def mostrar_panel_usuario():
    st.title(f"Panel de usuario: {st.session_state.usuario}")
    registrar_remesa()
    remesas = cargar_datos_json(REMESAS_FILE)
    if not remesas:
        st.info("No hay remesas registradas.")
        return
    remesas_usuario = remesas[remesas["usuario"] == st.session_state.usuario]
    if remesas_usuario.empty:
        st.info("Aún no tienes remesas registradas.")
        return
    st.write("Tus remesas:")
    st.dataframe(remesas_usuario)
