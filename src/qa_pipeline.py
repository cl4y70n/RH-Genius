from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma

class QAPipeline:
    def __init__(self, vectorstore_collection):
        self.vectorstore_collection = vectorstore_collection
        self.llm = ChatOpenAI(temperature=0)
        self.retriever = Chroma(collection_name="faq_collection", persist_directory="./data/vectorstore").as_retriever()
        self.qa_chain = RetrievalQA.from_chain_type(llm=self.llm, retriever=self.retriever, chain_type="stuff")

    def get_answer(self, question):
        return self.qa_chain.run(question)