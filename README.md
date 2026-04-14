# Space Shooter

A simple 2D space shooter built with [Pygame Zero](https://pygame-zero.readthedocs.io/) as an educational project for learning game development in Python.

![Gameplay](space.gif)

## About

This project is designed to demonstrate core game development concepts using Pygame Zero — a beginner-friendly framework built on top of Pygame. The code covers:

- **Game loop** — drawing, updating state, and handling input each frame
- **Actors** — sprites with position, angle, and velocity
- **Collision detection** — laser hits and player collisions
- **Randomness** — UFO spawning and movement direction changes
- **Sound effects** — lasers, explosions, shield hits, and game over
- **Animation** — frame-based explosion sequences

## Gameplay

Pilot your spaceship and destroy incoming UFOs before they collide with you. You start with **3 lives**. The game ends when you run out.

| Action | Key |
|---|---|
| Rotate left | `A` |
| Rotate right | `D` |
| Accelerate | `W` |
| Decelerate | `S` |
| Shoot laser | `Space` |

- Each UFO destroyed earns **10 points**
- UFOs wrap around the screen edges
- A **GAME OVER** screen is shown when all lives are lost

## Requirements

- Python 3.x
- Pygame Zero

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Game

```bash
python main.py
```

## Project Structure

```
main.py          # All game logic
images/          # Sprites (ship, UFOs, lasers, explosions, lives)
sounds/          # Sound effects
requirements.txt
```

## Assets

Sprites and sounds from [Kenney.nl](https://kenney.nl/) — free game assets.
