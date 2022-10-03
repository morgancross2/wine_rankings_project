import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


def get_q1_viz(train):
    '''
    This function takes in train and returns the visualization for question 1
    in the winespectator.com dataset.
    '''
    # make it big
    plt.figure(figsize=(12,8))
    # plot hist for red wines and non-red wines
    sns.histplot(data=train[train.red == 1], x='score', color='darkred')
    sns.histplot(data=train[train.red == 0], x='score', color='pink')
    # find score averages for red and non-red wines
    red_avg = train[train.red == 1].score.mean()
    other_avg = train[train.red == 0].score.mean()
    # plot lines at those averages and label them
    plt.axvline(x= red_avg, color='red', lw=3)
    plt.text(93.2,213, '''Average Red Wine Score''')
    plt.axvline(x=other_avg, color='black', lw=3)
    plt.text(89.3,213, '''Average Non-Red Wine Score''')
    # label the graph
    plt.title('Red wines have a higher average price than other wines')
    # show the graph
    plt.show()
    
def get_q1_stats(train):
    '''
    This function takes in train and returns the statistical results for question 1
    in the winespectator.com dataset.
    '''
    # create the samples
    reds = train[train.red == 1].score
    other = train[train.red == 0].score
    # set alpha
    α = 0.05
    # run the levene test to check for equal variances
    s, pval = stats.levene(reds, other)
    # run the ttest based on the levene results
    t, p = stats.ttest_ind(reds, other, equal_var=pval > α)
    # evaluate results based on the t-statistic and the p-value
    if ((t > 0) & (p/2 < α)):
        print('''Reject the Null Hypothesis.
    Findings suggest the mean score of red wine is greater than the mean score of all other wines. ''')
    else:
        print('''Fail to reject the Null Hypothesis.
    Findings suggest the mean score of red wine is less than or equal to the mean score of all other wines.''')
    print()
    
    
def get_q2_viz(train):
    '''
    This function takes in train and returns the visualization for question 2
    in the winespectator.com dataset.
    '''
    # make it big
    plt.figure(figsize=(12,8))
    # plot the box plot
    sns.boxplot(data=train, x='score', y='price', color='darkred')
    # give it a title
    plt.title('Price and score have a positive linear relationship')
    # show it
    plt.show()
    
def get_q2_stats(train):
    '''
    This function takes in train and returns the statistical results for question 2
    in the winespectator.com dataset.
    '''
    # set alpha
    α = 0.05
    # run the spearman's correlation test on price and score
    r, p = stats.spearmanr(train.price, train.score)
    # evaluate the results against the pvalue
    if p < α:
        print('''Reject the Null Hypothesis.
    Findings suggest there is a linear relationship between a wine's score and its price.
    Spearman's Correlation was: '''+ str(round(r,3)))
    else:
        print('''Fail to reject the Null Hypothesis.
    Findings suggest there is not a linear relationship between a wine's score and its price.''')
    print()
    
def get_q3_viz(train):
    '''
    This function takes in train and returns the visualization for question 3
    in the winespectator.com dataset.
    '''
    # make it big
    plt.figure(figsize=(12,8))
    # plot it
    sns.scatterplot(data=train, x='top100_year', y='top100_rank', hue='score').invert_yaxis()
    # add a horizonal line at 50
    plt.axhline(50, color='black')
    # add space for the labels
    plt.xlim(1984.5,2020)
    # add the labels
    plt.text(1984.8,48, 'Top 50')
    plt.text(1984.8,53, 'Bottom 50')
    # give it a title
    plt.title('Higher scoring wines also rank higher')
    # move the legend
    plt.legend(loc='upper left', title='score', framealpha=1)
    # show it
    plt.show()
    
def get_q3_stats(train):
    '''
    This function takes in train and returns the statistical results for question 3
    in the winespectator.com dataset.
    '''
    # create the samples
    top = train[train.top100_rank <= 50].score
    bottom = train[train.top100_rank > 50].score
    # set alpha
    α = 0.05
    # run the levene test to check for equal variances
    s, pval = stats.levene(top, bottom)
    # run the ttest based on the levene results
    t, p = stats.ttest_ind(top, bottom, equal_var=pval > α)
    # evaluate results based on the t-statistic and the p-value
    if ((t > 0) & (p/2 < α)):
        print('''Reject the Null Hypothesis.
    Findings suggest the mean score of wines ranking in the top 50 is higher.''')
    else:
        print('''Fail to reject the Null Hypothesis.
    Findings suggest the mean score of wines ranking in the top 50 is lower or equal to the bottom 50.''')
    print()