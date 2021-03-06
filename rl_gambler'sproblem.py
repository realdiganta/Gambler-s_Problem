# -*- coding: utf-8 -*-
"""
RL_Gambler'sProblem.ipynb
Author: Diganta Kalita (digankate26@gmail.com)
"""

#solving the Gambler's Problem using Value Iteration

import numpy as np
import matplotlib.pyplot as plt

def value_iteration(max_iterations=1000, prob_h=0.4, lmbda=0.9):
  lmbda = 0.9
  stateValues = [0 for i in range(0,101)]
  prob_t = 1 - prob_h
  for i in range(max_iterations):
    for state in range(1,100):
      action_space = [i for i in range(1,min(state+1, 101-state))]
      q_values = []
      for action in action_space:
        heads_value = prob_h * ((1 if state+action==100 else 0) + lmbda * stateValues[int(state+action)])
        tails_value = prob_t * (0 + lmbda * stateValues[int(state-action)])
        q_value = heads_value + tails_value
        q_values.append(q_value)
      max_q_value = np.argmax(np.asarray(q_values))
      stateValues[state] = q_values[max_q_value]
  return stateValues

def get_policy(stateValues, prob_h=0.4, lmbda=0.9):
  prob_t = 1 - prob_h
  policy = [0 for i in range(0,100)]
  for state in range(1,100):
    action_space = [i for i in range(1,min(state+1, 101-state))]
    q_values = []
    for action in action_space:
      heads_value = prob_h * ((1 if state+action==100 else 0) + lmbda * stateValues[int(state+action)])
      tails_value = prob_t * (0 + lmbda * stateValues[int(state-action)])
      q_value = heads_value + tails_value
      q_values.append(q_value)
    max_q_value = np.argmax(np.asarray(q_values))
    policy[state] = max_q_value
  return policy

stateValues = value_iteration(max_iterations=1000, prob_h=0.75, lmbda=0.9)
policy = get_policy(stateValues, prob_h=0.75, lmbda=0.9)

capital = [i for i in range(0,100)]

plt.plot(capital, stateValues[:100])
plt.xlabel('Capital')
plt.ylabel('Value Estimates')
plt.show()

plt.scatter(capital, policy)
plt.xlabel('Capital')
plt.ylabel('Final Policy(Stake)')
plt.show()

