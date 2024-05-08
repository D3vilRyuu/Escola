# 3- Crie um programa que simule um sistema de login. Configure em variáveis iniciais que reservem o e-mail e a
# senha correta. Em seguida peça ao usuário para informar o e-mail e senha de login. O programa deve bloquear
# caso o usuário passe de 3 tentativas erradas de login.
email_correto = "email@gmail.com"
senha_correta = "senha123"
tentativas_maximas = 3
tentativa = 0


while tentativa < tentativas_maximas:
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    if email == email_correto and senha == senha_correta:
        print("Login bem-sucedido!")
    else:
        print("E-mail ou senha incorretos. Tente novamente.")
        tentativa += 1

if tentativa == tentativas_maximas:
    print("Limite de tentativas excedido. Seu acesso foi bloqueado.")

            
            
