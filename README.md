# BrickGame

```diff
- UPDATE!!!
+ Newer version is released, and code is in branch verion2.0.0. Please checkout to that branch to play the newer version with extra features!
```

A game that can be played on the Terminal based on the classic DX-Ball Game. Built using Python3 as part of DASS Assignment 2.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install colorama.

```bash
pip3 install colorama
```

## Usage

In the brickgame/ directory, run

```bash
python3 main.py
```

## How to Play ?

After running the above commands on terminal, use the following controls

 - `<Space>` to Start Game
 - `D` to move paddle to the right
 - `A` to move paddle to left
 - `Q` to Quit Game

## Gameplay

Bricks are of 5 types:

 - Strength One
 - Strength Two
 - Strength Three
 - Unbreakable
 - Explosive Bricks

Breaking each brick awards you with a score of 10 points. Break all the bricks (except Unbreakable) to win the game.

Each time a brick is destroyed, a powerup randomly appears, which can be caught by the paddle. For more details, see the PowerUps Section below.

## Screens

![Sample gameplay](https://i.ibb.co/x1yxqZ6/Screenshot-from-2021-02-17-19-32-11.png)

![Sample gameplay](https://i.ibb.co/QQ11sHJ/Screenshot-from-2021-02-17-19-32-34.png)

![Sample gameplay](https://i.ibb.co/Zc33wCZ/Screenshot-from-2021-02-17-19-33-22.png)

## Required Components

### OOP
 - Inheritance: Brick is superclass, and is inherited by various types of bricks - StrengthOne, StrengthTwo, StrengthThree, Unbreakable, Explosive
 - Polymorphism: the `activate_power()` method is different for different powerups + many other examples
 - Encapsulation: The entire game has been built on a class and object based approach
 - Abstraction: `activate_power()`, `ball_brick_collision()`, `move_balls()`, `move_paddle()`, `move_powerups()` ...

### Startup

The ball initially appears randomly on any part of the paddle

### Movement

Paddle moves in left and right direction, ball moves across the entire frame according to its velocity and objects it collides with.

### Collision Handling

 - Ball and Brick Collision handled with all 4 sides
 - Ball and Paddle Collision handled with only top side of paddle, ball changes velocity according to the part it hits
 - Ball and Wall collision handled on 3 sides of the wall, ball gets lost when hits bottom

### Bricks

 - Different Coloured Bricks are present
 - Bricks with more strength require more hits to break
 - Unbreakable Bricks implemented

### Score and Time

 - Score, Time and Lives Remaining are displayed
 - Life is lost when all balls are lost
 - User starts with 3 Lives

### Power Ups

Six PowerUps have been implemented, which appear when a brick is destroyed. Powerup is activated on catching it with paddle. All powerups are present for a specified amount of time and are lost on loss of life. The powerups are as follows:

 - Expand Paddle - Expands the paddle by a fixed size
 - Shrink Paddle - Shrinks the paddle by a fixed size, but never completely disappears
 - Ball Multiplier - Doubles all the balls present on the screen
 - Fast Ball - Increases the velocity of the Ball
 - Paddle Grab - Allows the paddle to grab one of the balls, and the ball is relaunched on will by pressing the `<SpaceBar>` key.

### Bonus

Exploding Bricks have been implemented. When the ball hits any one of these, a chain reaction is caused which breaks all the breakable bricks in its vicinity.
