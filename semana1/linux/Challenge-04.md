# Desafio 04 - Conteúdo de Arquivos

[< Desafio Anterior](./Challenge-03.md) - **[Home](../README.md)** - [Próximo Desafio >](./Challenge-05.md)

## Descrição

Neste desafio, vamos aprender sobre a manipulação de conteúdo de arquivos e descobrir como contar as linhas de um arquivo, exibir linhas específicas de um arquivo e muito mais.

- Exiba as 10 primeiras linhas de `/etc/resolv.conf`
- Exiba as 5 últimas linhas de `/etc/crontab`
- Crie um arquivo chamado `count.log` com o seguinte conteúdo:
    Um<br>
    Dois<br>
    Três<br>
    Quatro<br>
    Cinco
- Use `cp` para fazer um backup deste arquivo chamado `count.bkp`
- Use `cat` para fazer um backup deste arquivo, salvando como `cat-count.log`
- Exiba o conteúdo de `cat-count.log`, com todas as linhas em ordem reversa
- Use `more` para exibir o arquivo `/etc/selinux/semanage.conf`
- Use `ls` para encontrar o maior arquivo em `/var/log`

## Critério de Sucesso

1. Mostre o conteúdo das 10 primeiras linhas de `/etc/resolv.conf`
2. Mostre as 5 últimas linhas de `/etc/crontab`
3. Valide se o conteúdo do arquivo `count.log` foi criado conforme o esperado
4. Verifique se o arquivo `count.bkp` foi criado
5. Verifique se o arquivo `cat-count.log` foi criado
6. Confirme se você pode ver o conteúdo do arquivo `cat-count.log` em ordem reversa
7. Valide se você conseguiu visualizar o conteúdo do arquivo `/etc/selinux/semanage.conf` paginado
8. Verifique se você pode ver o maior arquivo em `/var/log` no topo da lista

## Recursos de Aprendizado

- [O Shell](https://linuxjourney.com/lesson/the-shell)
