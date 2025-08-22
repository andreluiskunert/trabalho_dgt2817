# Microatividade 6 - função com parâmetro
def loginUsuario(perfil):
    if perfil.lower() == "admin":
        print("Bem-vindo, Administrador")
    else:
        print("Bem-vindo, Usuário")

# Chamadas de teste
loginUsuario("Admin")
loginUsuario("admin")
loginUsuario("User")
loginUsuario("usuário")
