# PokerProject
Poker simulation and solver project

## GTO approach and considerations:


## Model layout for aiming to determine villain's range
* Start with a tree with branches representing possible hands
* After certain actions are taken branches get eliminated from consideration
* The hands that are left are the villain's range
* Once we have the villains range, we determine our sizing/approach


## Reinforcement learning terminology
1. Agent: the learner and the decision maker
2. Environment: where the agent learns and decides what actions to perform
3. Action: a set of actions which the agent can perform
4. State: the state of the agent in the environment
5. Reward: for eac action selected by the agent the environment provides a reward. Usually scalar value 
6. Policy: the decision making function (control strategy) of the agent, which represents a mapping from situations to actions.
7. Value function: mapping from states to real numbers, where the value of a state represents the long-term reward achieved starting from that state, and executing a particular policy.
8. Function approximator: refers to the problem of inducing a function from training examples. Standard approximators include decision trees, neural netwroks, and nearest-neighbor methods
9. Markov decision process (MDP): A probabilistic model of a seuqential decision problem, where states can be percieved exactly, and the current state and action selected determine a probability distribution on future states. Essentially, the outcome of applying an action to a state depends only on the current aciton and state (and not on preceding actions or states)
10. Dynamic programming (DP): class of solution methods for solving sequential decision problems with a compositional cost structure
11. Monte Carlo methods: class of methods for learning of value functions, which estimates the value of a state by running many trial starting at that state, then averages the total rewards recieved on those trials
12. Temporal Difference (TD) algos: class of learning methods, based on the idea of comparing temporally successive predicitions. Possible the single most fundamental idea in all of reinforcement learning
13. Model: Agent view of environment, which maps state-action pairs to probability distributions over states. Note that not every reinforcement learning agent uses a model of its environment


## Model-based vs Model-free RL
### Model-based RL
#### Markov decision process (for probabilistic problems, dice roll, poker, etc) (eg Actor critic)
    * Means there is a probability: deterministic probability of moving from state *s* to state *s'*, given action *a* 
    * This probability is **known**, it does not depend on the previous actions/states, only the current one. Purely the chance of going from the current state to next state
    * If this true of our model we gain the ability to use two techniques:
        1. Policy Iteration: <sub>0</sub>(s,a)
        2. Value Iteration: V(s)
    * These tools allow you to walk itteratively through the game or decision process, and then assesing that value, and refining by iteration
* Special case of dynamic programming and Bellman optimality; Using dynamic programming on the value function, value iteration
#### Nonlinear dynamics (for deterministic problems, self driving car) (eg Deep MPC)
* d/dt x = f(x(t), u(t), t)
* Optimal control & Hamilton, Jacobi, Bellman equation
* Relies on bellman optimallity, and you can use dynamic programming to solve optimal nonlinear control problems 
* Its hard to do Hamilton Jacobi, Bellman for high dimensional system, such as chess, etc


### Model-free RL 
#### Gradient free (eg DQN)
* It becomes difficult to have the gradient used of an action of an opponent 
##### Off policy
* Incorporating suboptimal moves to try to learn information about the system; they may not neccessairly be the best move or a good move even
* Q(s,a) Q Learning; good way to learn when you have no idea of the mmodel and you can be off policy
* This is good for imitation learning as well

##### On policy (eg Deep Policy Network)
* Always play best game possible; you always use the best policy to attempt to get the most reward possible every game
* TD(0) ... TD(inf) = MC TD-lambda SARSA

#### Graident based
* Will usually be the fastest most efficient way to perform Model-free RL
* Update the parameters of policy/value function using gradient optimization (gradient descent etc)
* Theta new = Theta old + alphaR* Theta
* When you have the ability to do this it will be the fastest option by far; even than dynamic programming


 
## Markov decision process
We are trying to learn:
* The optimal value function
* The optimal policy function
We need to know beforehand:
* R(*s'*, *s*, *a*) = Pr(r<sub>k+1</sub> | s<sub>k+1</sub> = *s'*, s<sub>k</sub> = s, a<sub>k</sub> = a)
* P(*s'*, *s*, *a*) = Pr(s<sub>k+1</sub> = *s'*, s<sub>k</sub> = s, a<sub>k</sub> = a)
* We assume we have a model of how the environment works, we assume the environment evolves due to a markov decision process
* Given current state S and current action A there is some probability that the environment will go to state *s'*
* What is the probability of reward given current state S and current action A, assuming you move to state *s'* in the next state



## Libratus methodology
* Methodology is applied to imperfect-information games, any 

### General
* This methodology can be applied to any imperfect-information game
* Any strategic interaction that involves hidden information, eg: security interactions and negotiations
* Imperfect information games: poker is the go-to in AI/game theory, because it captueres the challenge of imperfect information


### Heads-up No-Limit Texas Hold'em 
* Has become the main benchmark and challenge problem in AI for imperfect-information games
* No-limit betting = continous action space
    * Technically, 10^161 situations since bets must be integers
* The most popular variant of poker in the world
* Two-player variant allows an objective winner to be determined
* No prior AI has been able to beat top humans


### Papers to observe
Recognized challenge problem in game theory and AI
* Nash 1950
* Kuhn 1950
* Waterman 1970
* Caro 1984
* Pfeffer & Koller 1995
* Billings et al. 1998
* Schaeffer et al. 1999
* Shi & Littman 2001
* Billings et al. 2003
Tremendous progress in last 12 years
* Rhode Island Hold'em Solved (10^9 decisions), Gilpin & Sandholm 2005
* Limit Texas Hold'em Essentially Solved (10^13 decisions), Bowling et al. 2015


