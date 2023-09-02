import numpy as np
class Perceptron:
    """perceptron classifier.

    Parameters
    ----------
    eta : float
        Learning Rate (between 0.0, 1.0).
    n_iter : int
        nuber of iteration over dataset.
    random_state : int
        random number generator seed for random weights initialization.

    Attributes
    ----------
    w_ : 1d-array
        weights after fitting.
    b_ : Scalar
        Bias unit after fitting.
    errors_ : list
        numbers of mis-classifications (updates) in each epoch.
    """
    def init(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        """Fit training data.

        Parameters
        ----------
        X: {array-like}, shape = [n_examples, n_features]
            training vectors where n_examples is the number of examples and n_features is the number of features.
        y: array-like, shape = [n_examples]
            target values

        Returns
        -------
        self : object
        """
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=X.shape[1])
        self.b_ = np.float_(0.)
        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0.0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_ += update * xi
                self.b_ += update
                errors += int(update != 0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """Calculate net input."""
        return np.dot(X, self.w_) + self.b_

    def predict(self, xi):
        """Return class label after unit step"""
        return np.where(self.net_input(xi) >= 0.0, 1, 0)
