class CountVectorizer:
    def __init__(self):
        pass

    def fit_transform(self, corpus: list[str]) -> list[list[int]]:
        """
        Функция формирует терм-документационную матрицу
        по переданному текстовому корпусу

        :param corpus: текстовый корпус
        :return: соответствующая корпусу терм-документационная матрица
        """
        # Создаём список фичей, а также хэшмап, чтобы можно было быстрее
        # определять наличие фичи и её номер в терм-документационной матрице
        self._feature_names = []
        self._feature_hashmap = {}
        feature_hashmap_len = 0
        # Формирование списка фичей и хэшмапы
        for sentence in corpus:
            for word in sentence.split():
                # Переводим буквы фичей в строчные
                feature = word.lower()
                if feature not in self._feature_hashmap:
                    self._feature_hashmap[feature] = feature_hashmap_len
                    feature_hashmap_len += 1
                    self._feature_names.append(feature)
        # Формирование терм-документационной матрицы
        self._docterm_matrix = []
        for sentence in corpus:
            row = [0]*feature_hashmap_len
            for word in sentence.split():
                row[self._feature_hashmap[word.lower()]] += 1
            self._docterm_matrix.append(row)
        return self._docterm_matrix

    def get_feature_names(self) -> list[str]:
        """
        Функция возращает список фичей, сформированный по текстовому
        корпусу corpus в методе fit_transform(corpus)

        :return: список фичей
        """
        return self._feature_names


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())

    print(count_matrix)
