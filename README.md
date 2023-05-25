# Python-Programming-using-OOPS
## Dice Game Project
### General Requirements:
- The game should have two players: a human player and a computer player. Both should
have the same functionality.
- Both players will start with a counter of 10.
- Each player will have a particular die during the entire game.
- Both players will roll their corresponding die (once per round).
- The values of the dice will be compared to determine who wins the round. The player
with the highest value wins the round.
- If the two values are equal, then there is a tie and there is no winner for that round. The
counters are not modified.
- The counter of the player who wins a round will be decremented by 1.
- The counter of the player who loses a round will be incremented by 1.
- The counter will determine who wins the game. The player whose counter reaches the
value 0 first wins the game.

### Specific Requirements:
- Interactivity
  - Before the human player rolls the die, he/she should be prompted to press any key to start the round.
- Rolling the dice
  - When a player rolls the dice, the result should be a random integer between 1 and 6 (inclusive).
- Messages
  - The game should show a descriptive message:
    - When the game starts.
    - When a new round starts.
    - When the game ends. This message should mention who won the game.
  - The game should display messages to:
    - Show the value of each die after the players roll the dice.
    - Mention the winner of the round or if there was a tie.
    - Show both counters when a round ends.

**Die**
- Each die should have:
  - A value.
    - This value should be either None (if the die has not been rolled yet) or a random integer between 1 and 6 (inclusive).
    - This attribute should not be changed outside the class. The change should be handled internally.
- Each die should be able to:
  - Roll
    - Generate a random integer between 1 and 6 (inclusive) and assign it to the value attribute.

**Player**
- Each player should have the following attributes:
  - A Die instance.
  - A Boolean value (True/False) to indicate if the player is a human or the computer.
  - A counter. The initial value should be 10.
- Each player should be able to:
  - Increment the value of the counter by 1.
  - Decrement the value of the counter by 1.
  - Roll the die.

**DiceGame**
- This class will represent a dice game.
- Each instance of the game should have the following attributes:
  - A human player instance.
  - A computer player instance.
    - This will create a relationship between these classes. A DiceGame “has a” human player and a computer player.
  - Each instance of the game should be able to:
    - Start the game (play)
      - This method will start the game logic. It should show a welcome message and create the endless loop that will continue the game until a counter has reached the value 0.
    - Start a round (play round)
      - This method should handle the main round logic. It should welcome the player to the round, roll the dice, determine the winner and loser of the round, update the counters accordingly, and show the values of the counters.
    - Determine when the game is over and stop the game.
      - The game should end when the counter of either one of the players hasreached the value 0.
      - A descriptive message should be printed before the game ends.
