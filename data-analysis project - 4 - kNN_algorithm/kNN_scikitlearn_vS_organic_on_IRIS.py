from sklearn import datasets
import numpy as np
import random
import matplotlib.pyplot as plt
'''
        We'll be applying both the SciKitLearn and our homemade classifier to a classic data set created by Ron Fisher in 1933.
        It consists of 150 different iris flowers.50 from each of three different species.For each flower, we have the following
        covariates: sepal length, sepal width,petal length, and petal width.
 '''
iris=datasets.load_iris()
# >>>iris["data"]
predictors = iris.data[:, 0:2]
outcomes = iris.target

plt.plot(predictors[outcomes==0][:,0], predictors[outcomes==0][:,1], "ro")
plt.plot(predictors[outcomes==1][:,0], predictors[outcomes==1][:,1], "go")
plt.plot(predictors[outcomes==2][:,0], predictors[outcomes==2][:,1], "bo")

k=5; filename="iris_grid.pdf"; limits=(4,8,1.5,4.5); h=0.1
(xx,yy,prediction_grid) = make_prediction_grid(predictors,outcomes,limits,h,k)
plot_prediction_grid(xx,yy,prediction_grid,filename)
plt.show()

from sklearn.neighbors import KNeighborsClassifier #predictions from skikit
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(predictors,outcomes)
sk_predictions  = knn.predict(predictors)

my_predictions = np.array([knn_predict(p,predictors,outcomes,5) for p in predictors])

# >>>sk_predictions == my_predictions
# >>>np.mean(sk_predictions == my_predictions)
print(" prediction by scikit learn : ")
print(100*np.mean(sk_predictions == outcomes))
print(" prediction by own model : ")
print(100*np.mean(my_predictions == outcomes))

# our homemade predicter is actually somewhat better
