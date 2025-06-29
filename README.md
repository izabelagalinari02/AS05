## Talking com PDFs: Um Assistente de Perguntas e Respostas para PDFs com IA

Este aplicativo Streamlit permite que você converse com seus documentos PDF usando o poder de Grandes Modelos de Linguagem (LLMs) e embeddings de texto. Faça upload de seus PDFs, faça perguntas em linguagem natural e obtenha respostas perspicazes com base no conteúdo de seus documentos.

Interface com Deploy feito via Streamlit. Disponível em:
https://izabela.streamlit.app/

## Recursos

* **Carregamento de PDFs:** Carregue facilmente vários documentos PDF.
* **Perguntas e Respostas Conversacionais:** Participe de uma conversa natural com seus documentos.
* **Embeddings OpenAI:** Utiliza os embeddings de linguagem da OpenAI para uma busca semântica precisa.
* **Armazenamento Vetorial FAISS:** Armazena e recupera informações de seus documentos de forma eficiente.
* **Framework Langchain:** Aproveita o Langchain para aplicativos simplificados com LLM.

## Instalação e Configuração

1. **Clone o Repositório:**
   ```bash
   git clone https://your-repository-url.git
   cd your-repository-name
   ```

2. **Crie um Ambiente Virtual (Recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate   
   ```

3. **Instale as Dependências:**
   ```bash
   pip install -r requirements.txt
   ```
   Certifique-se de ter estas versões específicas em seu `requirements.txt` para evitar problemas de compatibilidade:
   ```
   langchain==0.0.184
   PyPDF2==3.0.1
   python-dotenv==1.0.0
   streamlit==1.18.1
   openai==0.27.6
   faiss-cpu
   altair==4
   tiktoken
   ```
   
4. **Configure a Chave da API da OpenAI:**

   * Crie um arquivo `.env` no diretório do projeto e adicione sua chave da API da OpenAI:
     ```
     OPENAI_API_KEY=sua_chave_api_aqui
     ```

5. **Execute o Aplicativo:**
   ```bash
   streamlit run app.py
   ```
   Isso abrirá o aplicativo em seu navegador da web padrão.

## Uso

1. **Carregar PDFs:** Use a barra lateral para carregar um ou mais documentos PDF.
2. **Clique em "Processar":** O aplicativo processará os PDFs e criará um índice.
3. **Faça Perguntas:** Digite suas perguntas na área de entrada de texto.
4. **Obtenha Respostas:** O assistente responderá com base em seus PDFs.

## Personalização (Opcional)

* **Modelos HTML:** Modifique `htmlTemplates.py` para personalizar a interface do chat.
* **Modelo de Embeddings:** Explore outros modelos de embeddings (por exemplo, Hugging Face) na função `get_vectorstore`.
* **LLM:** Experimente diferentes LLMs (por exemplo, Hugging Face Hub) na função `get_conversation_chain`.

## Aviso Legal

Este aplicativo é para fins educacionais e demonstrativos. A qualidade das respostas depende da qualidade de seus documentos e das capacidades do LLM. 

Se precisar de algum ajuste ou explicação adicional, me avise!
