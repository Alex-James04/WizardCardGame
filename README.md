# Wizard Card Game Competition and Reinforcement Learning

### Overview
- This project is an attempt to code the card game Wizard in Python.
- One of the main motivations behind this project is to host a competition (among my friends) to see who can program the best strategy/bot for the game, playing them against each other thousands of times and tracking who wins the most games.
- Using the bots created in the tournament, I will build and train a multi-agent DQN model to play (and ideally win) Wizard games.
- A Wizard agent has been built with reinforcement learning, and even DQN specifically, before, but this approach will be different by independently training the bidding and playing models rather than training them simultaneously.

### Additional Information
- The first stage of this project, the building of the game, is completed and built with an object-oriented structure (Java-esque) in order to easily simulate many instances of the game and pass state information to the player bots and model.
-  The "player.py" file and Player class effectively serve as an interface of creating a strategy-bot for the game, with all the logical decision-making coming in the form of setting a trump card, making a bid, and playing a card when prompted, with the environmental information coming in the form of a GameState object.

### Future Applications
- My personal plan for this project is to use the agent to uncover some optimal strategy to play Wizard to maximize wins (ideally against my friends and their bots).
- This project could also likely be expanded, with more people creating bots using the player class as an interface and simulating games with them.
- Other machine learning algorithms, like PPO, could also be trained using this implementation of the game, and it would be especially interesting to see how different algorithms compare to my model's performance.

### Contact

Email: Ajames04321@gmail.com
