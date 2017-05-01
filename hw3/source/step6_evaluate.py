from sklearn.metrics import precision_score


# 6. Evaluate Classifier: you can use any metric you choose for this assignment 
# (accuracy is the easiest one). Feel free to evaluate it on the same data you 
# built the model on (this is not a good idea in general but for this assignment, 
#     it is fine). We haven't covered models and evaluation yet, so don't worry 
# about creating validation sets or cross-validation. 

def evaluate(df, var):
    pass

def generate_binary_at_k(y_scores, k):
    cutoff_index = int(len(y_scores) * (k / 100.0))
    test_predictions_binary = [1 if x < cutoff_index else 0 for x in range(len(y_scores))]
    return test_predictions_binary

def precision_at_k(y_true, y_scores, k):
    preds_at_k = generate_binary_at_k(y_scores, k)
    #precision, _, _, _ = metrics.precision_recall_fscore_support(y_true, preds_at_k)
    #precision = precision[1]  # only interested in precision for label 1
    precision = precision_score(y_true, preds_at_k)
    return precision