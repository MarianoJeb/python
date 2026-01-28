#EXERCICIO 06|DICIONÁRIOS
""" Crie um sistema de login com dois dicionários: um que guarda as credenciais corretas, e outro dicionário que guarde as informações inseridas pelo usuário. Peça ao usuário para digitar o usuário e senha, e verifique se está correto de acordo com o primeiro dicionário.
Se o usuário e a senha estão corretos → "Login bem-sucedido"
Senão → "Usuário ou senha incorretos" """
correto={
    "login":"MARIANO_JEB",
    "senha":"Abc@123"
}
tentativa={
    'login':input("LOGIN:\n"),
    'senha':input('SENHA:\n')
}
if correto["login"]==tentativa["login"] and correto["senha"]==tentativa["senha"]:
    print('Login bem-sucedido')
else:
    print("Usuário ou senhas incorretos")