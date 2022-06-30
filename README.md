# Snake
Runs a game of the classic game Snake. This program's GUI is implemented using PyQt5. The snake itself is a linked list of coordinates, which is appended to whenever the snake eats food, which spawns randomly on a non-snake tile. If the snake runs into itself or the walls, it will turn red and the game will end. Either WASD or arrow key inputs are accepted, and a pause function is included.

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/56368354/176570913-2304fc56-34d0-4f4d-b65e-6000ac7b044e.gif)

# Future Work
This project uses simple shape drawing functionality from PyQt5, which while functional, is far from aesthetically pleasing. Additionally, this method makes it difficult to distinguish where parts of the snake are, and could be improved with custom snake art that does not occupy the entire tile. However, this would require a check for the front and back of the snake, as well as additional code to determine which direction the snake's body should be facing.

A multiplayer version of this game can be created using sockets, but would require a conversion into a more web-friendly language like javascript. Each player would need a socket connection to a host that manages the actual program. The underlying game code would not need significant logical changes aside from the additional linked lists for the new snakes.
