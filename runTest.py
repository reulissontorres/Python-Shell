from subprocess import PIPE, run

comando = ["man", "whoami"]
execucao = run(comando, stdout=PIPE, stderr=PIPE)
print(execucao)


'''
Comandos para teste

- whoami - ok
- man whoami - ok
- clear -ok
- pwd -ok
- cd /home/runner/diretorio - ok

'''