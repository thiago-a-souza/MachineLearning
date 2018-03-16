# Author
Thiago Alexandre Domingues de Souza

# Machine Learning
Machine Learning (ML) is a field in Artificial Intelligence (AI) that is concerned with the development of computer programs that automatically improve with experience [(1)](#references). In that sense, if the system is able to learn and adapt according to past experiences, the programmer should not design all possible situations. This approach has been widely adopted to model  a wide range of applications from several fields, such as banking (e.g. credit analysis and fraud detection), medicine (e.g. medical diagnosis), networking (e.g. intrusion detection), speech and face recognition, etc.

A classical organization divides ML algorithms into two broad categories: supervised and unsupervised. Supervised learning algorithms requires a labeled training set (i.e. every element belongs a known class), which will be measured using a test set -  a set of elements different from the training set. When their output is a set of finite values (e.g. sunny, rainy, cloudy) they are identified as classification problems. Otherwise, when the output is a set of continuous values (e.g. age, height, weight) they are called regression problems. On the other hand, unsupervised learning algorithms does not require any prior information about the dataset, and their goal is to group objects based on their similarity (clustering). In addition to that, there is a new hybrid approach called semi-supervised learning, which is used when only a portion of the labeled dataset is provided.

# Supervised Learning

## Naive Bayes

Bayes theorem states that the probability of event B occuring, given that event A has already occured is:


![](/img/nb1.png)

### Example
Using the training set below, what's the probability to play a given game in a rainy day?

|     | outlook | temperature | humidity | windy |    play      |
|:---:|:-------:|:-----------:|:--------:|:-----:|:------------:|
|  1  |  sunny  |     hot     |   high   | false |     no       |
|  2  |  sunny  |     hot     |   high   | true  |     no       |
|  3  | overcast|     hot     |   high   | false |     yes      |
|  4  |  rainy  |     mild    |   high   | false |     yes      |
|  5  |  rainy  |     cool    |   normal | false |     yes      |
|  6  |  rainy  |     cool    |   normal | true  |     no       | 
|  7  | overcast|     cool    |   normal | true  |     yes      |
|  8  |  sunny  |     mild    |   high   | false |     no       |
|  9  |  sunny  |     cool    |   normal | false |     yes      |
|  10 |  rainy  |     mild    |   normal | false |     yes      |
|  11 |  sunny  |     mild    |   normal | true  |     yes      |
|  12 | overcast|     mild    |   high   | true  |     yes      |
|  13 | overcast|     hot     |   normal | false |     yes      |
|  14 |  rainy  |     mild    |   high   | true  |     no       |

We have two alternatives to answer that question:

![](/img/nb2.png)

Alternatively:

![](/img/nb3.png)

### Naive Bayes Classifier

A "naive" Bayes model takes a simplistic, but effective approach, that assumes that events are independent from one another. In practice, they can work very well even when that condition is not met [(2)](#references). Naive Bayes machine learning models assign new instances to the most likely class using the Maximum a Posteriori (MAP) equation, where *a* is the attribute and *v* is the class:

![](/img/nb4.png)

Rewriting to apply Bayes rule:

![](/img/nb5.png)

P(a1, a2, ..., an) can be dropped because it's a constant value, making no difference to indentify the max value:

![](/img/nb6.png)

Rewriting to apply the probability products, we have a Naive Bayes classifier:

![](/img/nb7.png)

### Example
Classify the test instance {outlook: sunny, temperature: cool, humidity: high, windy: true}, with yes/no classes.

Applying Naive Bayes classifier: 

![](/img/nb8.png)

Calculating classes:

![](/img/nb9.png)

The "no" class has the maximum probability, so for that particular instance, the game should not be played.

![](/img/nb10.png)

### Spam filter using Naive Bayes

A very practical application of Naive Bayes classifier is used in spam filters. For this application, it's necessary a training data of words present in spam and not spam emails. Using Naive Bayes approach, we assume that the words occurence are independent from each other - even though they are not. A test set should be executed against the training set to classify the email as spam or not spam.

## kNN
The idea behind k-Nearest Neighbor (kNN) is very simple. Having a training set with n attributes (i.e. n-dimensional space), it classifies an example based on the most frequent class among k nearest neighbors, using a provided distance metric (e.g. Euclidean, Manhattan, etc). When k=1, the unknown example is assigned to the class of the closest neighbor. However, this approach can be influenced by noise and return incorrect results, for instance, the example below in black would be  classified as red if it was used k=1. As result of that, choosing a good k is a challenge and depends on the training set used. Another common problem is having ties among classes. To minimize or eliminate that risk, it can be used odd numbers as k  or sort the nearest neighbors assigning weights according to their distances. 


<img src="https://github.com/thiago-a-souza/MachineLearning/blob/master/img/knn.png" height="35%" width="35%">


## Decision Tree

## SVM

# Unsupervised Learning

## K-Means

## Hierarchical Clustering





# References
(1) Mitchell, T. M. Machine Learning. McGraw Hill, 1997.

(2) Russell, Stuart J. and Norvig, Peter. Artificial intelligence: a modern approach (3rd edition). Pearson,  2009.

