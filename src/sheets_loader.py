import pandas as pd

def load_faq(csv_path="data/sheets/faq_mock.csv"):
    df = pd.read_csv(csv_path)
    faqs = []
    for _, row in df.iterrows():
        faqs.append({"pergunta": row["Pergunta"], "resposta": row["Resposta"]})
    return faqs