### Definição de sistema operacional

O sistema operacional é um software, ou conjunto de softwares, cuja função é administrar e gerenciar os recursos de um sistema, desde componentes de hardware e sistemas de arquivos a programas de terceiros, estabelecendo a interface entre o computador e o usuário.

Entenda como um “computador” qualquer máquina de processamento automático de dados, como um desktop, notebook ou celular e um console de videogame, por exemplo.

O sistema operacional introduz uma camada de abstração entre o hardware e o usuário, que transforma comandos no mouse, teclado e solicitações do sistema, como gerenciamento de recursos (CPU, memória RAM), em linguagem de máquina, enviando instruções ao processador.

Este último os traduz para código binário, executa os comandos e envia as respostas como informações que aparecem na sua tela.

Um sistema operacional contém componentes divididos entre os para o usuário (como bibliotecas, programas e interface) e as instruções que compõem o seu núcleo (kernel).

### O que é kernel?

A grosso modo é a ponte entre usuário e hardware, mas não somente. O kernel compõe a parte central do programa e responde por tarefas cruciais, como:

Estabelecer a camada de abstração de baixo nível (linguagem de máquina) com o hardware;
Gerenciar recursos como processador, RAM, sistemas de arquivos e dispositivos de entrada e saída (monitor, teclado, mouse, impressora, etc.);
Gerenciar processos (execução) de programas;
Gerenciar o uso de dispositivos, memória do sistema e chamadas dos programas, definindo quais têm prioridade.

[Livro sobre Sistemas Operacionais](./LIVRO_UNICO.pdf)


### Sistema Monotarefa

Sistemas monotarefa como o nome já diz faz execução de apenas um programa por vez. Qualquer aplicação, para ser executada, deveria aguardar o término do programa atualmente em execução. Sistemas desse tipo se caracterizam por permitir que o processador, a memória e os periféricos dediquem-se, exclusivamente, a um único programa. Esses sistemas, conhecidos como monotarefa, enquanto um programa aguarda por um comando, como a digitação de algum dado pelo usuário, o processador permanece inativo sem realizar nenhum processo. Um exemplo de sistema monotarefa é o MS-DOS. Onde apenas uma janela era aberta e apenas um usuário utilizava os seus recursos disponíveis também monousuário. Até as primeiras versões do Windows, que já foram chamadas de multitarefa, não tinham de fato essa característica, já que eram executadas sobre o MS-DOS. Para tentar contornar essa limitação, emulava-se a multitarefa, porém o núcleo do programa fazia sua própria gestão dos processos. Caso o processo bloqueasse o Windows, todas as aplicações teriam de ser terminadas pois eram todas dependentes.


### Sistemas Multiprogramados/multitarefa

Este tipo de sistema operacional é uma evolução dos sistemas operacionais monoprogramados/monotarefa. Enquanto os sistemas operacionais mono programados/mono tarefa permitiam apenas a execução de um único programa, uma única tarefa, os sistemas multiprogramados/multitarefas permitem que vários programas sejam executados compartilhando os recursos do computador tais como discos, impressora, memória e processador. Neste sistema enquanto um programa espera uma entrada de dados pelo usuário um outro programa pode estar sendo processado no mesmo intervalo de tempo. Neste caso tanto a memória quanto o processador são compartilhados e o sistema operacional deve gerenciar e controlar este compartilhamento dos recursos de forma segura e protegida. Como existem vários programas sendo executados, várias tarefas, é função do sistema operacional garantir que um programa não afete o outro, permitindo a execução das tarefas de forma independente umas das outras. Por permitir o compartilhamento dos recursos pelas várias tarefas sendo executadas este tipo de sistema operacional possibilita a redução de custos em hardware. Entretanto, os sistemas multiprogramados/multitarefa são de implementação muito mais complexa, por ser necessário o gerenciamento e controle de todas as tarefas em execução e do compartilhamento dos recursos entre as tarefas.

### Sistemas multiprogramados de tempo compartilhado
Permitem a execução de várias tarefas pela divisão de tempo do uso do processador em pequenos intervalos de tempo denominados fatia de tempo ( time slice ). Os programas em execução se alternam no uso do processador, cada programa em execução fazendo uso de sua fatia de tempo. Desta forma, o tempo de uso do processador é compartilhado pelas várias tarefas em execução pelo sistema operacional. Por este motivo. estes sistemas também são chamados de sistemas time-sharing. Quando um programa termina seu intervalo de tempo de uso do processador ele é interrompido pelo sistema operacional, sendo substituído por outro programa e fica aguardando um novo intervalo de tempo para ter sua execução reiniciada do ponto onde foi interrompido. Este tipo de sistema permite a interação dos usuários com as aplicações através de monitor, teclado e mouse. O sistema operacional possui uma linguagem de comandos que são usados pelo usuário para interagir com o sistema operacional. Os comandos são digitados em uma interface de linha de comandos ou em uma interface gráfica com o uso de mouse. Por permitir a interação entre o usuário com as aplicações, estes sistemas também são conhecidos por sistemas online.  Observação: Atualmente todos os sistemas operacionais fazem uso de interface gráfica para interação com o usuário, porém a interface de linha de comandos também está presente em todos os sistemas operacionais. É muito importante conhecer a linguagem de comandos de um sistema operacional e fazer uso da interface de linha de comandos.


