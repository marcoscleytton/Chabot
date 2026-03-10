from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Pergunta:
    def __init__(self, id, texto):
        self.id = id
        self.texto = texto

class Resposta:
    def __init__(self, id, texto, pergunta_id):
        self.id = id
        self.texto = texto
        self.pergunta_id = pergunta_id

class BancoDeDadosQA:
    def __init__(self):
        self.perguntas = []
        self.respostas = []

    def adicionar_pergunta(self, pergunta):
        self.perguntas.append(pergunta)

    def adicionar_resposta(self, resposta):
        self.respostas.append(resposta)

    def encontrar_resposta(self, pergunta_texto):
        if not self.perguntas or not self.respostas:
            return None

        textos = [p.texto for p in self.perguntas] + [r.texto for r in self.respostas]
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(textos)

        pergunta_vector = vectorizer.transform([pergunta_texto])
        respostas_vectors = tfidf_matrix[len(self.perguntas):]

        similaridades = cosine_similarity(pergunta_vector, respostas_vectors).flatten()
        melhor_correspondencia = similaridades.argmax()

        if similaridades[melhor_correspondencia] > 0.3:
            return self.respostas[melhor_correspondencia]
        return None