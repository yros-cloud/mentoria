## O que é o Git?

O Git ajuda a acompanhar as alterações quando muitas pessoas trabalham juntas em código de computador. É como uma máquina do tempo para código, para que você possa ver o que mudou e voltar se necessário.

### Por que usar o Git?
É ótimo para o trabalho em equipe. O Git torna mais fácil para muitas pessoas trabalharem no mesmo projeto sem atrapalhar o trabalho um do outro. Também ajuda a corrigir erros com facilidade.

### Como funciona o Git?
O Git armazena todas as versões do código de um projeto. Quando você faz alterações, o Git tira uma foto (como um instantâneo) do que é diferente. Você pode fazer versões diferentes ao mesmo tempo sem problemas.

### Quais são os principais comandos do Git?
O Git é uma ferramenta bastante robusta e oferece diversos utilitários para gerenciar as versões de um projeto em linha de comando. Confira os principais comandos da ferramenta:

Git config
Git init;
Git clone;
Git status;
Git add;
Git commit;
Git log;
Git branch;
Git checkout;
Git diff.
Git pull
Git push
Git merge


0) Git config 

O comando git config é usado para configurar e personalizar o ambiente Git no seu sistema. Ele permite que você defina informações como seu nome de usuário, endereço de e-mail, editor padrão e muitas outras configurações que definem como o Git interage com seus repositórios.

A estrutura básica do comando é:

git config <opções> chave valor
<opções>: Pode ser global (--global) para definir configurações para todos os repositórios no seu sistema ou local (--local) para definir configurações específicas para um repositório em particular.
chave: A chave de configuração que você deseja definir (por exemplo, user.name para o nome de usuário).
valor: O valor que você deseja atribuir à chave (por exemplo, seu nome de usuário ou endereço de e-mail).
Por exemplo, para configurar seu nome de usuário globalmente, você pode usar o comando:

git config --global user.name "Seu Nome"
Isso é útil para garantir que todos os commits que você fizer em qualquer repositório Git no seu sistema tenham o seu nome associado a eles.

Além disso, o comando git config pode ser usado para personalizar muitos outros aspectos do seu ambiente Git, tornando-o mais adaptado às suas preferências e necessidades.

1) Git init

É utilizado para inicializar um repositório Git dentro de um diretório do sistema. Após sua utilização, a ferramenta passa a monitorar o estado dos arquivos no projeto.

Repositório

O repositório é a pasta do projeto. Todo repositório tem uma pasta oculta .git. Isso é o que mostra para o git e para você que existe um repositório naquela pasta.

Criar um novo repositório
Vá até a pasta do projeto.

Use o comando: git init

2) Git clone e Git Pull

É utilizado para criar uma cópia de um repositório remoto em um diretório da máquina. Ou seja, quando se deseja trabalhar em um repositório hospedado no github, clona-se esse repositório para o seu computador, trabalha-se nele, e então é pedida a permissão para atualizar as alterações online.

A partir de um repositório clonado, é possível acompanhar o estado de um projeto e suas modificações, além de contribuir com o projeto, a partir do envio das suas modificações ao repositório central.

Realizar um clone
Use o comando: git clone [link do repositório]
Uma pasta será criada com o nome do repositório no lugar onde foi realizado o comando.

Dentro do repositório.
Use o comando: git pull [nome do repositório remoto]
No caso do github, o nome do repositório remoto costuma ser origin. Quando ocorre um clone, é sempre origin.

3) Git status

É utilizado para verificar o status de um repositório git, bem como o estado do repositório central. O comando mostra informações sobre se o projeto local está sincronizado com o central, quais arquivos estão sendo monitorados pelo Git e em qual branch você está no projeto.

4) Git diff e Git log
É utilizado para visualizar modificações feitas entre commits, sejam eles entre um commit arbitrário e o estado atual do projeto, dois commits arbitrários, ou até mesmo todas alterações entre dois commits distintos.

Para visualizar as alterações entre um commit distinto e o atual, basta usar o comando:

git diff <- Hashcode do commit anterior ->
E serão listadas todas as diferenças no projeto entre os dois commits.


