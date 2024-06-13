Fundamentos do Linux

## Introdução

Este é um recurso de aprendizado criado para ajudar pessoas interessadas a adquirir habilidades em Linux para aprender.

<img align="right" src="./linux/resources/images/linuxpenguin.png" width="250"/>

## História do Linux

Linux é uma família de sistemas operacionais de código aberto e livre baseados no kernel Linux. Sistemas operacionais baseados em Linux são conhecidos como distribuições ou distros Linux. Exemplos incluem Debian, Ubuntu, Fedora, CentOS, Gentoo, Arch Linux e muitos outros.

O kernel Linux tem sido desenvolvido ativamente desde 1991 e tem se mostrado extremamente versátil e adaptável. Você pode encontrar computadores que executam Linux em uma ampla variedade de contextos ao redor do mundo, desde servidores web até celulares. Hoje, 90% de toda a infraestrutura em nuvem e 74% dos smartphones do mundo são alimentados pelo Linux.

Para ler mais sobre a história do Linux, distribuições Linux e kernel Linux, [clique aqui](./linux/resources/linux-history.md).


## Objetivos de aprendizado
Neste hack, você será desafiado com algumas tarefas comuns de um cenário do mundo real em tarefas de administração do Linux, tais como:

1. Criar uma Máquina Virtual Linux
2. Manipular arquivos e diretórios
3. Manipular o conteúdo de arquivos
4. Trabalhar com permissões padrão do Linux
5. Coletar informações sobre processos Linux em seu ambiente
6. Gerenciamento de usuários e grupos
7. Scripting básico de shell

## Desafios

Com exceção do desafio 01, que resulta em uma Máquina Virtual Linux necessária para todos os outros desafios, cada desafio pode ser feito separadamente e eles não são interdependentes. O nível de complexidade aumenta de acordo com o número do desafio.

* Desafio 01: **[Criar uma Máquina Virtual Linux](linux/Challenge-01.md)**
  - Uma máquina virtual Linux é um pré-requisito para os desafios, portanto, crie uma nova VM Linux do Ubuntu.
* Desafio 02: **[Manipulação de Diretórios](linux/Challenge-02.md)**
  - Aprenda a realizar operações comuns em diretórios, como exibir o diretório atual e listar o conteúdo do diretório.
* Desafio 03: **[Manipulação de Arquivos](linux/Challenge-03.md)**
  - Aprenda comandos básicos sobre manipulação de arquivos, como criar, renomear, encontrar e remover arquivos.
* Desafio 04: **[Conteúdo de Arquivos](linux/Challenge-04.md)**
  - Aprenda sobre manipulação de conteúdo de arquivos e descubra como contar linhas de arquivo, exibir linhas específicas de um arquivo e muito mais.
* Desafio 05: **[Permissões de Arquivos Padrão](linux/Challenge-05.md)**
  - Aprenda sobre as permissões de arquivo padrão do Linux e entenda como trabalhar com permissões de arquivo em um ambiente Linux.
* Desafio 06: **[Gerenciamento de Processos](linux/Challenge-06.md)**
  - Seus objetivos envolverão o gerenciamento básico de processos, como verificar processos em execução e identificar IDs de processos.
* Desafio 07: **[Gerenciamento de Grupos e Usuários](linux/Challenge-07.md)**
  - Neste desafio, você aprenderá sobre a criação de usuários e grupos em um ambiente Linux.
* Desafio 08: **[Scripting](linux/Challenge-08.md)**
  - Aprenda algumas coisas básicas sobre scripting de shell e o uso de comandos como echo, cut, read e grep.


## Pré-requisitos
- Acesso a um terminal. Os termos "terminal", "shell" e "interface de linha de comando" são frequentemente usados ​​de forma intercambiável, mas existem diferenças sutis entre eles:

	* Um terminal é um ambiente de entrada e saída que apresenta uma janela somente de texto executando um shell.
	* Um shell é um programa que expõe o sistema operacional do computador a um usuário ou programa. Em sistemas Linux, o shell apresentado em um terminal é um interpretador de linha de comando.
	* Uma interface de linha de comando é uma interface de usuário (gerenciada por um programa interpretador de linha de comando) que processa comandos para um programa de computador e gera os resultados.
Quando alguém se refere a um desses três termos no contexto do Linux, geralmente significa um ambiente de terminal onde você pode executar comandos e ver os resultados impressos no terminal.

		Tornar-se um especialista em Linux requer que você se sinta à vontade ao usar um terminal. Qualquer tarefa administrativa, incluindo manipulação de arquivos, instalação de pacotes e gerenciamento de usuários, pode ser realizada por meio do terminal. O terminal é interativo: você especifica os comandos a serem executados e o terminal gera os resultados desses comandos. Para executar qualquer comando, você o digita no prompt e pressiona ENTER.

- Existem alguns conceitos básicos que serão úteis se você os tiver. Se você quiser dar uma olhada, eles estão [listados aqui](./linux/resources/concepts.md).
- Conceitos sobre o Padrão de Hierarquia do Sistema de Arquivos (FHS) do Linux são recomendados, para que você possa obter mais detalhes sobre isso [aqui](./linux/resources/fhs.md).
- Em relação aos comandos do Linux, apenas como referência, [aqui está](./linux/resources/commands.md) um bom guia de referência rápida.
- As páginas de manual do Linux são suas melhores amigas. Certifique-se de usá-las da melhor maneira possível.

## Recursos de Aprendizado

* [Linux Journey](https://linuxjourney.com/)
* [Linux Upskill Challenge](https://linuxupskillchallenge.org/)
* [Guia para Iniciantes em Linux - Tecmint](https://www.tecmint.com/free-online-linux-learning-guide-for-beginners/)
* [Preparação para o Linux Foundation Certified System Administrator](https://github.com/Bes0n/LFCS)
* [Notas do Linux Foundation Certified System Administrator (LFCS)](https://github.com/simonesavi/lfcs)
* [O Projeto de Documentação do Linux](https://tldp.org/)
* [Introdução ao Linux - do TLPD](https://tldp.org/LDP/intro-linux/intro-linux.pdf)
* [Notas de Comandos do Linux para Profissionais](https://goalkicker.com/LinuxBook/LinuxNotesForProfessionals.pdf)
* [Introdução ao Linux - Curso gratuito da Linux Foundation](https://training.linuxfoundation.org/training/introduction-to-linux/)


## Contribuições
Contribuições na forma de erros, solicitações de recursos e PRs são sempre bem-vindas. Siga estas etapas antes de enviar um PR:

* Crie uma issue descrevendo o erro ou solicitação de recurso.
* Clone o repositório e crie um branch de tópico.
* Faça alterações, adicionando novos testes para novas funcionalidades.
* Envie um PR.

