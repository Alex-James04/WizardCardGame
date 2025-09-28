# Wizard Strategy Bot Implementation Guide

### Overview
- This file provides a guide to anyone implementing their own version of the player.py file and the contained Player class.
- The implementation of Wizard in this repo was done such that any object following the interface designed in the player.py file can be used to perform actions in the game.
- The first thing to do when creating a strategy bot is to create a new Python file and copy everything from player.py into it - this file will be where all the bot's logic lives and the file that will be used to simulate the game with.
- Do not change any of the method headers or return types - additional private methods may be created, but only the provided four methods directly interact with the implementation of the game provided.

### Player Interface
- The player class provided is what's called an interface, meaning it shows the minimum required methods that need to be implemented for a class to be usable in the implementation of the game.
- The interface includes a constructor (should be left as-is) and three methods that are used in the game to prompt the player for some action, listed as follows:
  - setTrumpSuit - this is called during the game when the led suit for a trick is a jester and the dealer must be prompted to choose a suit, so it is required to return one of the four main card suits (DO NOT RETURN THE NULL SUIT).
  - makeBid - this is called during the game when a player must be prompted to make their bid for how many tricks they think they can win in the hand, so it is required to return an integer between 0 and the total number of tricks available in the round.
  - playCardFromHand - this is called during the game when a trick is being played out and a player must select a card from their hand to play, so it is required to return a card from the player's hand (accessible through the GameState object, as shown in the interface).

### Game-State Object
- The player interface takes in a GameState object in each of its callable methods.
- The GameState object contains all the information about the game that the player knows when they are prompted to make a move.
- The specific information that a player has in the GameState when each function is called varies - for example, when setTrumpSuit() is called, the player doesn't know yet what the lead suit of the trick is because no tricks have been played yet.
- It is recommended to view the game_state.py file to get an understanding of all the accessible information and to logically consider what information will be available in each player method that needs to be implemented.
- It is also recommended to, when developing a custom player/strategy bot, to simulate individual games and print out information at each stage of the game, most importantly the information contained in the Game-State object when the player is prompted for some action.

### Additional Information/Requirements
- As mentioned before, the setTrumpSuit MUST return one of Hearts, Diamonds, Spades, and Clubs - not the NULL suit built into the card_attributes.py file and Suit enum class that is reserved for Wizards and Jesters
- The makeBid value returned should be between 0 and the total number of tricks available (accessible through the GameState object), but the game won't break if a value outside of that range is returned, it will just guarantee that the player will lose points for that round.
- ***THE MOST IMPORTANT IMPLEMENTATION REQUIREMENT*** - The playCardFromHand() method MUST implement the logic to follow the led suit if any card of the led suit is in the player's hand, with the exception of playing Wizards and Jesters, as this is not checked in the game and must be handled by the player.
