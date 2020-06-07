# AI-plays-Flappy-Bird
### The project is credit to the Youtuber Tech With Tim's AI Plays Flappy Bird - NEAT Python series. I used different implementation of objects and designing on my ideas other than his. NOT A SINGLE OF LETTER OF CODE IS COPIED AND PASTED
## 1. Implement the game(DONE)
### The game is implemented Objected Oriented. Everything is a class(object). It is easy to play: click mouse to jump the bird going through pipes to survive. There is no losing state since we want to train the AI we don't want to restart the game over and over
## 2. Create neural network(DONE)
### The neural network is set up using NEAT, which is a powerful module that we just need to input the correct data, the module will set up network for us(for more details: [NEAT](https://neat-python.readthedocs.io/en/latest/config_file.html). I modified the game that it is now not playable by user, that now only my AI can play it. I set up rewards and punishments to train the AI. After a few training generations, we will get a winner who will be the GOD of Flappy Bird.
