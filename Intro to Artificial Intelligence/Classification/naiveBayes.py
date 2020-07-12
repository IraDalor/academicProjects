# naiveBayes.py
# -------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and Pieter 
# Abbeel in Spring 2013.
# For more info, see http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html

import util
import classificationMethod
import math

class NaiveBayesClassifier(classificationMethod.ClassificationMethod):
    """
    See the project description for the specifications of the Naive Bayes classifier.

    Note that the variable 'data' in this code refers to a counter of features
    (not to a raw samples.data).
    """
    def __init__(self, legalLabels):
        self.legalLabels = legalLabels
        self.type = "naivebayes"
        self.k = 1 # this is the smoothing parameter, ** use it in your train method **
        self.automaticTuning = False # Look at this flag to decide whether to choose k automatically ** use this in your train method **

    def setSmoothing(self, k):
        """
        This is used by the main method to change the smoothing parameter before training.
        Do not modify this method.
        """
        self.k = k

    def train(self, trainingData, trainingLabels, validationData, validationLabels):
        """
        Outside shell to call your method. Do not modify this method.
        """

        # might be useful in your code later...
        # this is a list of all features in the training set.
        self.features = list(set([f for data in trainingData for f in data.keys()]));

        if (self.automaticTuning):
            kgrid = [0.001, 0.01, 0.05, 0.1, 0.5, 1, 2, 5, 10, 20, 50]
        else:
            kgrid = [self.k]

        self.trainAndTune(trainingData, trainingLabels, validationData, validationLabels, kgrid)

    def trainAndTune(self, trainingData, trainingLabels, validationData, validationLabels, kgrid):
        """
        Trains the classifier by collecting cnt over the training data, and
        stores the Laplace smoothed estimates so that they can be used to classify.
        Evaluate each value of k in kgrid to choose the smoothing parameter
        that gives the best accuracy on the held-out validationData.

        trainingData and validationData are lists of feature Counters.  The corresponding
        label lists contain the correct label for each data.

        To get the list of all possible features or labels, use self.features and
        self.legalLabels.
        """

        best_acc = -1
        prev = util.Counter()
        com_cnt = util.Counter()
        com_prob = util.Counter()


        for i in range(len(trainingData)):
            data = trainingData[i]
            lbl = trainingLabels[i]
            prev[lbl] += 1
            for k, v in data.items():
                com_cnt[(k,lbl)] += 1
                if v > 0:
                    com_prob[(k, lbl)] += 1

        for k in kgrid:
            cnt = util.Counter()
            con_prob = util.Counter()
            prior = util.Counter()

            for ky, v in prev.items():
                prior[ky] += v
            for ky, v in com_cnt.items():
                cnt[ky] += v
            for ky, v in com_prob.items():
                con_prob[ky] += v
            for lbl in self.legalLabels:
                for feat in self.features:
                    con_prob[(feat, lbl)] += k
                    cnt[(feat, lbl)] += 2*k

            prior.normalize()
            for x, c in con_prob.items():
                con_prob[x] = c * 1.0 / cnt[x]

            self.prior = prior
            self.con_prob = con_prob
            predictions = self.classify(validationData)
            accuracyCount =  [predictions[i] == validationLabels[i] for i in range(len(validationLabels))].count(True)

            if accuracyCount > best_acc:
                bestParams = (prior, con_prob, k)
                best_acc = accuracyCount
        self.prior, self.con_prob, self.k = bestParams

    def classify(self, testData):
        """
        Classify the data based on the posterior distribution over labels.

        You shouldn't modify this method.
        """
        guesses = []
        self.posteriors = [] # Log posteriors are stored for later data analysis (autograder).
        for data in testData:
            posterior = self.calculateLogJointProbabilities(data)
            guesses.append(posterior.argMax())
            self.posteriors.append(posterior)
        return guesses

    def calculateLogJointProbabilities(self, data):
        """
        Returns the log-joint distribution over legal labels and the data.
        Each log-probability should be stored in the log-joint counter, e.g.
        logJoint[3] = <Estimate of log( P(Label = 3, data) )>

        To get the list of all possible features or labels, use self.features and
        self.legalLabels.
        """
        logJoint = util.Counter()
        for lbl in self.legalLabels:
            logJoint[lbl] = math.log(self.prior[lbl])
            for k, v in data.items():
                if v > 0:
                    logJoint[lbl] += math.log(self.con_prob[k,lbl])
                else:
                    logJoint[lbl] += math.log(1-self.con_prob[k,lbl])
        return logJoint

    def findHighOddsFeatures(self, label1, label2):
        """
        Returns the 100 best features for the odds ratio:
                P(feature=1 | label1)/P(feature=1 | label2)

        Note: you may find 'self.features' a useful way to loop through all possible features
        """
        featuresOdds = []

        for ft in self.features:
            featuresOdds.append((self.con_prob[ft, label1]/self.con_prob[ft, label2], ft))
        featuresOdds.sort()
        featuresOdds = [ft for v, ft in featuresOdds[-100:]]

        return featuresOdds
