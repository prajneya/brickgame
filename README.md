# BrickGame

A game that can be played on the Terminal based on the classic DX-Ball Game. Built using Python3 as part of DASS Assignment 2.

Update: Version 2 of the Game. Added new features as part of Assignment 3

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

 New Update:

 - `Y` to skip levels

## Gameplay

Bricks are of 5 types:

 - Strength One
 - Strength Two
 - Strength Three
 - Unbreakable
 - Explosive Bricks

 New Update:

 - Rainbow Bricks

Breaking each brick awards you with a score of 10 points. Break all the bricks (except Unbreakable) to win the game.

Each time a brick is destroyed, a powerup randomly appears, which can be caught by the paddle. For more details, see the PowerUps Section below.

## Screens

![Sample gameplay](https://i.ibb.co/x1yxqZ6/Screenshot-from-2021-02-17-19-32-11.png)

![Sample gameplay](https://i.ibb.co/QQ11sHJ/Screenshot-from-2021-02-17-19-32-34.png)

![Sample gameplay](https://i.ibb.co/Zc33wCZ/Screenshot-from-2021-02-17-19-33-22.png)

New Update:

![Sample gameplay](https://i.ibb.co/1v1c1kc/guns.png)

![Sample Gameplay](https://i.ibb.co/10qKXkt/Screenshot-from-2021-03-17-22-35-42.png)

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

New Updates:

### Levels

A total of 4 levels have been implemented now

### Falling Bricks - Time Attack

After a period of 10 seconds, bricks start falling down. You have to destroy all bricks before touchdown

### Rainbow Bricks

A new type of brick has been introduced, that keeps changing colour (and strength) until it is hit.

### Powerups 2.0

Powerups now attain the velocity of the ball and have a gravity effect

### GUNS!

A new powerup allows the paddle to have shooting capabilities for a limited amount of time

### BOSS Enemy

Last level involves the BOSS Fight, where you have to destroy a UFO to win the match. Health Bar is also displayed. Careful, the UFO can spawn bricks around itself as a defense strategy.

### Bonus

Fireball Powerup: New powerup that gives the ball the ability to explode bricks it touches alongwith the bricks in its proximity
Sounds Added