from src.sheets_loader import load_faq
from src.preprocessor import clean_text
from src.embeddings import EmbeddingModel
from src.vectorstore import create_vectorstore, add_faqs
from src.qa_pipeline import QAPipeline
from src.slack_bot import receive_message

# Carregar FAQs do mock Google Sheets
faqs = load_faq()

# Limpar texto
for faq in faqs:
    faq["resposta"] = clean_text(faq["resposta"])

# Criar embeddings
emb_model = EmbeddingModel()
embeddings = emb_model.encode([faq["resposta"] for faq in faqs])

# Criar vectorstore e adicionar FAQs
vectorstore = create_vectorstore()
add_faqs(vectorstore, faqs, embeddings)

# Inicializar pipeline QA
qa_pipeline = QAPipeline(vectorstore)

# Simulação de mensagem no Slack
while True:
    question = input("Digite sua pergunta (ou 'sair' para encerrar): ")
    if question.lower() == "sair":
        break
    receive_message(question, qa_pipeline)