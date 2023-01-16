# Snake
Simple snake game using some DDD and Clean Architecture methods

# Dependencies
`pip3 install pynput`

# Usage
1. Open two terminals and place them side by side
2. start server in one terminal:
   `python3 server.py`
3. start client in another terminal:
   `python3 client.py`

# Following features implemented
- collision checking with walls
- collision checking of the snake against itself
- update rate 0.5 s
- a user can control the snake over udp with w, a, s ,d keys
- each 5 s client sends to server random valid food position
- playfield size can be changed with width and heigh variables in the code
- initial snake has 3 elements (head, tail, tail)
- \# for walls, * for food, h for head, s for tail
