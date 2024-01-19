# Flappy Bird AI Game

This project is a Flappy Bird game implemented in Python using the Pygame library, with the added feature of an artificial intelligence (AI) that can play and learn the game. The project was created following the tutorial from https://www.youtube.com/@HashtagProgramacao.

## Game Overview

The Flappy Bird game consists of a bird that the player can control to navigate through a series of pipes. The goal is to pass through the openings between the pipes without colliding. Each successful passage increases the player's score.

## A.I. Integration

The game features an AI player capable of learning and playing the game autonomously. The AI uses a neural network created with the `NEAT` (NeuroEvolution of Augmenting Topologies) algorithm. The neural network takes into account the bird's current position and the distances to the pipes to make decisions on when to jump.

## Getting Started

To run the game, make sure you have Python installed on your machine. Additionally, you need to have the Pygame library and NEAT library installed. You can install them using the following commands:

```
pip install pygame
pip install neat-python
```

After installing the required dependencies, you can run the game by executing the `FlappyBird.py` script:

```
python FlappyBird.py
```

If you want to observe the AI playing the game and learning, set the AI_PLAYING variable to True in the script.

## Controls

`Spacebar` or `Up Arrow`: Make the bird jump (applicable when AI is not playing).

## Configuration

The AI's behavior is controlled by the configuration file config.txt, which includes parameters for the NEAT algorithm. You can adjust these parameters to observe how they affect the learning and performance of the AI.
