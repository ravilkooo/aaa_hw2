from typing import List

class CountVectorizer:
    def __init__(self):
        pass

    def fit_transform(self, corpus : List[str]) -> List[List[int]]:
        self._feature_names = []
        self._hashmap = {}
        hashmap_len = 0
        for sentence in corpus:
            for word in sentence.split():
                feature = word.lower()
                if feature not in self._hashmap:
                    self._hashmap[feature] = hashmap_len
                    hashmap_len += 1
                    self._feature_names.append(feature)
        self._docterm_matrix = []
        for sentence in corpus:
            row = [0]*hashmap_len
            for word in sentence.split():
                row[self._hashmap[word.lower()]] += 1
            self._docterm_matrix.append(row)
        return self._docterm_matrix

    def get_feature_names(self) -> List[str] :
        return self._feature_names

corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]
vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names())

print(count_matrix)
