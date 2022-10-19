class CountVectorizer:
    def __init__(self):
        self._feature_names = []

    def fit_transform(self, corpus: list[str]) -> list[list[int]]:
        """
        Функция формирует терм-документационную матрицу
        по переданному текстовому корпусу

        :param corpus: текстовый корпус
        :return: соответствующая корпусу терм-документационная матрица
        """

        '''
        # отдельно храним набор _feature_names как атрибут класса, т.к. он понадобиться при выводе набора фичей
        # в методе get_feature_names()
        # массив словарей - каждая i-ый словарь содержит слова (ключи) i-ого предложения
        # и количество повторений данного слова в это предложениее (значение)
        '''
        # _feature_names - набор фичей корпуса
        self._feature_names = set()
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
            self._feature_names = self._feature_names.union(feature_dict.keys())
        # преобразуем множество фичей в лист фичей
        self._feature_names = list(self._feature_names)
        # print(f'feature_names = {self._feature_names}')
        # print(f'docterm_dict = {docterm_dict}')
        # Формируем терм-документную матрицу:
        # считаем сколько раз в каждом предложении встречается каждая фича из _feature_names
        # с помощью сохранённых словарей со счётчиками фичей внутри одного предложенияЦ
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


    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())

    print(count_matrix)