import os
import glob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class FAQHandler:
    def __init__(self, folder_path):
        self.qa_pairs = []
        self.questions = []
        self.answers = []
        self.load_faqs(folder_path)

    def load_faqs(self, folder_path):
        for file_path in glob.glob(os.path.join(folder_path, '*.txt')):
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.read().splitlines()
                for line in lines:
                    if '?' in line:
                        q, *a = line.split('?')
                        question = q.strip() + '?'
                        answer = '?'.join(a).strip()
                        self.qa_pairs.append((question, answer))
                        self.questions.append(question)
                        self.answers.append(answer)

        self.vectorizer = TfidfVectorizer().fit(self.questions)
        self.vectors = self.vectorizer.transform(self.questions)

    def answer_query(self, query):
        query_vec = self.vectorizer.transform([query])
        similarity = cosine_similarity(query_vec, self.vectors).flatten()
        best_idx = similarity.argmax()
        if similarity[best_idx] < 0.3:
            return "Sorry, I couldn’t find a relevant FAQ answer."
        return f"Q: {self.questions[best_idx]}\nA: {self.answers[best_idx]}"

