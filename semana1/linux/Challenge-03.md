# Desafio 03 - Manipulação de arquivos

[< Desafio Anterior](./Challenge-02.md) - **[Home](../README.md)** - [Próximo Desafio >](./Challenge-04.md)

## Descrição

Neste desafio, você aprenderá comandos básicos de manipulação de arquivos, como criar, renomear, encontrar e remover arquivos.

- Encontre no diretório `/var` todos os arquivos que foram modificados nos últimos 60 minutos
- Mostre o tipo de arquivo de `/bin/htop`, `/etc/passwd` e `/usr/bin/passwd`
- Vá para o diretório pessoal e faça o download do arquivo [azure-linux.svg](https://docs.microsoft.com/en-us/learn/achievements/azure-linux.svg) e [InfographicRC2.pdf](https://azure.microsoft.com/mediahandler/files/resourcefiles/infographic-reliability-with-microsoft-azure/InfographicRC2.pdf)
- Exiba o tipo de arquivo de `azure-linux.svg` e `InfographicRC2.pdf`
- Renomeie `azure-linux.svg` para `azure-linux.pdf`
- Exiba o tipo de arquivo de `azure-linux.pdf` e `InfographicRC2.pdf`
- Crie um diretório `~/lab` e entre nele.
- Crie o arquivo `today.log` e o arquivo `yesterday.log` em lab.
- Verifique a data e hora de criação
- Altere a data em `yesterday.log` para corresponder à data de ontem
- Verifique a data e hora de criação novamente
- Crie um diretório `~/mybackup` e copie todos os arquivos de `~/lab` para ele
- Use um comando para remover o diretório `~/mybackup` e todos os arquivos dentro dele
- Crie um diretório `~/logbackup` e copie os arquivos `*.log` de `/var/log` para ele
- Conte quantas vezes a palavra 'linux' aparece no arquivo `/etc/wgetrc`
- Conte quantas palavras existem no arquivo `/etc/hdparm.conf`

## Critério de Sucesso

1. Mostre todos os arquivos que foram modificados nos últimos 60 minutos dentro de `/var`
2. Certifique-se de verificar os diferentes tipos de arquivo dos arquivos `/bin/htop`, `/etc/passwd` e `/usr/bin/passwd`
3. Verifique se você conseguiu fazer o download dos arquivos [azure-linux.svg](https://docs.microsoft.com/en-us/learn/achievements/azure-linux.svg) e [azure-ops-guide.pdf](https://docsmsftpdfs.blob.core.windows.net/guides/azure/azure-ops-guide.pdf) com sucesso em seu diretório pessoal
4. Confirme os diferentes tipos de arquivo
5. Valide a renomeação de `azure-linux.svg` para `azure-linux.pdf`
6. Após a renomeação da extensão, verifique se o tipo do arquivo foi alterado
7. Certifique-se de que o diretório foi criado com sucesso e que você está dentro do diretório
8. Verifique se os arquivos foram criados corretamente dentro do diretório `~/lab`
9. Confirme a data e hora de criação de cada arquivo
10. Verifique se você alterou corretamente a data para a data de ontem
11. Confirme se a data e hora de criação foram definidas conforme o esperado
12. Valide se todos os arquivos de `~/lab` foram colocados com sucesso em `~/mybackup`
13. Certifique-se de que você conseguiu remover tudo usando apenas um comando
14. Mostre todos os arquivos de log copiados de `/var/log` para `~/logbackup`
15. Confirme quantas linhas existem em `/etc/wgetrc`
16. Confirme quantas palavras existem em `/etc/hdparm.conf`

## Recursos de Aprendizado

- [O Shell](https://linuxjourney.com/lesson/the-shell)
