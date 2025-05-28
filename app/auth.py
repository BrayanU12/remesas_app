import streamlit as st
import os
import json
from utils import cargar_datos_json, guardar_datos_json

usuarios_file = "data/usuarios.json"

def login():
    st.subheader("Iniciar Sesión")
    username = st.text_input("Nombre de usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión"):
        usuarios = cargar_datos_json(usuarios_file)
        usuario = next((u for u in usuarios if u["username"] == username), None)

        if usuario and usuario["password"] == password:
            st.session_state.usuario = usuario["username"]
            st.session_state.rol = usuario["rol"]
            st.success("Sesión iniciada. Usa el menú de la izquierda.")
        else:
            st.error("Usuario o contraseña incorrectos")

def registro_usuario():
    st.subheader("Registrarse")
    username = st.text_input("Elige un nombre de usuario")
    password = st.text_input("Elige una contraseña", type="password")
    rol = st.selectbox("Selecciona tu rol", ["usuario", "admin"])

    if st.button("Registrarse"):
        usuarios = cargar_datos_json(usuarios_file)

        if any(u["username"] == username for u in usuarios):
            st.error("El nombre de usuario ya existe")
            return

        nuevo_usuario = {
            "username": username,
            "password": password,
            "rol": rol
        }
        usuarios.append(nuevo_usuario)
        guardar_datos_json(usuarios_file, usuarios)
        st.success("Usuario registrado. Ahora puedes iniciar sesión.")
