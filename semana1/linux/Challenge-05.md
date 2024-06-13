# Desafio 05 - Permissões de arquivos padrão

[< Desafio Anterior](./Challenge-04.md) - **[Home](../README.md)** - [Próximo Desafio >](./Challenge-06.md)

## Descrição

Neste desafio, você aprenderá sobre as permissões padrão de arquivos no Linux e entenderá como trabalhar com permissões de arquivos em um ambiente Linux.

- Como usuário regular (student), crie um diretório `~/permissions`
- Crie um arquivo chamado `myfile.txt` dentro do diretório `~/permissions`
- Liste as propriedades do arquivo `/var/log/waagent.log`. Em seguida, copie este arquivo para o seu diretório `permissions`
- Como root, crie um arquivo chamado `rootfile.txt` no diretório `/home/student/permissions`
- Como usuário regular (student), verifique quem é o proprietário deste arquivo criado pelo root
- Altere a propriedade de todos os arquivos no diretório `/home/student/permissions` para você mesmo (student)
- Certifique-se de que você (student) tenha todos os direitos nos arquivos dentro de `~`, e que os outros usuários só possam ler

## Critério de Sucesso

1. Verifique se o diretório foi criado com sucesso
2. Confirme o arquivo criado dentro do `~permissions`
3. Verifique o arquivo dentro do seu diretório `permissions`. Quem é o novo proprietário deste arquivo agora?
4. Verifique se você criou o arquivo como o usuário root no diretório `/home/student/permissions`
5. Certifique-se de estar logado como usuário regular (student), em seguida, verifique o proprietário do arquivo criado pelo usuário root
6. Valide se você foi capaz de alterar a propriedade de todos os arquivos no diretório `/home/student/permissions` para o usuário student
7. Confirme seus direitos dentro de `~`, e certifique-se de que outros usuários só possam ler

## Recursos de Aprendizado

- [Permissões de Arquivos](https://linuxjourney.com/lesson/file-permissions)
- [Compreendendo as Permissões de Arquivos no Linux](https://www.linuxfoundation.org/blog/classic-sysadmin-understanding-linux-file-permissions/)
- [Calculadora Chmod](https://chmod-calculator.com/)
- [Permissões de Arquivos no Linux](https://linuxhandbook.com/linux-file-permissions/)
- [Suid, Sgid e Sticky Bit](https://linuxhandbook.com/suid-sgid-sticky-bit/)