### Sistemas multiprogramados de tempo real

Permitem a execução de várias tarefas de acordo com a prioridade de execução de cada tarefa. A diferença entre os sistemas de tempo real e os sistemas de tempo compartilhado é que nos sistemas de tempo compartilhado o tempo de resposta pode variar um pouco sem no entanto comprometer a execução das tarefas, enquanto que nos sistemas de tempo real o tempo de resposta é rigidamente controlado e devem estar dentro de limites de tempo definidos que devem ser obedecidos caso contrário podem ocorrer problemas irreparáveis as aplicações. Costuma-se dizer que estes sistemas tem tempo de resposta quase instantâneo por isso são conhecidos por sistemas de tempo real. Em sistemas de tempo real não existe fatia de tempo para as tarefas em execução. O mecanismo utilizado para o compartilhamento do processador é a prioridade. Uma tarefa permanece em execução pelo processador o tempo que for necessário, até que outra tarefa com maior prioridade seja iniciada. A prioridade de execução das tarefas é determinada pela aplicação e não pelo sistema operacional. Estes sistemas são usados para aplicações críticas como controle de refinarias, controle de tráfego aéreo, sistemas de defesa, usinas termoelétricas, usinas nucleares, etc. Nestes sistemas o tempo de resposta é crítico para o controle de operações. Por isso são usados sistemas de tempo real.


### SISTEMAS OPERACIONAIS MAIS CONHECIDOS

### Windows

O Windows é o sistema operacional mais popular do mundo, usado por milhões de pessoas em todo o mundo. Ele é conhecido por sua interface amigável e sua compatibilidade com uma ampla variedade de softwares e hardwares.

No entanto, o Windows também é conhecido por sua vulnerabilidade a vírus e malware, o que pode comprometer a segurança do seu computador.

Ao comparar o Windows com outros sistemas operacionais como macOS, é importante considerar suas vantagens distintas. Aqui estão algumas vantagens do Windows:

##### Compatibilidade e suporte ao software

O Windows é um sistema operacional amplamente utilizado e, portanto, possui uma grande base de usuários e desenvolvedores. Isso resulta em uma ampla compatibilidade de software, com uma vasta gama de aplicativos e jogos disponíveis para Windows.

Além disso, o suporte da Microsoft é extenso, com atualizações regulares e ampla documentação para solução de problemas.

##### Variedade de hardware
Uma das principais vantagens do Windows é a ampla variedade de hardware disponível para os usuários. Você pode escolher entre uma ampla gama de fabricantes e modelos de computadores, laptops e dispositivos que são projetados especificamente para o sistema operacional Windows. Isso oferece opções de escolha para atender às necessidades e orçamentos individuais.

##### Jogos e entretenimento
O Windows é considerado a plataforma líder para jogos de PC, com a maioria dos jogos sendo desenvolvidos e otimizados para rodar no sistema operacional Windows.

A Microsoft também oferece recursos como o Xbox Game Pass para PC, que fornece acesso a uma biblioteca de jogos por assinatura. Além disso, o Windows suporta uma ampla gama de aplicativos de entretenimento, como serviços de streaming de vídeo e áudio.

##### Integração com ambientes corporativos
O Windows tem sido uma escolha popular em ambientes corporativos há muito tempo. Ele oferece recursos robustos de gerenciamento e segurança, além de suporte a uma ampla gama de aplicativos de negócios.

##### Personalização e flexibilidade
O Windows oferece uma variedade de opções de personalização, permitindo que os usuários ajustem a aparência e o funcionamento do sistema operacional de acordo com suas preferências.

Também é possível escolher entre uma variedade de navegadores da web, programas de e-mail e outros aplicativos de terceiros para atender às necessidades individuais.

### MacOS
O Mac OS é o sistema operacional usado em computadores Macintosh da Apple. Ele é conhecido por sua estabilidade e segurança, bem como sua facilidade de uso.

O Mac OS é menos vulnerável a vírus e malware do que o Windows, mas também é mais caro e menos compatível com uma ampla variedade de softwares e hardwares.

Aqui estão algumas vantagens do MacOS:

