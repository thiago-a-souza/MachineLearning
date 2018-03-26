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

There are two alternatives to answer that question:

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

<p align="center">
<img src="https://github.com/thiago-a-souza/MachineLearning/blob/master/img/knn.png" height="80%" width="80%">
</p>

## Decision Tree
Using an intuitive structure that emulate human decisions, decision trees are used to solve both classification and regression problems. Starting from the root node, every non-leaf node have descendants that represent  alternatives available, and leaf nodes denote the result for the decisions taken. For example, considering the table used in the Naive Bayes section, the following decision tree can be created to classify if the weather conditions are suitable or not for playing tennis.

<p align="center">
<img src="https://github.com/thiago-a-souza/MachineLearning/blob/master/img/decision_tree.png">
</p>

ID3 (Iterative Dichotomiser), C4.5 (a sucessor of ID3) and CART (Classification and Regression Trees) are  the most popular decision tree algorithms. All three algorithms use a greedy strategy in top-down recursive divide-and-conquer approach. The fundamental question when creating a decision tree is: what attribute should be selected for a given node that produces a significant decision tree and minimizes the final tree depth? Answering that question requires a statistical analysis on the training set. Solutions frequently used: information gain (ID3), gain ratio (C4.5) and Gini index (CART).

### Entropy
In probability theory, entropy measures the uncertainty of a random variable, so lower entropies represent a well organized/predictable data distribution. Entropy varies from zero to one, zero representing no uncertainty and one denoting that the occurrences are the same, for example, the probability of flipping a coin and getting heads or tails is the same, so the entropy is 1. Taking that into account, in the context of decision trees, attributes with higher entropies should be chosen before lower entropies, that way leaf nodes have a final output. Entropy can be defined using the equation below, where *S* is a collection of examples with *c* different classes and *pi* as the proportion of classes labeled as *ci*.


<p align="center">
<img src="https://github.com/thiago-a-souza/MachineLearning/blob/master/img/entropy.png">
</p>

**Example:** consider the playing tennis table described in the Naive Bayes section. It has 14 examples, 9 of them are suitable for playing tennis and the remaining 5 examples are not, so the entropy for this collection can be calculated as follows:

![](/img/entropy2.png)

### Information Gain
In order to choose higher entropies for a given node, ID3 uses a measures called Information Gain, which simply calculates the entropy after removing the entropy related to a given attribute, that way the attribute with the  highest information gain is chosen. Information gain can be defined using the equation below, where S represents the entire collection, Sv is a subset of S that refers to the attribute v and Values(A) specifies the possible values for the attribute A.

<p align="center">
<img src="https://github.com/thiago-a-souza/MachineLearning/blob/master/img/information_gain.png">
</p>

**Example:**  considering the play tennis table, identify the root node of a decision tree using ID3 algorithm.


Creating the root node requires selecting the highest information gain among all attributes (i.e. outlook, temperature, humidity and wind). Consider the steps below to calculate the information gain for the wind attribute:

![](/img/step1.png)

The Entropy should be calculated for the entire collection S and the subsets weak and strong. The entropy for the collection S  considers all 14 examples, 9 of them have a "yes" class and the remaining 5 are classified as "no". Similarly, the weak subset has 8 examples, 6 classified as "yes" and 2 as "no". Finally, the strong subset has 6 examples and they are equally classified between "yes" and "no".

![](/img/step2.png)

Computing the fraction of examples whose attribute has a given value (e.g. 8 examples are weak out of 14):

![](/img/step3.png)

Determining the information gain after replacing values calculated before:

![](/img/step4.png)

Evaluating the information gain for all attributes return the values below. As result of that, the outlook should be selected as the root node, since it has the highest information gain.

![](/img/step5.png)

**Example:** identify the child attribute that should be selected when the outlook is sunny.

### Gain Ratio

### Gini Index

## SVM

# Unsupervised Learning

## K-Means

## Hierarchical Clustering





# References
(1) Mitchell, T. M. Machine Learning. McGraw Hill, 1997.

(2) Russell, Stuart J. and Norvig, Peter. Artificial intelligence: a modern approach (3rd edition). Pearson,  2009.

(3) Han, Jiawei; Pei, Jian; Kamber, Micheline. Data mining: concepts and techniques (3rd edition). Morgan Kaufmann, 2011.


