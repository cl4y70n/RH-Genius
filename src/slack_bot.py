def receive_message(question, qa_pipeline):
    print(f"Pergunta recebida: {question}")
    answer = qa_pipeline.get_answer(question)
    print(f"Resposta: {answer}")