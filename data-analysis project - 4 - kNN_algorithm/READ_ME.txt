Assigning observation(point) to a category & building Synthetic Data.We also build our very own kNN classifier.
 
Statistical learning refers to a collection
 of mathematical and computation tools to understand data.
In what is often called supervised learning,
the goal is to estimate or predict an output based on one or more inputs.
The inputs have many names, like predictors, independent variables,
features, and variables being called common.
The output or outputs are often called response variables,
or dependent variables.
If the response is quantitative - say, a number that measures weight or height,
we call these problems regression problems.
If the response is qualitative-- say, yes or no, or blue or green,
we call these problems classification problems.
This case study deals with one specific approach to classification.
The goal is to set up a classifier such that when 
it's presented with a new observation whose category is not known,
it will attempt to assign that observation to a category, or a class,
based on the observations for which it does know the true category.
This specific method is known as the k-Nearest Neighbors classifier,
or kNN for short.
Given a positive integer k,  say 5, and a new data point,
it first identifies those k points in the data that are nearest to the point
 and classifies the new data point as belonging to the most common class
 among those k neighbors.



Order of Project subparts :
1.kNN_distance_algorithm
2.kNN_majority_vote+nearest_neighbour
3.kKK_predict+synthetic_points
4.kNN_prediction_grids
5.kNN_scikitlearn_vS_organic_on_IRIS


I did this project to accompany my learnings from HarvardX course - PH526x Using Python for Research.

- Amartya Ranjan Saikia (amartyasaikia@acm.org/ar5saikia@gmail.com)