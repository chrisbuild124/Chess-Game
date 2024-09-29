This is a chess game that can run on the ChessVar.py file (back-end only at the moment)! However, it displays a board in the terminal using "________" as blanks and <color>.<type> (color being B or W, and type being piece name). This is a modified chess game that assumes a winner by capturing all of an opponent's pieces of one type. 

**Here is what the board looks like at the start:**
![image](https://github.com/user-attachments/assets/93630f71-62e9-4c9e-92c8-f51825dc3df1)

**Summary of the rules of the game:**
  - This is a two person game.
  - The starting position for the game is the normal starting position for standard chess.
  - As in standard chess, white moves first. However, **The winner is the first player to capture all of an opponent's pieces of one type**, for example capturing all of the opponent's knights (of which there are     two) would win the game, or all of the opponent's pawns (of which there are eight), or all of the opponent's kings (of which there is only one), etc.
  - The king isn't a special piece in this game - there is no check or checkmate.
  -  Pieces move and capture the same as in standard chess, except that there is no castling, en passant, or pawn promotion.
  -  As in standard chess, each pawn should be able to move two spaces forward on its first move (but not on subsequent moves).

Note - Illegal moves will simply not work, and the same player who made the illegal move will need to make a different move. 

**Getting started**
  - To start the game, run the python script in the terminal (ex - python ChessVar.py).
  - Player 1 (white team) will go first. Type column name (a - h) in lowercase letters followed by row name (1-8).
  - Example - First line: "From: a2" Second line: "To: a3"
  - Player 2 (black team) will go next. Same idea as player 1 with moves.
  - Repeat until someone wins!
