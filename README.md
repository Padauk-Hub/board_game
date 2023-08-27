# Board Game
## Motivation
When I write TicTacToe game, I found they check all the possible combination of the winning moves. It Ok for Tic Tac Toe because it has only 8 winning moves. But in the GoMokhu Game( Like TicTacToe but it play `9*9, 11*11 or 15*15` board and winning state is 5 in a line) so there are many possible winning moves. I want to check out the winning moves that contain. That is the story behind the project.

## Steps
1. `ngram_v2.py`  in this program, The problem I try to solve is that from the given array of length N, we only look the $\pm$ of window size (5 in Gomokhu) from the current move.
2. `diagonal.py` in this program, the diagonal line pass through the given point
3. `anti_diagonal.py` in this program, the anti diagonal line pass through the given point. This is more challenge than diagonal.py
4. `check.py` it is the class.
	for `check win` function we need to know the horizontal, vertical, diagonal and anti-diagonal line pass through it. That is why I try to solve early. From each line, I crop the N-gram with window size. for each window. I check each items.
5. `board_game.py` This make to create a game.
6. `TicTacToe.py` The use of `board_game.py`

## Future Work
- [ ] Gomokhu game
- [ ] Board class and Game class must be suppurated
- [ ] Draw class diagram for this project.
