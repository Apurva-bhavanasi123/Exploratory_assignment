# Exploratory_assignment
Part of the research process in random processes is first to understand what is going on at a high level and then to use this understanding in order to develop formal mathemat- ical proofs. In this assignment, you will be given several variations on a basic random process. To gain insight, you should perform experiments based on writing code to simulate the processes. (The code should be very short, a few pages at most.) After the experiments, you should use the results of the simulations to guide you to make conjectures and prove statements about the processes. You can apply what you have learned up to this point, including probabilistic bounds and analysis of balls-and-bins problems.
Consider a complete binary tree with N = 2" 1 nodes. Here n is the depth of the tree. Initially, all nodes are unmarked. Over time, via processes that we shall describe, nodes becomes marked.
All of the processes share the same basic form. We can think of the nodes as having unique identifying numbers in the range of [1, N]. Each unit of time, I send you the identifier of a node. When you receive a sent node, you mark it. Also, you invoke the following marking rule, which takes effect before I send out the next node.
• If a node and its sibling are marked, its parent is marked. If a node and its parent are marked, the other sibling is marked.
The marking rule is applied recursively as much as possible before the next node is sent. For example, in Figure 5.3, the marked nodes are filled in. The arrival of the node labeled by an X will allow you to mark the remainder of the nodes, as you apply the marking rule first up and then down the tree. Keep in mind that you always apply the marking rule as much as possible.
Now let us consider the different ways in which I might be sending you the nodes.
Process 1: Each unit of time, I send the identifier of a node chosen independently and uniformly at random from all of the N nodes. Note that I might send you a node that is already marked, and in fact I may send a useless node that I have already sent.

![image](https://user-images.githubusercontent.com/43738214/220412493-74e5f822-667c-4b96-9b54-b7fd7f67eb8b.png)


Figure 5.3: The arrival of X causes all other nodes to be marked.
Process 2: Each unit of time I send the identifier of a node chosen uniformly at random from those nodes that I have not yet sent. Again, a node that has already been marked might arrive, but each node will be sent at most once.
Process 3: Each unit of time I send the identifier of a node chosen uniformly at random from those nodes that you have not yet marked.
We want to determine how many time steps are needed before all the nodes are marked for each of these processes. Begin by writing programs to simulate the sending processes and the marking rule. Run each process ten times for each value of n in the range [10, 20]. Present the data from your experiments in a clear, easy-to-read fashion and explain your data suitably. A tip: You may find it useful to have your program print out the last node that was sent before the tree became completely marked.
1. For the first process, prove that the expected number of nodes sent is (N log N). How well does this match your simulations?
2. For the second process, you should find that almost all N nodes must be sent before the tree is marked. Show that, with constant probability, at least N – 2√Ñ nodes must be sent.
3. The behavior of the third process might seem a bit unusual. Explain it with a proof. After answering these questions, you may wish to consider other facts you could prove about these processes.




Solution:
Here I have developed the experiment using socket programming in python, by creating both server and client to exchange messages ( here nodes) and creation of tree si done by client and the marking of the binary tree is done by deamon thread as server keeps sending new nodes.
Server has three conditions on which process to run and based on the selection nodes will be sent and client keeps sending marked nodes after each execution of mark thread.
 
