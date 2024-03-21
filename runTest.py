from subprocess import PIPE, run

comando = ["cd", "diretorio"]

execucao = run(comando, stdout=PIPE, stderr=PIPE)

print(execucao.stdout.decode('utf-8'))
print(execucao.stderr)



'''
Comandos para teste

- whoami - ok
- man whoami - ok
- clear -ok
- pwd -ok
- cd /home/runner/diretorio - ok

'''