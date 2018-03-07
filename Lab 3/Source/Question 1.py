from sklearn import datasets, svm, metrics
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

#Set the model. We will be using both the linear discriminant analysis method.
lda = LinearDiscriminantAnalysis()
lr = LogisticRegression()

#import the data set that will be used to create the model
wine = datasets.load_wine()

#Setting X to data
X = wine.data[:,11:]

#Setting Y to the target (classes for the data set)
Y = wine.target

#Split the data and targets into test variables and training variables
Xtrain,Xtest,Ytrain,Ytest=train_test_split(X,Y,test_size=0.2, random_state=0)

#Feature Scaling
Xscale = StandardScaler()
Xtrain = Xscale.fit_transform(Xtrain)
Xtest = Xscale.transform(Xtest)

Xvariables = Xtest
Yvariables = Ytest

#Creating the range for the X and Y axis and setting the pixel resolution to 0.01
Xaxis, Yaxis = np.meshgrid(np.arange(start = Xvariables[:,0].min()-1, stop = Xvariables[:,0].max()+1, step = 0.01),
                           np.arange(start = Xvariables[:,1].min()-1, stop = Xvariables[:,1].max()+1, step = 0.01))

#Setting the limits of the x and y axis
plt.xlim(Xaxis.min(), Xaxis.max())
plt.ylim(Yaxis.min(), Yaxis.max())

for fig_num, model in enumerate(('Linear Discriminant Analysis', 'Logistic Regression')):
#Plotting each point in the test values
    for i, j in enumerate(np.unique(Yvariables)):
        plt.scatter(Xvariables[Yvariables == j,0], Xvariables[Yvariables == j, 1],
                    c=ListedColormap(('blue','red','green'))(i), label = j)
        # Add the legend for graph
        plt.legend()

    #Provide the title and the names for the x and y axis
    plt.figure(fig_num)
    plt.xlim(Xaxis.min(), Xaxis.max())
    plt.ylim(Yaxis.min(), Yaxis.max())
    plt.title(model)
    plt.xlabel('Feature 11')
    plt.ylabel('Feature 12')

    if model is 'Linear Discriminant Analysis':
        clf = lda
    else:
        clf = lr

    # Use the training variables to generate the model
    clf.fit(Xtrain, Ytrain)

    #Use the testing variables to test the model that was generated
    expected = Ytest
    predicted = clf.predict(Xtest)

    #Show the accuracy of each model. Compare what was expected with what was generated
    print('The accuracy of the', model,  'method is:',metrics.accuracy_score(expected,predicted))

    #Creating the line between the two classes
    plt.contourf(Xaxis,Yaxis, clf.predict(np.array([Xaxis.ravel(),Yaxis.ravel()]).T).reshape(Xaxis.shape),alpha = 0.75,
             cmap = ListedColormap(('blue','red','green')))

#Show the graphs
plt.show()
