# AudioLives - Leitor de Chat Inteligente com Voz de IA

Este projeto é um sistema automatizado de Text-to-Speech (TTS) integrado ao chat da Twitch. Ele monitora mensagens destacadas por pontos do canal, utiliza Inteligência Artificial (OpenRouter) para categorizar e moderar o conteúdo em tempo real (bloqueando conteúdos nocivos) e reproduz o texto usando uma voz neural realista.

---

## Etapas para Configuração e Execução

Siga as etapas abaixo no seu terminal para colocar o sistema para rodar:

### Etapa 1: Clonar o Repositório
Abra o terminal do seu computador, clone o projeto do GitHub e entre na pasta do repositório:
```bash
git clone <URL_DO_REPOSITORIO>
cd AudioLives
```

### Etapa 2: Instalar as Dependências
Instale todas as bibliotecas do Python necessárias para o funcionamento do bot (como `twitchio`, `edge-tts` e `openai`) executando o comando:
```bash
pip install -r requirements.txt
```

### Etapa 3: Configurar as Variáveis de Ambiente (`.env`)
Crie um arquivo chamado exatamente **`.env`** na raiz do projeto (na mesma pasta onde está este arquivo README) e configure as suas chaves. 

Se quiser testar no seu próprio canal da Twitch, siga as instruções para gerar as credenciais:
1. **CHANNEL_NAME:** Altere para o nome do seu canal da Twitch (por padrão, está configurado para minha live, `Fiiiirezada`).
2. **TWITCH_TOKEN:** Acesse o site [twitchtokengenerator.com](https://twitchtokengenerator.com/), marque as permissões (`Scopes`) de `chat:read` e `chat:edit`, clique em gerar e copie o **Access Token**. Cole no arquivo sempre começando com `oauth:`.

O arquivo `.env` deve ficar neste formato:
```env
# Chaves da IA (OpenRouter)
OPENROUTER_API_KEY=chave_openrouter
MODEL_NAME=openai/gpt-oss-120b:free

# Configurações do Chat da Twitch
CHANNEL_NAME=sua_twitch
TWITCH_TOKEN=oauth:seu_token_twitch
```

### Etapa 4: Executar a Aplicação
Com todas as dependências instaladas e as chaves configuradas no `.env`, inicie o bot rodando o script principal a partir da raiz do projeto:
```bash
python src/main.py
```

---

## Etapa 5: Como Testar o Funcionamento

1. Assim que o bot inicializar com sucesso no seu terminal, ele exibirá a seguinte mensagem de confirmação:  
   `🤖 Sistema de TTS por Pontos Conectado! Canal: Fiiiirezada`
2. Abra o chat do canal da Twitch configurado (por padrão, `Fiiiirezada`).
3. No chat da live, use os pontos do canal (**papagaio coins**) para resgatar o recurso nativo **"Destacar minha mensagem"** (recompensa padrão que custa 100 pontos), digite o seu texto e envie.
4. **O que vai acontecer:** O bot irá capturar o destaque em tempo real, acionará a LLM para fazer a moderação contextual automática, definirá a categoria da mensagem no console e reproduzirá a fala de forma fluida no sistema de som do computador através da voz de IA do Antonio.
