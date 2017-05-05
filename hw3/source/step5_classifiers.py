from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

# 5. Build Classifier: For this assignment, select any classifier you feel 
# comfortable with (Logistic Regression for example)

def make_model(method):

    if method == 'RF':
        model = RandomForestClassifier(n_estimators=50, n_jobs=-1)
    elif method == 'BA':
        model = BaggingClassifier(DecisionTreeClassifier(max_depth=1, criterion='gini', min_samples_split=2, max_features='log2'), max_samples=0.65, max_features=1., n_jobs=-1)
    elif method == 'AB':
        model = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1, criterion='gini', min_samples_split=2, max_features='log2'))
    elif method == 'LR':
        model = LogisticRegression(penalty='l1', C=1e5, n_jobs=-1)
    elif method == 'SVM':
        model = SVC(kernel='linear', probability=True, random_state=0)
    elif method == "LSVM":
        model = LinearSVC(penalty='l2', random_state=0)
    elif method == 'DT':
        model = DecisionTreeClassifier()
    elif method == 'KNN':
        model = KNeighborsClassifier(n_neighbors=3, n_jobs=-1)

    return model