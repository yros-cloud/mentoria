### **Programa de Mentoria - DevOps/SRE e Cloud Computing**

Duração Total do Programa prevista: 6 meses a 8 meses

Esse Cronograma está em constante desenvolvimento, os tópicos ficam prontos entre 1 e 2 semanas antes da apresentação do tópico.
Fique a vontade para abrir Issue ou Criar PR para adicionar algo ou alguma idéia no cronograma.


### Semana 1: Introdução e Fundamentos

* Apresentação do programa de mentoria e objetivos. 
* Sessão de introdução pessoal e definição de expectativas.
* Visão geral de SysAdmin, DevOps, SRE e Engenheiro de Plataforma.
* Conceito de abstração - O Pesquisador 
* Criação de conta no Github, configuração e criação de repositórios
* Introdução ao Github e ao protocolo Git básico
    * Branches
    * Pull Request/Merge Request
    * Markup
    * Issue
    * Merge
* Criação de times/squads

### Semana 2-3: Introdução a Sistemas Operacionais, Redes e Storage

* Instalação das ferramentas necessárias para o módulo
* Fundamentos Sistemas Operacionais
    * Linux/Windows/Mac OSX
    * Conceito de threads e processos (swapping) slice time 
    * Instalação de um Linux no Virtual Box
        * Estrutura de diretórios
        * Variáveis de ambiente
        * Conhecendo os comandos básicos de Linux
            * `introdução ao Shell`
            * `man`
            * `apt/yum/yast/apk`
            * `ls`
            * `find`
            * `chmod`
            * `chown`
            * `sudo`
            * `adduser/useradd`
            * `addgroup/groupadd`
            * `mv`
            * `cp`
            * `ps`
            * `ssh`
            * `du`
            * `vim/nano`
            * `sed`
            * `grep`
            * `sudo`
            * `stdin e stdout > >> tee`
            * `awk`
            * `shell script`
            * `set`
            * `env`
            * `exit code`
            * `alias`
            * `ln`
            * `bashrc e bash_profile`
    * Exercícios comandos de Linux
    * Simulação de problemas reais

	*  Referências e links úteis

* Guia foca linux
* Viva o linux
* Filme InProprietario
* Guia do Administrador do Sistema
* Fundamentos de Rede
    * Instalação de ferramentas necessárias
    * Como funciona uma comunicação de rede
    * Domínio de broadcast
    * Router e gateways 
    * Modelo de Referência OSI
    * Protocolo TCP e UDP  (RFCs)
    * IPV4 - Cálculo de rede, CIDR, Classes de Endereço, VLSM, Roteamento Estático e Dinâmico.
    * NAT, DNAT, SNAT
    * Serviços de Rede e protocolos (DNS, ICMP, SMTP, SSH, FTP, HTTP, HTTPS, MYSQL, WEBServer)
    * VPN (OpenVPN / IPSEC / Site2Site / User2Site)
    * Zero Trust
    * Introdução ao IPV6
    * Ferramentas de rede, roteamento.
    * Comandos
        * `ifconfig`
        * `ip route`
        * `iptraf`
        * `traceroute`
        * `iperf`
        * `vnstat`
        * `netstat`
        * `nslookup / dig`
        * `whois`
        * `iptables`
        * `netcat`
        * `telnet`
    * Exercícios de Solução de problemas em rede e problemas reais

	* Referências e links úteis


* Fundamentos de Storage
    * Instalação de ferramentas necessárias
    * Discos, volumes, storage, Inodes
    * DAS, NAS, SAN, CEPH
    * IOPS  e sua relação com a CPU
    * Exercício de montagem de volume, RAID, LVM, ISCSI, NAS, SMB 
    * Comandos:
        * `df`
        * `top`/`htop`
        * `mpstat`
        * `pidstat`
        * `vmstat`
        * `iostat`
        * `lvm`
        * `fdisk`
        * `mkfs`
        * `mount`
    * Caso de Solução de problema envolvendo discos
* Atividade Resolução de Problemas de performance no servidor usando as ferramentas open source

### Semana 4-5: 

* Do Bare metal até funções (a evolução da computação)
* Conceitos de servidores físicos, virtuais e em nuvem.
* Cloud computing Serviços
    * IaaS
    * PaaS
    * SaaS
* Containers
* Funções

#### Cloud computing

* Load Balance
* Autoscaling
* Object Storage
* IAM
* VPC
* Instances
* CDN
* Function
* SQL and NOSQL
* Eventos
* Filas


### Semana 6: Lógica de Programação e Scripting



