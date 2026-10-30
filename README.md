# Projeto Ransomware e Keylogger Simulados com Python

## 1. Introdução

Este projeto foi desenvolvido como parte do Bootcamp de Cibersegurança da DIO, com o objetivo de estudar o funcionamento de dois tipos de malware: Ransomware e Keylogger, utilizando Python em um ambiente controlado e exclusivamente educacional.

## 2. Ferramentas utilizadas

- Python
- VS Code
- Windows
- Bibliotecas Python para criptografia, captura simulada de teclas e Temporizador

## 3. Desenvolvimento

### 3.1. Ransomware Simulado

Foi desenvolvido um script em Python para simular o comportamento de um ransomware, utilizando arquivos de teste.

Funcionalidades:
- Criação de arquivos de teste.
- Criptografia e descriptografia de arquivos.
- Geração de uma mensagem simulada de resgate.
- Utilização do pyw para "camuflagem" do python.


### 3.2. Keylogger Simulado

Foi desenvolvido um script para demonstrar o funcionamento de um keylogger, responsável por registrar teclas digitadas.

Funcionalidades:
- Captura simulada de teclas.
- Registro das informações em arquivo `.txt`.
- Demonstração de técnicas de furtividade.
- Estudo do envio de informações por e-mail.

## 4. Integração do Keylogger com Telegram (Teste Educacional)

Durante os testes em ambiente controlado, consegui realizar a integração entre o Keylogger Simulado e um bot do Telegram.

O objetivo foi demonstrar, de forma educacional, como funciona a comunicação entre um script Python e uma API externa. Durante a execução, o programa realiza a captura de eventos de teclado autorizados no ambiente de teste e envia os registros para um chat do Telegram previamente configurado.

### Configuração do Telegram

Para reproduzir a integração em um ambiente próprio de estudos e autorizado, é necessário:

1. Acessar o Telegram e conversar com o **@BotFather**.
2. Criar um novo bot utilizando o comando `/newbot`.
3. Copiar o token de acesso fornecido pelo Telegram.
4. Iniciar uma conversa com o bot criado `/start`.
5. Configurar o token e o `Chat ID` nas variáveis de ambiente do projeto.

        Observações de segurança:

        Este experimento foi desenvolvido exclusivamente para fins educacionais, com o objetivo de compreender a captura de eventos de teclado, a comunicação com APIs e os riscos relacionados a ferramentas de monitoramento.

        **Importante:** qualquer teste deve ser realizado somente em dispositivos próprios ou com autorização expressa do responsável. A captura e o envio de informações de terceiros sem consentimento podem representar uma violação de privacidade e da legislação aplicável.

## 5. Medidas de Defesa

Algumas medidas importantes para prevenir ataques desse tipo são:

- **Antivírus:** identificar e bloquear ameaças.
- **Firewall:** controlar conexões suspeitas.
- **Sandboxing:** executar arquivos suspeitos em ambientes isolados.
- **Backups:** manter cópias de segurança dos arquivos.
- **Conscientização:** evitar links,