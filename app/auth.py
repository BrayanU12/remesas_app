import streamlit as st
import pandas as pd
from utils import cargar_datos_json, guardar_datos_json

USUARIOS_FILE = "usuarios.json"

def login():
    st.title("Inicio de Sesión")
    usuario = st.text_input("Usuario")
    contrasena = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión"):
        usuarios = cargar_datos_json(USUARIOS_FILE)
        if usuarios.empty or "usuario" not in usuarios.columns:
            st.error("No hay usuarios registrados.")
            return

        user_data = usuarios[(usuarios["usuario"] == usuario) & (usuarios["contrasena"] == contrasena)]

        if not user_data.empty:
            st.session_state.usuario = usuario
            st.session_state.rol = "admin" if usuario == "admin" else "usuario"
            st.success(f"Bienvenido, {usuario}")
            st.experimental_rerun()
        else:
            st.error("Credenciales inválidas.")

def registro_usuario():
    st.title("Registro de Usuario")
    usuario = st.text_input("Usuario")
    correo = st.text_input("Correo")
    contrasena = st.text_input("Contraseña", type="password")

    if st.button("Registrarse"):
        usuarios = cargar_datos_json(USUARIOS_FILE)
        if usuarios.empty:
            usuarios = pd.DataFrame(columns=["usuario", "correo", "contrasena"])

        if "usuario" in usuarios.columns and usuario in usuarios["usuario"].values:
            st.error("Usuario ya registrado.")
        else:
            nuevo = pd.DataFrame([{
                "usuario": usuario,
                "correo": correo,
                "contrasena": contrasena
            }])
            usuarios = pd.concat([usuarios, nuevo], ignore_index=True)
            guardar_datos_json(usuarios, USUARIOS_FILE)
            st.success("Usuario registrado con éxito. Ahora inicia sesión.")
            st.experimental_rerun()
