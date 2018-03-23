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

|     | outlook | temperature | humidity |  wind  |   play    |
|:---:|:-------:|:-----------:|:--------:|:------:|:---------:|
|  1  |  sunny  |     hot     |   high   | weak   |    no     |
|  2  |  sunny  |     hot     |   high   | strong |    no     |
|  3  | overcast|     hot     |   high   | weak   |    yes    |
|  4  |  rainy  |     mild    |   high   | weak   |    yes    |
|  5  |  rainy  |     cool    |   normal | weak   |    yes    |
|  6  |  rainy  |     cool    |   normal | strong |    no     | 
|  7  | overcast|     cool    |   normal | strong |    yes    |
|  8  |  sunny  |     mild    |   high   | weak   |    no     |
|  9  |  sunny  |     cool    |   normal | weak   |    yes    |
|  10 |  rainy  |     mild    |   normal | weak   |    yes    |
|  11 |  sunny  |     mild    |   normal | strong |    yes    |
|  12 | overcast|     mild    |   high   | strong |    yes    |
|  13 | overcast|     hot     |   normal | weak   |    yes    |
|  14 |  rainy  |     mild    |   high   | strong |    no     |

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
Classify the test instance {outlook: sunny, temperature: cool, humidity: high, windy: strong}, with yes/no classes.

Applying Naive Bayes classifier: 

![](/img/nb8.png)

Calculating classes:

![](/img/nb9.png)

The "no" class has the maximum probability, so for that particular instance, the game should not be played.

![](/img/nb10.png)

### Spam filter using Naive Bayes

A very practical application of Naive Bayes classifier is used in spam filters. For this application, it's necessary a training data of words present in spam and not spam emails. Using Naive Bayes approach, we assume that the words occurence are independent from each other - even though they are not. A test set should be executed against the training set to classify the email as spam or not spam.

## kNN
The idea behind k-Nearest Neighbor (kNN) is very simple. Having a labeled dataset (a.k.a training set) with *n* attributes (i.e. *n*-dimensional space), it classifies an example based on the most frequent class among *k* nearest neighbors, using a provided distance metric (e.g. Euclidean, Manhattan, etc). When *k*=1, the unknown example is assigned to the class of the closest neighbor. However, this approach is sensitive to noise and may return incorrect results.  For instance, the example  in the following figure would be classified as red for 1NN and blue for 5NN. As result of that, choosing a good *k* can be difficult depending on the training set. Good candidates for *k* can be determined empirically by choosing an initial *k*, estimating the error rate and incrementing *k* until an acceptable threshold is found.  

Another common problem occurs when the number of neighbor classes are tied. There are several alternatives to eliminate that side effect, for example, by choosing a random class among ties, or assigning weights to tied classes according to their distances, etc.

Using kNN against large training sets can be prohibitive. Ideal supervised machine learning algorithms should demand a high computational cost in training phase and a fast test phase, but kNN does the opposite. It does not have a training phase, and the test phase is time-consuming, since the entire training set is used to search for nearest neighbors. Several solutions were proposed to mitigate this difficulty: using kd-trees to store nearby nodes more efficiently, eliminating least relevant dimensional spaces, removing redundant data from the training set, etc [(3)](#references). 

<img src="https://github.com/thiago-a-souza/MachineLearning/blob/master/img/knn.png" height="80%" width="80%">


## Decision Tree
Decision Trees are used to solve both classification and regression problems, and their intuitive structure emulate human decisions. Starting from the root node, every non-leaf node have descendents that represent  alternatives available, and leaf nodes denote the result for the decisions taken.

ID3 (Iterative Dichotomiser), C4.5 (a sucessor of ID3) and CART (Classification and Regression Trees) are  the most popular decision tree algorithms. All three algorithms build decision trees using a greedy strategy in top-down recursive divide-and-conquer approach.


## SVM

# Unsupervised Learning

## K-Means

## Hierarchical Clustering





# References
(1) Mitchell, T. M. Machine Learning. McGraw Hill, 1997.

(2) Russell, Stuart J. and Norvig, Peter. Artificial intelligence: a modern approach (3rd edition). Pearson,  2009.

(3) Han, Jiawei; Pei, Jian; Kamber, Micheline. Data mining: concepts and techniques (3rd edition). Morgan Kaufmann, 2011.


