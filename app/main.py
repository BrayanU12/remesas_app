import streamlit as st
import auth
import remesas
import admin

def main():
    st.sidebar.title("Navegación")

    if "usuario" not in st.session_state:
        menu = st.sidebar.selectbox("Menú", ["Iniciar sesión", "Registrarse"])
        if menu == "Iniciar sesión":
            auth.login()
        else:
            auth.registro_usuario()
    else:
        st.sidebar.write(f"Usuario: {st.session_state.usuario}")
        if st.sidebar.button("Cerrar sesión"):
            st.session_state.clear()
            st.success("Sesión cerrada. Usa el menú para volver a iniciar sesión.")

        if st.session_state.rol == "admin":
            admin.mostrar_panel_admin()
        else:
            remesas.mostrar_panel_usuario()

if __name__ == "__main__":
    main()