##### Integração com o ecossistema da Apple
O macOS é desenvolvido pela Apple e é projetado especificamente para funcionar em seus dispositivos, como iMac, MacBook, MacBook Pro e MacBook Air. Isso resulta em uma integração perfeita entre o hardware e o software, oferecendo uma experiência otimizada para os usuários da Apple.

Além disso, o macOS está intimamente ligado ao ecossistema da Apple, permitindo uma sincronização fácil com outros dispositivos da Apple, como iPhone e iPad, por meio do iCloud.

##### Design e interface intuitivos
O macOS é conhecido por seu design elegante e interface intuitiva. A Apple prioriza a experiência do usuário, fornecendo uma interface coesa e amigável, além de animações suaves e transições elegantes. Isso resulta em uma experiência agradável e fácil de usar para os usuários.

##### Estabilidade e desempenho
O macOS é conhecido por sua estabilidade e desempenho confiáveis. A Apple controla tanto o hardware quanto o software, permitindo uma otimização eficiente entre eles. Isso resulta em um sistema operacional estável e eficiente, com menor probabilidade de falhas ou travamentos.

##### Segurança e privacidade
A Apple tem uma reputação sólida em termos de segurança e privacidade. O macOS possui recursos de segurança integrados, como o Gatekeeper, que protege contra a execução de aplicativos não confiáveis, e o FileVault, que criptografa seus arquivos.

Além disso, a Apple tem uma abordagem rígida em relação à privacidade do usuário, com recursos como o Intelligent Tracking Prevention no Safari e controles granulares de privacidade em aplicativos.

##### Ecossistema de aplicativos e desenvolvimento
O macOS oferece uma ampla variedade de aplicativos disponíveis na Mac App Store, que são projetados especificamente para o sistema operacional.

Além disso, o macOS é amplamente utilizado em ambientes de desenvolvimento, sendo a plataforma preferida por muitos desenvolvedores de software, especialmente para o desenvolvimento de aplicativos para iOS e macOS.

### Linux
Linux é um sistema operacional de código aberto, o que significa que pode ser personalizado e modificado livremente pelos usuários. Isso permite que os usuários ajustem o sistema operacional para suas necessidades específicas e adicionem funcionalidades que não são encontradas em outros sistemas operacionais.

O Linux é conhecido por sua segurança, estabilidade e flexibilidade, tornando-o popular entre empresas, desenvolvedores e entusiastas de tecnologia. Além disso, o Linux é gratuito, o que significa que pode ser usado sem custos adicionais.

Embora o Linux seja um sistema operacional poderoso, sua curva de aprendizado pode ser íngreme, o que pode torná-lo menos acessível para usuários iniciantes. O Linux exige um conhecimento técnico mais avançado do que outros sistemas operacionais, o que pode dificultar a configuração e a personalização do sistema.

No entanto, existem muitos recursos e comunidades online disponíveis para ajudar os usuários a aprender e solucionar problemas relacionados ao Linux.

Aqui estão algumas vantagens do Linux:

##### Software livre e código aberto
Uma das principais vantagens do Linux é o fato de ser um sistema operacional de software livre e código aberto. Isso significa que você tem acesso ao código-fonte do sistema operacional e pode modificá-lo de acordo com suas necessidades.

Além disso, o Linux tem uma comunidade de desenvolvedores ativa que contribui para o aprimoramento contínuo do sistema.

##### Variedade de distribuições
O Linux é distribuído em várias versões ou distribuições, como Ubuntu, Fedora, Debian, CentOS, entre outras. Cada distribuição tem suas próprias características e objetivos, o que permite escolher uma que se adapte melhor às suas necessidades.

Isso também resulta em uma grande flexibilidade, pois você pode personalizar e adaptar o sistema operacional de acordo com suas preferências.

##### Estabilidade e desempenho
O Linux é conhecido por sua estabilidade e desempenho robustos. Devido à natureza de código aberto, muitos desenvolvedores e especialistas em segurança colaboram para aprimorar o sistema operacional e corrigir problemas de forma rápida. Além disso, o Linux é altamente configurável, permitindo otimizar o desempenho para diferentes tipos de hardware.

##### Segurança
O Linux é amplamente reconhecido por sua segurança. Devido à sua natureza de código aberto, muitos olhos estão constantemente examinando e aprimorando a segurança do sistema operacional. Vulnerabilidades e falhas de segurança são identificadas e corrigidas rapidamente, e existem muitas ferramentas e recursos disponíveis para garantir a segurança no Linux.

##### Customização e flexibilidade
O Linux oferece uma grande flexibilidade e capacidade de personalização. Você pode escolher entre uma variedade de ambientes de desktop, como GNOME, KDE, Xfce, entre outros, e personalizar a aparência e o comportamento do sistema operacional de acordo com suas preferências.

Além disso, o Linux suporta uma ampla gama de software e aplicativos de código aberto, fornecendo opções gratuitas e poderosas para diferentes necessidades.

