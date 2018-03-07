from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

#Loading the dataset
iris=datasets.load_iris()

#import the data set that will be used to create the model
iris = datasets.load_iris()
#Setting X to data
X = iris.data
#Setting Y to the target (classes for the data set)
Y = iris.target

#Split the data and targets into test variables and training variables
Xtrain,Xtest,Ytrain,Ytest=train_test_split(X,Y,test_size=0.2, random_state=0)

#Feature Scaling
Xscale = StandardScaler()
Xtrain = Xscale.fit_transform(Xtrain)
Xtest = Xscale.transform(Xtest)

#split the data for training and testing
kneigh= KNeighborsClassifier(n_neighbors=3)
kneigh.fit(Xtrain,Ytrain)

#Using the model classify each instance
predict=kneigh.predict(Xtest)

#Print the accuracy of the model
print(metrics.accuracy_score(Ytest,predict))

#Change K
Krange=range(1,50)
accuracy=[]

for k in Krange:
    #Update the model for different K values
    kneigh=KNeighborsClassifier(n_neighbors=k)
    kneigh.fit(Xtrain,Ytrain)
    #Using the updated model classify each of the instances
    predict=kneigh.predict(Xtest)
    #Determine the accuracy of the model
    accuracy.append(metrics.accuracy_score(Ytest,predict))

#Plot the different accuracies for each K value
plt.plot(Krange,accuracy)
plt.xlabel("value of k")
plt.ylabel("testing accuracy")
plt.show()