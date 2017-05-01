from sklearn.linear_model import LogisticRegression

# 5. Build Classifier: For this assignment, select any classifier you feel 
# comfortable with (Logistic Regression for example)

class MyClassifier(object):
    def __init__(self, X, Y, method):
        
        if method == 'logistic':
            self.model = LogisticRegression()
            self.model.fit(self.X_train, self.Y_train)