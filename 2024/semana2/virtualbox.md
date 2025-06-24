# Linux-on-VIrtualBox

# Instalação de um servidor Ubuntu uma Virtual Box

## Ferramentas necessárias (Passo 1):

### Virtual Box
- Virtual Box é necessário para criarmos a máquina virtual.
- Se você não o possui, é necessário que o instale na sua máquina.
- Download Virtual Box Oracle: https://www.virtualbox.org/wiki/Downloads
- Online terminal, Fedora e Alpine Linux: https://itsfoss.com/online-linux-terminals/

### Ubuntu Linux
- Ubuntu é um sistema operacional gratuito
- Para instalar o Linux Baixe o arquivo ISO do Ubuntu: https://yros-public.s3.amazonaws.com/ubuntu-minimal.iso
- Para usar uma versão já instalada: https://yros-public.s3.amazonaws.com/ubuntu-server-24-vbox.7z

## Criando uma máquina virtual (VM)(Passo 2):
**Abra seu Virtual Box para dar inicio a esse passo**

1. Clique no botão NOVO ou NEW na barra superior do lado direito.
2. Assim que clicar irá surgir um nova janela para nomear a sua máquina virtual, pode nomear como "Ubuntu Linux"
3. Na Opção Imagem ISO, selecione a o arquivo ISO que baixou no Passo 1
4. Por último clique em Próximo

![VirtualBox1](https://github.com/1saacYves/Linux-on-VIrtualBox/assets/170655155/4147de08-3db1-4f35-8508-90b26f37cb30)

### Configuração de Instalação VM:
1. Logo depois que clicar em **Próximo** no último item do Passo 2
2. Coloque um nome de **usuário** e **senha**
3. Na opção **NOME DO SERVIDOR**, coloque um nome simples sem espaços só para identificar o seu servidor, e clique em **Próximo**.

![VirtualBox2](https://github.com/1saacYves/Linux-on-VIrtualBox/assets/170655155/7141da90-635a-49ef-9a1e-78005c88de92)

### Selecionando Hardware
1. São recomendados para processamento **4GB** de RAM, selecione **4096MB** que equivalem a 4GB.
2. Clique **PRÓXIMO**

![VirtualBox3](https://github.com/1saacYves/Linux-on-VIrtualBox/assets/170655155/d34b93ac-2e38-49b4-8c7a-e076dc4cb3bc)

### Disco rigido
Deixe selecionado a opção **CRIAR UM NOVO DISCO RÍGIDO VIRTUAL AGORA**
No item **TAMANHO DO DISCO**, Selecione no mínimo **12GB**
Clique em **PRÓXIMO**.
E **FINALIZAR**

![VirtualBox4](https://github.com/1saacYves/Linux-on-VIrtualBox/assets/170655155/5471f4bc-3ac8-48d0-a821-8909672c3b03)

## Adicionando o Linux na máquina virtual (Passo 3):

1. Selecione a opção **CONFIGURAÇÕES** na barra superior a direita, isso vai abrir um menu de opções.
2. Selecione a opção **ARMAZENAMENTO**, clique no espaço vazio abaixo de **Controladora:IDE**
3. Clique no icone de CD, no item **DRIVE OPTICO**, e selecione a Imagem ISO que baixou, no meu caso está salvo como "mini.iso", em seguida clique em **OK**.

![VirtualBox5](https://github.com/1saacYves/Linux-on-VIrtualBox/assets/170655155/d97ae85b-1500-4731-9da0-560e9ebbcc6a)

### Instalando o Linux na VM
1. No canto superior a direita, clique em **INICIAR**, isso vai fazer com que inicie a VM e comece a instalação do Linux.
2. Pressione **Enter**
3. Aguarde finalizar a instalação.

![VirtualBox6](https://github.com/1saacYves/Linux-on-VIrtualBox/assets/170655155/992abdf5-0c0c-4d5d-bd67-86dee30055bd)

### Configurando
1. Selecione o Idioma e **CONTINUAR**
2. Depois será redirecioado para a tela de **RESUMO DE INSTALAÇÃO**, que contém diversas opções de configuração diferentes. Vamos atualizar cada um deles, especialmente as opções com marcas de alerta, antes de iniciar o processo de instalação.

   ![VirtualBox7](https://github.com/1saacYves/Linux-on-VIrtualBox/assets/170655155/8ae92783-2340-4839-863d-9f1ed16511ba)

4. Na Seção **SISTEMA** selecione **REDE E NOME DO HOST**, e o ligue depois clique em **PRONTO**
5. Ainda na seção **SISTEMA**, selecione **DESTINO DA INSTALAÇÃO**, selecione o disco, e na seção **CONFIGURAÇÃO DE ARMAZENAMENTO**, deixe marcada a opção **AUTOMÁTICA**
6. Na seção **SISTEMA** selecione **KDUMP**, e selecione a opção **ATIVAR KDUMP**, e pronto.
7. A opção mais importante na seção **PROGRAMA** é a opção **FONTE DE INSTALAÇÃO**, clique nessa opção e selecione a opção **MÍDIA DE INSTALAÇÃO DETECTADA AUTOMATICAMENTE**. Depois disso, clique no botão **VERIFICAR**.
8. Abra a opção Seleção de programas na seção Programas:
   Mantenha a opção **SERVIDOR COM GUI**, e selecione a opção **FERRAMENTAS DE DESENVOLVIMENTO** no menu a direita, por fim clique em pronto.
9. Agora, na Seção **CONFIGURAÇÕES DO USUARIO**, selecione a opção **SENHA ROOT**, e coloque uma senha, depois clique em PRONTO
10. Depois de atualizar todas essas informações pode dar inicio a instalação do Software, no botão **INICIAR A INSTALAÇÃO** e aguarde a instalação ser feita.
11. Quando finalizado a instalção clique em **REINICIAR O SISTEMA**

![VirtualBox8](https://github.com/1saacYves/Linux-on-VIrtualBox/assets/170655155/d86e8ded-2281-40ed-a37b-8f5a6e2c6db2)

### Finalizando instalação
- Para Finalizar dê aceite no contrato de licença.
- E por fim clique em **FINISH CONFIGURATION**

![VirtualBox9](https://github.com/1saacYves/Linux-on-VIrtualBox/assets/170655155/680cf450-eaaa-43cf-bc32-ab0ba5f31d10)