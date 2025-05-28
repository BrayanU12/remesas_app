import streamlit as st
import utils
from datetime import datetime


def mostrar_panel_usuario():
    st.header("Panel de Usuario")
    registrar_remesa()
    mostrar_historial_remesas()


def registrar_remesa():
    st.subheader("Registrar Nueva Remesa")

    monto = st.number_input("Monto a enviar", min_value=0.0, format="%.2f")
    pais_destino = st.selectbox("País de destino", ["Colombia", "México", "Perú", "Otro"])
    destinatario = st.text_input("Nombre del destinatario")

    if st.button("Enviar remesa"):
        if monto > 0 and destinatario:
            nueva_remesa = {
                "usuario": st.session_state.usuario,
                "monto": monto,
                "pais_destino": pais_destino,
                "destinatario": destinatario,
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            lista_remesas = utils.cargar_datos_json("data/remesas.json")
            lista_remesas.append(nueva_remesa)
            utils.guardar_datos_json("data/remesas.json", lista_remesas)
            st.success("Remesa registrada con éxito")
        else:
            st.warning("Por favor completa todos los campos correctamente.")


def mostrar_historial_remesas():
    st.subheader("Historial de Remesas")

    lista_remesas = utils.cargar_datos_json("data/remesas.json")
    remesas_usuario = [r for r in lista_remesas if r.get("usuario") == st.session_state.usuario]

    if not remesas_usuario:
        st.info("No hay remesas registradas aún.")
        return

    for remesa in remesas_usuario:
        st.write(f"""
        - **Fecha:** {remesa.get('fecha')}
        - **Destinatario:** {remesa.get('destinatario')}
        - **País:** {remesa.get('pais_destino')}
        - **Monto:** ${remesa.get('monto'):.2f}
        """)

