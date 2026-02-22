# Evolutionary Neural Game Agent

This project implements a neural network–based control policy trained using an evolutionary optimization approach within a Flappy-Bird–style game environment.

A population of neural networks is evaluated each generation. The highest-performing network is selected and used to produce the next generation through weight mutation. Over time, the agent improves its ability to survive and successfully navigate obstacles.

## Method

- A fixed-size population of policy networks is initialized.  
- Each network interacts independently with the game environment.  
- Performance is measured using a reward signal based on survival and obstacle navigation.  
- The best-performing network is selected.  
- Mutated copies of the best network form the next generation.  
- The strongest model across all generations is saved.  

## State Representation

The policy network receives:

- Bird vertical position  
- Bird velocity  
- Pipe horizontal position  
- Pipe gap center position  

The network outputs a probability used to decide between two actions:

- Flap  
- No flap  

This project explores neural network policy representation, evolutionary weight mutation, and reward-driven optimization within a dynamic game environment.
