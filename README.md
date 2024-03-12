# HelloPDF
Chat with your PDF 

HelloPDF provides a **RAG** **interface** to ask questions based on your uploaded PDFs.

## Installation
1. Create a .env file and add your HuggingFace API Token.
2. Install required libraries and run the server:
```
$python -r requirements.txt
$streamlit run app.py
```
Features:
* **Local Embeddings** for increased data privacy.
* Use of **Open Source LLMs** instead of ChatGPT services.

Note: Performace may vary depending on host machine as creating embeddings is a CPU intensive task.