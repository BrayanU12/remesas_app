import streamlit as st
import pandas as pd
from utils import cargar_datos_json, guardar_datos_json

REMESAS_FILE = "remesas.json"

def mostrar_panel_admin():
    st.title("Panel de Administrador")
    remesas = cargar_datos_json(REMESAS_FILE)
    if remesas.empty:
        st.info("No hay remesas registradas.")
        return

    for i, remesa in remesas.iterrows():
        st.markdown("---")
        st.write(f"Remesa #{remesa['id']} - Usuario: {remesa['usuario']}")
        st.write(f"Monto: {remesa['monto']} {remesa['moneda']}")
        st.write(f"Desde: {remesa['origen']} → Hacia: {remesa['destino']}")

        estados = ["Pendiente", "Procesada", "Cancelada"]
        estado_actual = remesa.get("estado", "Pendiente")

        try:
            nuevo_estado = st.radio("Estado:", estados, index=estados.index(estado_actual), key=remesa["id"])
        except ValueError:
            nuevo_estado = st.radio("Estado:", estados, index=0, key=remesa["id"])

        if nuevo_estado != remesa["estado"]:
            remesas.at[i, "estado"] = nuevo_estado

    if st.button("Guardar cambios"):
        guardar_datos_json(remesas, REMESAS_FILE)
        st.success("Cambios guardados.")
