# Linux Commands Cheat Sheet

O terminal de linha de comando no Linux é o componente mais poderoso do sistema operacional. No entanto, devido à quantidade de comandos disponíveis, pode ser intimidante para iniciantes. Mesmo usuários experientes podem esquecer um comando de vez em quando, e é por isso que criamos este guia de comandos de referência do Linux.

Nesta página, apresentaremos uma lista selecionada dos comandos mais úteis do Linux.

Observação: os comandos mencionados são para o Linux em geral, tanto distribuições baseadas em RedHat quanto em Debian. Existem alguns comandos na seção de gerenciamento de pacotes que podem ser específicos para sistemas baseados em RedHat, como yum e rpm, que não funcionam no Ubuntu (baseado em Debian).

## Comandos de Arquivo

| Comando | Descrição |
|--------------|--------------|
| `ls` | Listar arquivos no diretório |
| `ls -a` | Listar todos os arquivos (mostra arquivos ocultos) |
| `locate [nome]` | Encontrar todos os arquivos e diretórios relacionados a um nome específico |
| `pwd` | Mostrar o diretório em que você está trabalhando atualmente |
| `mkdir [diretório]` | Criar um novo diretório |
| `rm [nome_arquivo]` | Remover um arquivo |
| `rm -r [nome_diretório]` | Remover um diretório recursivamente |
| `rm -rf [nome_diretório]` | Remover um diretório recursivamente sem confirmar |
| `cp [nome_arquivo1] [nome_arquivo2]` | Copiar o conteúdo de um arquivo para outro |
| `cp -r [nome_diretório1] [nome_diretório2]` | Copiar recursivamente o conteúdo de um arquivo para outro |
| `mv [nome_arquivo1] [nome_arquivo2]` | Renomear [nome_arquivo1] para [nome_arquivo2] com o comando |
| `ln -s /caminho/para/[nome_arquivo] [nome_link]` | Criar um link simbólico para um arquivo |
| `touch [nome_arquivo]` | Criar um novo arquivo usando o touch |
| `more [nome_arquivo]` | Mostrar o conteúdo de um arquivo |
| `cat [nome_arquivo]` | ou use o comando cat |
| `cat [nome_arquivo1] >> [nome_arquivo2]` | Acrescentar o conteúdo do arquivo a outro arquivo |
| `head [nome_arquivo]` | Exibir as primeiras 10 linhas de um arquivo com o comando head |
| `tail [nome_arquivo]` | Mostrar as últimas 10 linhas de um arquivo |
| `wc` | Mostrar o número de palavras, linhas e bytes em um arquivo usando wc |
| `ls | xargs wc` | Listar o número de linhas/palavras/caracteres em cada arquivo em um diretório com o comando xargs |
| `cut -d[delimitador] [nome_arquivo]` | Cortar uma seção de um arquivo e imprimir o resultado na saída padrão |
| `[dados] | cut -d[delimitador]` | Cortar uma seção de dados encadeados e imprimir o resultado na saída padrão |
| `awk '[padrão] {print $0}' [nome_arquivo]` | Imprimir todas as linhas que correspondem a um padrão em um arquivo |
| `diff [arquivo1] [arquivo2]` | Comparar dois arquivos e exibir as diferenças |
| `source [nome_arquivo]` | Ler e executar o conteúdo do arquivo no shell atual |
| `[comando] | tee [nome_arquivo] >/dev/null` | Armazenar a saída do comando em um arquivo e ignorar a saída do terminal |

## Pesquisando

| Comando | Descrição |
|--------------|--------------|
| `grep [padrão] [nome_arquivo]` | Pesquisar por um padrão específico em um arquivo com o grep |
| `grep -r [padrão] [nome_diretório]` | Pesquisar recursivamente por um padrão em um diretório |
| `locate [nome]` | Encontrar todos os arquivos e diretórios relacionados a um nome específico |
| `find [/local/do/diretório] -name [a]` | Listar nomes que começam com um caractere especificado [a] em uma localização especificada [/local/do/diretório] usando o comando find |
| `find [/local/do/diretório] -size [+100M]` | Ver arquivos maiores que um tamanho especificado [+100M] em uma pasta |

## Navegação de Diretórios

| Comando | Descrição |
|--------------|--------------|
| `tar cf [arquivo_comprimido.tar] [nome_arquivo]` | Arquivar um arquivo existente |
| `tar xf [arquivo_comprimido.tar]` | Extrair um arquivo arquivado |
| `tar czf [arquivo_comprimido.tar.gz]` | Criar um arquivo tar comprimido com gzip |
| `gzip [nome_arquivo]` | Comprimir um arquivo com a extensão .gz |

## Transferência de Arquivos

| Comando | Descrição |
|--------------|--------------|
| `scp [nome_arquivo.txt] [servidor/tmp]` | Copiar um arquivo para um diretório do servidor com segurança usando o comando scp do Linux |
| `rsync -a [/seu/diretório] [/backup/]` | Sincronizar o conteúdo de um diretório com um diretório de backup usando o comando rsync |

## Usuários e Grupos