5) Git add

É utilizado para adicionar arquivos ao pacote de alterações a serem feitas. É possível adicionar um único arquivo, múltiplos arquivos de uma vez, como git add <-arquivo1-> <-arquivo2-> ..., ou até mesmo um diretório, a partir de seu caminho. Uma vez que um arquivo é adicionado ao pacote de alterações com o comando add, ele está pronto para entrar no próximo commit.

6) Git commit

Commit
Um commit é um grupo de alterações no código. Toda vez que você quiser "salvar" as alterações feitas por você no repositório, você commita essas mudanças. Um commit contém as alterações que foram feitas nele e uma mensagem descritiva, além de informações meta (data, autor, etc).

O ideal é que os commit sejam feitos de forma lógica e organizada, por exemplo: Você criou uma alteração no layout e vai comitar ela depois, ao invés de fazer commits separados ("Adição de div no HTML", "Alteração do CSS", "link do CSS"), faça um só commit ("Alteração no layout: <pequena descrição sobre a alteração>").

Ou seja, faça commit de alterações já completas ou que possam ser completadas por alguém. Nunca separe alterações em pequenos commits de poucas mudanças.

Criar um commit
Na pasta do repositório
Use o comando: git add [arquivos a serem adicionados ao commit]
Use o comando: git commit -m [mensagem]
O comando "git add ." adiciona todos os arquivos alterados num repositório.

7) Git branch

Branches são separações de código. O branch padrão do projeto é o master. Branches normalmente são utilizados para separar alterações grandes ou novas funcionalidades do projeto, por exemplo: Existe um projeto de blog, os desenvolvedores já fizeram quase toda a parte do blog, mas existem alterações para fazer no sistema de usuários do blog e algumas a fazer no sistema de posts do blog. Para isso, cria se uma branch "usuarios" e uma "posts" (ou algo do tipo) e fazem-se as alterações nessas branches, um time trabalha em cada uma dessas branches, enquanto isso, outro time continua trabalhando em pequenas mudanças ou bugfixes na branch master.

Criar uma branch

Use o comando: git branch [nome da branch]

Trocar de branch

Use o comando: git checkout [branch de destino]

8) Git checkout

É utilizado para navegar entre as versões do projeto, bem como entre as diferentes ramificações criadas. Para navegar entre as versões, basta usar o comando:

git checkout <- Hashcode do commit ->
E todo o estado do projeto se modificará ao estado no qual o commit foi feito.

Similarmente, para navegar entre as ramificações podemos usar o comando:

git checkout <- nome da branch ->
E a branch será alterada. O comando também permite criar uma branch e imediatamente mudar para ela, através do comando:

git checkout -b <- nome da branch ->
Que vai criar a ramificação e navegar até ela.


9) Git Push

Envia (ou tenta enviar) o código comitado atual para o repositório online.

Dentro do repositório.
Use o comando: git push [node do repositório remoto].


10) Pull Request

Um pull request é um pedido que se faz ao dono do repositório para que esse atualize o código dele com o seu código. Ou seja, você pede para que o dono do projeto ao qual você quer contribuir adicione suas modificações ao projeto oficial.


11) Git merge

Um merge é a união de duas branches, normalmente, merges são feitos na branch master ou main. No exemplo do blog, quando a alteração do blog for terminada, alguém vai unir essas alterações na branch master para que elas possam finalmente fazer parte do projeto de fato.

Os merges costumam dar bastante problema, pois os códigos podem (e provavelmente vão entrar em conflito). Se houverem alterações no mesmo arquivo ou o git não conseguir definir se alguma linha deve ou não entrar no projeto por motivo de conflito, essas alterações deverão ser corrigidas manualmente.

Realizar um merge
Vá para a branch de destino (exemplo: git checkout master).
Use o comando: git merge [branch a unir]

12) Fork
O fork é como um clone, porém dentro do github. Isso quer dizer que o repositório não vai ser baixado para seu computador, mas será criado um igual na sua conta.


Links uteis: https://rogerdudler.github.io/git-guide/index.pt_BR.html