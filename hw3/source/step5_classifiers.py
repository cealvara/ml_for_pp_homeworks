from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

# 5. Build Classifier: For this assignment, select any classifier you feel 
# comfortable with (Logistic Regression for example)

def make_model(method):

    if method == 'RF':
        model = RandomForestClassifier(n_estimators=50, n_jobs=-1)
    elif method == 'BA':
        model = BaggingClassifier(DecisionTreeClassifier(max_depth=1), n_estimators = 5, max_samples=0.65, max_features=1.)
    elif method == 'AB':
        model = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), algorithm="SAMME", n_estimators=200)
    elif method == 'LR':
        model = LogisticRegression(penalty='l1', C=1e5)
    elif method == 'SVM':
        model = SVC(kernel='linear', probability=True, random_state=0)
    elif method == 'DT':
        model = DecisionTreeClassifier()
    elif method == 'KNN':
        model = KNeighborsClassifier(n_neighbors=3)

    return model