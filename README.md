
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Space Racers
## CS110 Final Project  Fall, 2024

## Team Members

Landon Kozdemba

***

## Project Description

My project will be a game where you control a spacecraft through the vast darkness of space.  Your goal is to make it as far as you can while avoiding space debris and collecting fuel to make sure your spacecraft can fly.  Your score will accumulate with each fuel can you collect, and the highest score will be saved in a leaderboard shown to the player.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Title Screen
2. Moveable Player
3. Real-Time Score Tracker
4. Obstacles with Hitboxes
5. Game Over Screen
6. Leaderboard Tracker

### Classes

- Player: This is the character that the player will control during the game
- Obstacle: These are the objects that the player must avoid to stay alive
- Fuel: These are the energy sources that the player must collect to stay alive

## ATP
|Description | Steps | Results |
|---|---|---|
| 1. Verify that the user can start the program up | Open terminal, go to the project folder, type "python main.py", and click on start button | Character will appear on screen, and the game will start |
| 2. Verify that the user can move left, right, up, and down | Start the game, press the left arrow key and verify that the player moves left, press the right arrow key and verify that the player moves right, press the up arrow key and verify that the player moves up, press the down arrow key and verify that the player moves down | Character will move left, right, up, and down in response to the arrow keys |
| 3. Verify that the collisions between the player and the obstacles are correct | Start the game, make contact with a meteor, verify that the game will end | User will receive a game over |
| 4. Verify that the collisions between the player and the fuel cans are correct | Start the game, make contact with a fuel cane, verify that the fuel can disappears and the score adds by one | Fuel can will disappear and the score will increase by one |
| 5. Verify that the collisions between the fuel can and the bottom of the screen are correct | Start the game, allow the fuel can to leave the bottom of the screen, verify that the game will end | User will receive a game over |