* Introdução à lógica de programação.
* Prática de algoritmos simples.
* Build time e runtime conceitos
* Introdução a linguagens de script (Python, Bash, etc.).
* Exercícios práticos de scripting para automação.


### Semana 7: Servidores e Infraestrutura como Código (IaC)


* Introdução à Infraestrutura como Código (IaC).
* Ferramentas populares: Terraform, Ansible, Chef, Puppet, CDK, Pulumi
* Boas práticas
* Exercícios práticos de provisionamento de infraestrutura usando Terraform

#### CI/CD


* Métricas de Desempenho
* Github Actions
* Git Lab CI
* Steps de pipeline
* Git Flow ou Trunk Based
* Promote
* CODE OWNERS
* Branch Protection
* Boas práticas
    * Shared Pipelines (DRY)
    * Secrets
* Tests
    * Unit tests
    * Integration Tests
    * Security Tests
        * SAST/DAST/Container Scaning
        * Secrets Test
        * Infra Test
    * Build test
    * Smoke test
    * Performance test
    * Infra test
    * 

#### Aplicações Estáticas


* O Que é uma aplicação estática
* Node/JavaScript/HTML
* NestJS
* Exercicios Aplicacao Estática

#### APIs

* O Que é uma API
* Tipos de API
* Curl
* Header
* Response Codes


### Semana 8-9: Containers e Docker, Packaging 


* Introdução à containers e Docker.
* Gerenciamento de contêineres.
* Construção de imagens Docker.
* Orquestração de containers com Docker Compose.
* Containers para aplicações:
    * Golang
    * PHP
    * Java Spring
    * Python
    * Node/TypeScript


### Semana 10-11: Orquestração de Containers com Kubernetes


* Fundamentos do Kubernetes.
* Implantação de aplicativos em clusters Kubernetes.
* Escalabilidade e resiliência com Kubernetes.
* Exercícios práticos com Kubernetes.


### Semana 12: Serverless Computing


* Introdução ao conceito de serverless.
* Plataformas populares: AWS Lambda, Azure Functions, Google Cloud Functions.
* Desenvolvimento e implantação de funções serverless.
* Uso de eventos e gatilhos.


### Semana 13: Arquitetura de Aplicações Distribuídas


* Over Engineering
* Princípios de arquitetura de microsserviços.
* Comunicação entre microsserviços.
* Desafios e práticas recomendadas.
* Arquitetura de eventos
* Kafka


### Semana 14-15: Estratégias de Monitoramento e Observabilidade (SRE)


* Diferença entre monitoramento e observabilidade
* Importância do monitoramento em sistemas distribuídos (MELT).
* Ferramentas de monitoramento: Prometheus, Grafana, NewRelic, DataDog, Uptime Robot, OpenTelemetry
* Implementação de métricas e rastreamento.
* Logs
* SLI/SLA/SLO e Budget Error
* Status Page
* Ops Genie, PagerDuty
* Gerenciamento de incidentes e Postmortem, RCA
* Exercícios de gerenciamento de incidentes


### Semana 16-17: Segurança na Nuvem e Práticas de DevSecOps

* Princípios de segurança na nuvem.
* Melhores práticas de DevSecOps.
* Ferramentas de segurança: AWS IAM, Azure AD, GCP Identity & Access Management.

#### Gitops

* O Que é GitOps
* Entendendo um control plane
* ArgoCD
* Crossplane


### Semana 19-20: Resolução de Problemas e Simulação de Cenários

* Análise de casos de uso e resolução de problemas.
* Simulação de incidentes e prática de resposta.
* Revisão e consolidação de conhecimentos.

##### Arquitetando soluções em Cloud:

* migrando para cloud
* migrando para kubernetes


### Semana 21-24: Projetos Práticos e Acompanhamento Individual

* Divisão dos participantes em squads.
* Desenvolvimento de projetos práticos em equipe.
* Acompanhamento próximo de cada squad.
* Sessões individuais para elaboração de Planos de Desenvolvimento Individual (PDI).


### Semana 25-26: Apresentação de Projetos e Avaliação

* Apresentação dos projetos desenvolvidos pelos squads.
* Avaliação dos participantes e feedback individualizado.
* Discussão sobre próximos passos e oportunidades de aprimoramento.

### Final: Simulação de entrevistas

Durante todo o programa, haverá uma mistura de sessões teóricas, práticas e de discussão em equipe. O acompanhamento próximo garantirá que cada participante receba suporte adequado e tenha a oportunidade de aplicar os conhecimentos adquiridos em projetos reais.
