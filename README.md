# 🤖 Jarvis - Assistente de Voz em Python

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Licença: MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-yellow.svg)](LICENSE)

## ✨ Sobre o Projeto

O Jarvis é um assistente de voz pessoal desenvolvido em Python, capaz de rodar em segundo plano no Windows (usando o Agendador de Tarefas) e executar comandos do sistema operacional através de detecção de palavra-chave (Hotword).

O assistente utiliza tecnologias de reconhecimento de voz local e em nuvem para garantir baixo consumo de recursos e alta precisão nos comandos.

### 🚀 Funcionalidades Principais

* **Detecção de Hotword:** Usa o **Picovoice Porcupine** para escutar continuamente em modo offline e de baixo consumo pela palavra-chave `"Jarvis"`.
* **Reconhecimento de Fala:** Utiliza o **Google Speech Recognition** (API em nuvem) para transcrever comandos após a detecção da Hotword.
* **Text-to-Speech (TTS):** Respostas audíveis usando **pyttsx3** (ex: "Estou pronto!").
* **Comandos de Sistema:** Desligar/cancelar desligamento do PC, abrir navegadores, calculadora, etc.

---

## ⚙️ Tecnologias Utilizadas

| Tecnologia | Função | Observação |
| :--- | :--- | :--- |
| **Python** | Linguagem de Programação | Core do Projeto |
| **pvporcupine** | Detecção de Palavra-Chave (Hotword) | Offline, Baixo Consumo |
| **SpeechRecognition** | Transcrição de Comandos | Usa Google Web Speech API (online) |
| **PyAudio** | Acesso ao Microfone | Necessário para captura de áudio |
| **pyttsx3** | Voz do Assistente (TTS) | Offline, usa motores de voz do sistema |
| **python-dotenv** | Gerenciamento seguro de chaves | Para a `AccessKey` do Picovoice |

---

## 📋 Pré-requisitos

1.  **Python 3.x** (Recomendado 3.8 ou superior).
2.  **Microfone** funcional.
3.  **Conexão com a Internet** (necessária para o reconhecimento de comandos, após a Hotword).
4.  **Sistema Operacional:** Desenvolvido e testado no Windows.

### Configuração da Chave de Acesso

O Porcupine requer uma chave de acesso gratuita:

1.  Obtenha sua chave em **[console.picovoice.ai](https://console.picovoice.ai/)**.
2.  Crie um arquivo chamado **`.env`** na raiz do projeto.
3.  Adicione sua chave a este arquivo:
    ```
    PICOVOICE_ACCESS_KEY="SUA_CHAVE_DE_ACESSO_AQUI"
    ```

## 🚀 Instalação e Execução

### 1. Clonar o Repositório

```bash
git clone [https://github.com/SeuUsuario/Jarvis-Assistente-de-Voz.git](https://github.com/SeuUsuario/Jarvis-Assistente-de-Voz.git)
cd Jarvis-Assistente-de-Voz
```

### 2. Criar e Ativar o Ambiente Virtual

```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar o Script para Teste
```bash
python script.py
#Seu assistente irá dizer: "Bem Vindo, Jarvis Iniciado!"
```
---

## 🎙️ Comandos de Voz Disponíveis
<!-- Seu assistente responderá a estes comandos após ouvir a palavra-chave "Jarvis": -->

| Categoria | Comando de Voz | Descrição |
| :--- | :--- | :--- |
| **Controle de Sistema** | desligar computador | Inicia um timer de 30 segundos para desligamento. |
| **Controle de Sistema** | cancelar desligamento | Aborta qualquer desligamento ativo no Windows. |
| **Aplicativos** | abrir navegador | Abre o navegador Microsoft Edge. |
| **Aplicativos** | abrir calculadora | Abre o aplicativo Calculadora do Windows. |
| **Controle do Assistente** | até mais | Encerra o script em execução (encerra o loop). |

---

# 💡 Execução em Segundo Plano (Windows)

```bash
Crie o Launcher: Crie o arquivo jarvis.bat na raiz do projeto para ativar o venv e rodar o assistente_voz.py.

Configure o Agendador de Tarefas: Use o Agendador de Tarefas do Windows para configurar uma nova ação de inicialização (Gatilho: Ao fazer logon).

Programa/Script: cmd.exe

Argumentos: /c start /B "Jarvis" "C:\Caminho\Para\Seu\Projeto\jarvis.bat"
```

# 🤝 Contribuições
Contribuições, sugestões e relatórios de bugs são bem-vindos! Sinta-se à vontade para abrir uma Issue ou enviar um Pull Request.

# 📄 Licença
Este projeto está licenciado sob a Licença MIT.