| Comando | Descrição |
|--------------|--------------|
| `id` | Ver detalhes sobre os usuários ativos |
| `last` | Mostrar os últimos logins do sistema |
| `who` | Exibir quem está atualmente logado no sistema |
| `w` | Mostrar quais usuários estão logados e sua atividade |
| `groupadd [nome_do_grupo]` | Adicionar um novo grupo |
| `adduser [nome_do_usuário]` | Adicionar um novo usuário |
| `usermod -aG [nome_do_grupo] [nome_do_usuário]` | Adicionar um usuário a um grupo |
| `sudo [comando_a_ser_executado_como_superusuário]` | Elevar temporariamente os privilégios do usuário para superusuário ou root usando o comando sudo |
| `userdel [nome_do_usuário]` | Excluir um usuário |
| `usermod` | Modificar informações do usuário |
| `chgrp [nome_do_grupo] [nome_do_diretório]` | Alterar o grupo de um diretório |

## Instalação de Pacotes

| Comando | Descrição |
|--------------|--------------|
| `yum list installed` | Listar todos os pacotes instalados com yum |
| `yum search [palavra-chave]` | Encontrar um pacote por palavra-chave relacionada |
| `yum info [nome_pacote]` | Mostrar informações e resumo do pacote |
| `yum install [nome_pacote.rpm]` | Instalar um pacote usando o gerenciador de pacotes YUM |
| `dnf install [nome_pacote.rpm]` | Instalar um pacote usando o gerenciador de pacotes DNF |
| `apt install [nome_pacote]` | Instalar um pacote usando o gerenciador de pacotes APT |
| `rpm -i [nome_pacote.rpm]` | Instalar um pacote .rpm a partir de um arquivo local |
| `rpm -e [nome_pacote.rpm]` | Remover um pacote .rpm |
| `dpkg -i [nome_pacote.deb]` | Instalar um pacote .deb a partir de um arquivo local |
| `dpkg -r [nome_pacote.deb]` | Remover um pacote .deb |
| `tar zxvf [codigo_fonte.tar.gz] && cd [codigo_fonte] && ./configure && make && make install` | Instalar um software a partir do código-fonte |

## Gerenciamento de Processos

| Comando | Descrição |
|--------------|--------------|
| `ps` | Ver uma captura instantânea dos processos ativos |
| `pstree` | Mostrar os processos em um diagrama em forma de árvore |
| `pmap` | Exibir um mapa de uso de memória dos processos |
| `top` | Ver todos os processos em execução |
| `kill [ID_processo]` | Terminar um processo Linux com um ID específico |
| `pkill [nome_processo]` | Terminar um processo com um nome específico |
| `killall [nome_processo]` | Terminar todos os processos rotulados como "nome_processo" |
| `bg` | Listar e retomar trabalhos interrompidos em segundo plano |
| `fg` | Trazer o trabalho suspenso mais recente para o primeiro plano |
| `fg [trabalho]` | Trazer um trabalho específico para o primeiro plano |
| `lsof` | Listar arquivos abertos pelos processos em execução |
| `trap "[comandos_a_executar_ao_ser_interrompido]" [sinal]` | Capturar um sinal de erro do sistema em um script shell |
| `wait` | Pausar o terminal ou um script Bash até que um processo em execução seja concluído |
| `nohup [comando] &` | Executar um processo Linux em segundo plano |

## Gerenciamento e Informações do Sistema

| Comando | Descrição |
|--------------|--------------|
| `uname -r` | Mostrar informações do sistema |
| `uname -a` | Ver informações sobre a versão do kernel |
| `uptime` | Exibir quanto tempo o sistema está em execução, incluindo a média de carga |
| `hostname` | Ver o nome do sistema |
| `hostname -i` | Mostrar o endereço IP do sistema |
| `last reboot` | Listar o histórico de reinicialização do sistema |
| `date` | Ver a hora e a data atuais |
| `timedatectl` | Consultar e alterar o relógio do sistema |
| `cal` | Mostrar o calendário atual (mês e dia) |
| `whoami` | Ver qual usuário você está usando |
| `finger [nome_usuário]` | Mostrar informações sobre um usuário específico |
| `ulimit [flags] [limite]` | Ver ou limitar a quantidade de recursos do sistema |
| `shutdown [hh:mm]` | Agendar o desligamento do sistema |
| `shutdown now` | Desligar o sistema imediatamente |

## Uso do Disco

| Comando | Descrição |
|--------------|--------------|
| `df -h` | Ver espaço livre e usado em sistemas montados |
| `df -i` | Mostrar inodes livres em sistemas de arquivos montados |
| `fdisk -l` | Exibir partições de disco, tamanhos e tipos |
| `du -ah` | Ver uso de disco de todos os arquivos e diretórios |
| `du -sh` | Mostrar uso de disco do diretório em que você está |
| `findmnt` | Exibir ponto de montagem de destino para todos os sistemas de arquivos |
| `mount [caminho_dispositivo] [ponto_montagem]` | Montar um dispositivo |

## Login SSH

