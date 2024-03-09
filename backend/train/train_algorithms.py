# Linear regression
from sklearn.linear_model import LogisticRegression# Train a logistic regression model on the training data

# KNN
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# SVM
from sklearn import svm

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


def linear_train(X_train, X_test, y_train, y_test):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)
    print('The accuracy of the Logistic Regression is', metrics.accuracy_score(prediction,y_test))
    

def knn(X_train, X_test, y_train, y_test):
    classifier = KNeighborsClassifier(n_neighbors=2)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    # Summary of the predictions made by the classifier
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))
    # Accuracy score
    print('accuracy is',accuracy_score(y_pred,y_test))


def svm():
    model = svm.SVC() #select the algorithm
    model.fit(X_train, y_train) # train the algorithm with the training data and the training output
    prediction=model.predict(X_test) #pass the testing data to the trained algorithm
    #check the accuracy of the algorithm. 
    print('The accuracy of the SVM is:',metrics.accuracy_score(prediction,y_test))


def main():
    pass


if '__main__' == __name__:
    main()