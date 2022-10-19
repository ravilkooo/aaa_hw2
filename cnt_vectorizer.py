class CountVectorizer:
    def __init__(self):
        # Набор фичей корпуса
        self._feature_names = []

    def fit_transform(self, corpus: list[str]) -> list[list[int]]:
        """
        Функция формирует терм-документационную матрицу
        по переданному текстовому корпусу

        :param corpus: текстовый корпус
        :return: соответствующая корпусу терм-документационная матрица
        """
        # В данном методе
        # сохраняем набор _feature_names как атрибут класса,
        # т.к. он понадобиться для передачи набора фичей в методе get_feature_names()

        # feature_names_set - набор фичей корпуса
        feature_names_set = set()
        # docterm_dict - массив, где i-ый элемент представляет собой словарь, где
        # ключ: фича из i-ого предложения корпуса
        # значение: количество повторений данной фичи в i-ом предложении корпуса
        docterm_dict = []
        for sentence in corpus:
            # Преподготовка данных:
            # features_list - наборов фичей предложения sentence (с повторениями)
            feature_list = list(map(lambda word : word.lower(), sentence.split()))
            # features_dict - словарь, где
            # ключ: фича из предложения sentence
            # значение: количество повторений данной фичи в предложении sentence
            feature_dict = dict( (feature, feature_list.count(feature) ) for feature in set(feature_list))
            # сохраняем словарь фичей предложения sentence
            docterm_dict.append(feature_dict)
            # пополяняем множетсво фичей новыми фичами из предложения sentence
            feature_names_set = feature_names_set.union(feature_dict.keys())
        # Преобразуем и сохраняем множество фичей в лист фичей как атрибут класса
        self._feature_names = list(feature_names_set)
        # print(f'feature_names = {self._feature_names}')
        # print(f'docterm_dict = {docterm_dict}')
        # Формируем терм-документную матрицу:
        # считаем сколько раз в каждом предложении встречается каждая фича из _feature_names
        # с помощью сохранённых словарей со счётчиками фичей внутри одного предложения
        return [ [feature_dict.get(feature) or 0 for feature in self._feature_names] for feature_dict in docterm_dict ]

    def get_feature_names(self) -> list[str]:
        """
        Функция возращает список фичей, сформированный по текстовому
        корпусу corpus в методе fit_transform(corpus)

        :return: список фичей
        """
        return list(self._feature_names)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    # Проверяем работу метода
    # Создаём объект
    vectorizer = CountVectorizer()
    # Получаем терм-док матрицу
    count_matrix = vectorizer.fit_transform(corpus)
    # Выводим все фичи с помощью метода get_feature_names()
    print(vectorizer.get_feature_names())
    # Выводим терм-док матрицу
    print(count_matrix)