| Comando | Descrição |
|--------------|--------------|
| `ssh user@host` | Conectar-se ao host como usuário |
| `ssh host` | Conectar-se ao host com segurança via SSH na porta padrão 22 |
| `ssh -p [porta] user@host` | Conectar-se ao host usando uma porta específica |

## Permissões de Arquivo

| Comando | Descrição |
|--------------|--------------|
| `chmod 777 [nome_arquivo]` | Atribuir permissão de leitura, gravação e execução para todos |
| `chmod 755 [nome_arquivo]` | Dar permissão de leitura, gravação e execução para o proprietário e permissão de leitura e execução para grupo e outros |
| `chmod 766 [nome_arquivo]` | Atribuir permissão total ao proprietário e permissão de leitura e gravação para grupo e outros |
| `chown [usuário] [nome_arquivo]` | Alterar a propriedade de um arquivo |
| `chown [usuário]:[grupo] [nome_arquivo]` | Alterar a propriedade do usuário e do grupo de um arquivo |

## Network

| Comando | Descrição |
|--------------|--------------|
|`ip addr show` | Listar endereços IP e interfaces de rede|
|`ip address add [endereço_IP]`| Atribuir um endereço IP à interface eth0|
|`ifconfig` | Exibir endereços IP de todas as interfaces de rede|
|`netstat -pnltu` | Ver portas ativas (ouvindo) com o comando netstat|
| `netstat -nutlp` | Mostrar portas tcp e udp e seus programas|
| `whois [domínio]` | Exibir mais informações sobre um domínio|
| `dig [domínio] ` | Mostrar informações DNS sobre um domínio usando o comando dig|
| `dig -x host` | Fazer uma busca reversa em um domínio|
| `dig -x [endereço_IP]` | Fazer busca reversa de um endereço IP|
| `host [domínio]` | Realizar uma busca de IP para um domínio|
| `hostname -I` | Mostrar o endereço IP local|
| `wget [nome_arquivo]` | Baixar um arquivo de um domínio usando o comando wget|
| `nslookup [nome_domínio]` | Receber informações sobre um domínio da Internet|
| `curl -O [URL_arquivo]` | Salvar um arquivo remoto em seu sistema usando o nome de arquivo correspondente ao nome do servidor|

## Variáveis

| Comando | Descrição |
|--------------|--------------|
| `let "[variável]=[valor]"`| Atribuir um valor inteiro a uma variável|
| `export [nome_variável]` | Exportar uma variável do Bash| 
| `declare [nome_variável]= "[valor]"` | Declarar uma variável do Bash|
| `set` | Listar os nomes de todas as variáveis e funções do shell|
| `echo $[nome_variável]` | Exibir o valor de uma variável|

## Gerenciamento de Comandos do Shell

| Comando | Descrição |
|--------------|--------------|
| `alias [nome_alias]='[comando]'` | Criar um alias para um comando|
| `watch -n [intervalo_em_segundos] [comando]` | Definir um intervalo personalizado para executar um comando definido pelo usuário|
| `sleep [intervalo_de_tempo] && [comando]` | Adiar a execução de um comando|
| `at [hh:mm]` | Criar uma tarefa para ser executada em um determinado horário (Ctrl+D para sair do prompt depois de digitar o comando)|
| `man [comando]` | Exibir um manual interno para um comando |
| `history` | Imprimir o histórico dos comandos que você usou no terminal|

## Atalhos de Teclado do Linux

| Comando | Descrição |
|--------------|--------------|
| `Ctrl + C` | Encerrar o processo em execução no terminal|
| `Ctrl + Z` | Parar o processo atual - O processo pode ser retomado em primeiro plano com `fg` ou em segundo plano com `bg`|
| `Ctrl + W` | Recortar uma palavra antes do cursor e adicioná-la à área de transferência|
| `Ctrl + U` | Recortar parte da linha antes do cursor e adicioná-la à área de transferência|
| `Ctrl + K` | Recortar parte da linha após o cursor e adicioná-la à área de transferência|
| `Ctrl + Y` | Colar da área de transferência|
| `Ctrl + R` | Recuperar o último comando que corresponde aos caracteres fornecidos|
| `Ctrl + O` | Executar o comando recuperado anteriormente|
| `Ctrl + G` | Sair do histórico de comandos sem executar um comando|
| `!!` | Executar novamente o último comando |
| `Ctrl + D | Fazer logout da sessão atual|

## Informações de Hardware

| Comando | Descrição |
|--------------|--------------|
|`dmesg` | Mostrar mensagens de inicialização|
| `cat /proc/cpuinfo` | Ver informações da CPU|
| `free -h` | Exibir memória livre e usada |
| `lshw` | Listar informações de configuração de hardware |
| `lsblk` | Ver informações sobre dispositivos de bloco |
| `lspci -tv`| Mostrar dispositivos PCI em um diagrama em forma de árvore | 
| `dmidecode` | Exibir informações de hardware da BIOS |
| `hdparm -i /dev/disk` | Exibir informações de dados do disco |
| `hdparm -tT /dev/[dispositivo]` | Realizar um teste de velocidade de leitura no dispositivo/disco |
| `fsck [localização_disco_ou_partição]`| Executar uma verificação de disco em um disco ou partição desmontados |
