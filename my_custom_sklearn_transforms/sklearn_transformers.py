# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns:
    def __init__(self, columns):
        self._columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = X.copy()
        for c in self._columns:
            if c in data:
                data.drop(labels=self._columns, axis='columns', inplace=True)
        return data
