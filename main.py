import os
from subprocess import PIPE, run


def changeDirectory(comando):
  """
  Função que muda o diretório atual.
  """
  if len(comando) < 2:
    raise ValueError("Argumento de diretório ausente para cd")
  os.chdir(comando[1])
  print(f"Diretório alterado para {os.getcwd()}\n")


def man(comando):
  """
  Função que imprime o manual de um comando.
  """
  if len(comando) < 2:
    raise ValueError("Argumento de comando ausente para man")
  os.system(f"man {comando[1]}")


def pythonShell():
  while True:
    x = input(">>> ")
    if x == "exit()":
      break

    try:
      y = eval(x)
      if y:
        print(y)
    except Exception:
      try:
        exec(x)
      except Exception as e:
        print("Erro:", e)


while True:
  # Recupera o caminho completo do diretório
  dir_atual = os.getcwd()

  # Solicita a entrada do usuário e divide o comando digitado
  comando = input(f"C:{dir_atual}$ ").split()

  # Verifica se o usuário deseja sair do programa
  if 'exit' in comando:
    print('Saindo')
    break

  try:
    # Verifica se o comando é 'cd' para alterar diretórios
    if comando[0] == 'cd':
      changeDirectory(comando)
    
    # Verifica se é para limpar o terminal
    elif comando[0] == 'clear':
      os.system('clear')

    # Mostra o manual do comando
    elif comando[0] == 'man':
      man(comando)

    elif comando[0] == 'python' and len(comando) == 1:
      pythonShell()
    
    else:
      # Executa o comando usando o subprocess
      execucao = run(comando, stdout=PIPE, stderr=PIPE)
    
      # Imprime o resultado da execução
      print(execucao.stdout.decode('utf-8'))  
  except Exception as e:
    # Exibe quaisquer erros que ocorram durante a execução
    print(f'Erro de execução: {e}')
    