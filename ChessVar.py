# Author: Christopher Sexton
# Description: This python file plays chess with two players. To win this game, one player must acquire all the
# pieces of one category of pieces from the other player (i.e. player 1 collects all Rooks from player 2, player 1
# wins). The king is not a special piece in the game. There is no castling, en passant, or pawn promotion.
# Players make a move by using the make_move method inside the class ChessVar after declaring it.

class Piece:
    """
    Description: This is the Piece Class; it is a chess piece type. It will hold attribute color of the piece. It will
    communicate with the ChessVar class since each class is a piece on the board. Knowing the name and color
    attributes will help determine where each piece can be placed, and how to score the game in each method of
    the ChessVar class. Without knowing the name, the program wouldn't know which method to send the Piece
    data. Without knowing the color, the program wouldn't know who's who for the points.
    """
    def __init__(self, name, color):
        """
        Parameters:
            1. name: The name of the chess piece type (Bishop, Rook, Knight, Queen, etc...)
            2. color: Which player is whom (either White or Black)
        Attributes:
            1. name: The name of the chess piece type (Bishop, Rook, Knight, Queen, etc...) and adjusted to show 8
            characters in the string to make the display look correct.
            2. color: Which player is whom (either White or Black)
        """
        if len(color) < 1:
            self._name = '_' * (8 - len(name))  # For empty Piece positions.
        else:
            self._name = color[0] + '.' + name + ' ' * (6 - len(name))  # Name will be in this format: "X.name  ".
        self._color = color

    def get_name(self):
        """
        Parameters: Void
        Description: A method that returns the private attribute name.
        :return: A string for the piece's type
        """
        return self._name  # Returns the name attribute.

    def get_color(self):
        """
        Parameters: Void
        Description: A method that returns the private attribute color.
        :return: A string for the piece's color (either White or Black)
        """
        return self._color  # Returns the color attribute.


class ChessVar:
    """
    Description: A class that plays an abstract board game. This is a variant of chess. It will
    communicate with the Piece class since each class is a piece on the board. Knowing the name and color
    attributes will help determine where each piece can be placed, and how to score the game in each method.
    It will sort each piece type to the correct method and award points to the correct player (White or Black).
    Additionally, the Display method will display the current board of the game by using the name attribute
    in the Piece class.
    """
    def __init__(self):
        """
        Parameters: Void
        Attributes:
            1. board: The current Board and its pieces
            2. turn: Which player's turn is who's
            3. point_board: The current point board of the game (0 means the player has won)
        """
        self._board = {'a8': Piece("Rook", "Black"), 'b8': Piece("Knight", "Black"), 'c8': Piece("Bishop", "Black"),
                       'd8': Piece("King", "Black"), 'e8': Piece("Queen", "Black"), 'f8': Piece("Bishop", "Black"),
                       'g8': Piece("Knight", "Black"), 'h8': Piece("Rook", "Black"),
                       'a7': Piece("Pawn", "Black"), 'b7': Piece("Pawn", "Black"), 'c7': Piece("Pawn", "Black"),
                       'd7': Piece("Pawn", "Black"), 'e7': Piece("Pawn", "Black"), 'f7': Piece("Pawn", "Black"),
                       'g7': Piece("Pawn", "Black"), 'h7': Piece("Pawn", "Black"),
                       'a6': Piece('', ''), 'b6': Piece('', ''), 'c6': Piece('', ''), 'd6': Piece('', ''),
                       'e6': Piece('', ''), 'f6': Piece('', ''), 'g6': Piece('', ''), 'h6': Piece('', ''),
                       'a5': Piece('', ''), 'b5': Piece('', ''), 'c5': Piece('', ''), 'd5': Piece('', ''),
                       'e5': Piece('', ''), 'f5': Piece('', ''), 'g5': Piece('', ''), 'h5': Piece('', ''),
                       'a4': Piece('', ''), 'b4': Piece('', ''), 'c4': Piece('', ''), 'd4': Piece('', ''),
                       'e4': Piece('', ''), 'f4': Piece('', ''), 'g4': Piece('', ''), 'h4': Piece('', ''),
                       'a3': Piece('', ''), 'b3': Piece('', ''), 'c3': Piece('', ''), 'd3': Piece('', ''),
                       'e3': Piece('', ''), 'f3': Piece('', ''), 'g3': Piece('', ''), 'h3': Piece('', ''),
                       'a2': Piece("Pawn", "White"), 'b2': Piece("Pawn", "White"), 'c2': Piece("Pawn", "White"),
                       'd2': Piece("Pawn", "White"), 'e2': Piece("Pawn", "White"), 'f2': Piece("Pawn", "White"),
                       'g2': Piece("Pawn", "White"), 'h2': Piece("Pawn", "White"),
                       'a1': Piece("Rook", "White"), 'b1': Piece("Knight", "White"), 'c1': Piece("Bishop", "White"),
                       'd1': Piece("King", "White"), 'e1': Piece("Queen", "White"), 'f1': Piece("Bishop", "White"),
                       'g1': Piece("Knight", "White"), 'h1': Piece("Rook", "White")}
        self._turn = "White"
        self._point_board = {"White": {"Rook": -2, "Knight": -2, "Bishop": -2, "King": -1, "Queen": -1, "Pawn": -8},
                             "Black": {"Rook": -2, "Knight": -2, "Bishop": -2, "King": -1, "Queen": -1, "Pawn": -8}}
        # Score board will go back to 0 if a player wins (each point adds 1 point).

    def get_turn(self):
        """
        Parameters: Void
        Description: A method that returns the private attribute turn.
            :returns: The private attribute turn
        """
        return self._turn  # Returns the turn attribute.

    def get_game_state(self):
        """
        Parameters: Void
        Description: A method that determines who has won the game, or if the game is unfinished.
        Checks if the current player's score is 0 or not for any of the pieces.
            :returns: A string of either of the following: 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'.
        """
        for keys in self._point_board["White"]:
            if self._point_board["White"][keys] >= 0:
                return "WHITE_WON"
        for keys in self._point_board["Black"]:
            if self._point_board["Black"][keys] >= 0:
                return "BLACK_WON"
        return "UNFINISHED"

    def make_move(self, moved_from, moved_to):
        """
        Parameters:
            1. moved_from: A string that represents the square the piece is moved from
            2. moved_to: A string that represents the square the piece is moved to
        Description: Checks if the game is won by calling get_game_state. Checks if moved_from equals moved_to.
        Checks if it is this person's turn (if not, returns false). Checks if new move is out of bounds.
        Checks to see if position is not two characters. Checks to see if moved_from is empty. Determines if the move
        is legal (by calling the is_legal method). Checks if there are pieces in path. If the capture piece belongs
        to the current player and the current piece does not (this method). The capture method then removes
         any captured piece and updates the board, updates the game state if necessary by checking if the game
         is won, updates whose turn it is, and returns True.
            :returns: False for an illegal move, the piece does not belong to the player, or the game is already won;
            True otherwise
        """
        if self.get_game_state() != "UNFINISHED":  # Game is finished, no further moves.
            return False
        if len(moved_to) != 2:  # If next position is not a length of 2, not allowed.
            return False
        if (("a" > moved_to[0]) or (moved_to[0] > "h")) or ((1 > int(moved_to[1])) or (int(moved_to[1]) > 8)):
            # If next position is out of bounds, not allowed.
            return False
        if moved_from == moved_to:  # New position = next position, not allowed.
            return False
        if self._turn != self._board[moved_from].get_color():  # If it is not player's turn, should not move.
            return False
        if "_" in self._board[moved_from].get_name():  # If current position has no piece.
            return False
        if self.is_legal(moved_from, moved_to) is False:  # If the move isn't legal.
            return False
        dif_col = ord(moved_to[0]) - ord(moved_from[0])  # These next 7 lines create a unit vector, leaves 0 if 0.
        dif_row = int(moved_to[1]) - int(moved_from[1])
        largest_difference = max(abs(dif_col), abs(dif_row))
        if dif_row != 0:
            dif_row = int(dif_row/abs(dif_row))
        if dif_col != 0:
            dif_col = int(dif_col/abs(dif_col))
        if "Knight" not in self._board[moved_from].get_name():  # Checks to see if there is a Piece between moved_from
            # and moved_to, exclusive. Returns False if there is. Knight is exempt since it can jump.
            for count in range(0, largest_difference - 1):
                if '_' not in self._board[chr(ord(moved_from[0]) + dif_col) +
                                          str(int(moved_from[1]) + dif_row)].get_name():
                    return False
                if dif_row != 0:
                    dif_row += int(dif_row/abs(dif_row))
                if dif_col != 0:
                    dif_col += int(dif_col/abs(dif_col))
        if self._board[moved_to].get_color() == '':  # If next piece is empty, moves piece and changes turn.
            self._board[moved_to] = self._board[moved_from]
            self._board[moved_from] = Piece('', '')
            if self._board[moved_to].get_color() == "Black":
                self._turn = "White"
            else:
                self._turn = "Black"
            return True
        elif self._board[moved_to].get_color() == self._board[moved_from].get_color():  # Cannot jump same piece color.
            return False
        else:  # Capturing a piece of the different color.
            if self.capture(moved_from, moved_to) is False:
                return False
            else:
                if self._board[moved_to].get_color() == "Black":  # If moving to empty space, updates turn.
                    self._turn = "White"
                else:
                    self._turn = "Black"
                return True

    def is_legal(self, moved_from, moved_to):
        """
        Parameters:
            1. moved_from: A string that represents the square the piece is moved from
            2. moved_to: A string that represents the square the piece is moved to
        Description: This method determines if the position is legal based on if the piece is functioned to move
        to that spot.
            :returns: False for an illegal move, True otherwise
        """
        if "Pawn" in self._board[moved_from].get_name():  # Pawn legality.
            if self._board[moved_from].get_color() == "Black" and self._board[moved_to].get_color() != "White" \
                    and (ord(moved_from[0]) != ord(moved_to[0])):
                return False  # Other turns False if not correct movement. Next move is not opposite color.
            if self._board[moved_from].get_color() == "White" and self._board[moved_to].get_color() != "Black" \
                    and (ord(moved_from[0]) != ord(moved_to[0])):
                return False  # Other turns False if not correct movement. Next move is not opposite color.
            if "W." in self._board[moved_from].get_name():  # First turn for White.
                if int(moved_from[1]) == 2:
                    if (int(moved_to[1]) != 3) and (int(moved_to[1]) != 4):
                        return False
                    else:
                        return True
            else:  # First turn for Black.
                if int(moved_from[1]) == 7:
                    if (int(moved_to[1]) != 6) and (int(moved_to[1]) != 5):
                        return False
                    else:
                        return True
            if self._board[moved_from].get_color() == "Black" and int(moved_to[1]) != int(moved_from[1]) - 1:
                return False  # Other turns False if not correct movement. Rows up 1.
            elif self._board[moved_from].get_color() == "White" and int(moved_to[1]) != int(moved_from[1]) + 1:
                return False  # Other turns False if not correct movement. Rows down 1.
            else:
                return True
        if "Rook" in self._board[moved_from].get_name():  # Rook legality.
            if (moved_from[0] != moved_to[0]) and (moved_from[1] != moved_to[1]):
                return False
        if "Knight" in self._board[moved_from].get_name():  # Knight legality. Checks all possible places.
            possible_places = [chr(ord(moved_from[0]) - 2) + str(int(moved_from[1]) + 1),
                               chr(ord(moved_from[0]) - 2) + str(int(moved_from[1]) - 1),
                               chr(ord(moved_from[0]) - 1) + str(int(moved_from[1]) + 2),
                               chr(ord(moved_from[0]) - 1) + str(int(moved_from[1]) - 2),
                               chr(ord(moved_from[0]) + 1) + str(int(moved_from[1]) + 2),
                               chr(ord(moved_from[0]) + 1) + str(int(moved_from[1]) - 2),
                               chr(ord(moved_from[0]) + 2) + str(int(moved_from[1]) + 1),
                               chr(ord(moved_from[0]) + 2) + str(int(moved_from[1]) - 1)]
            if moved_to not in possible_places:
                return False
            if self._board[moved_from].get_color() == self._board[moved_to].get_color():
                return False
        if "Bishop" in self._board[moved_from].get_name():  # Bishop legality.
            dif_col = ord(moved_from[0]) - ord(moved_to[0])
            dif_row = int(moved_from[1]) - int(moved_to[1])
            if abs(dif_col) != abs(dif_row):
                return False
        if "King" in self._board[moved_from].get_name():  # King legality.
            if (ord(moved_from[0]) + 1 < ord(moved_to[0]) < ord(moved_from[0]) - 1) or \
                    (int(moved_from[1]) + 1 < int(moved_to[1]) < int(moved_from[1]) - 1):
                return False
        if "Queen" in self._board[moved_from].get_name():  # Queen legality.
            dif_col = ord(moved_from[0]) - ord(moved_to[0])
            dif_row = int(moved_from[1]) - int(moved_to[1])
            if abs(dif_col) != abs(dif_row):
                if (moved_from[0] != moved_to[0]) and (moved_from[1] != moved_to[1]):
                    return False
                else:
                    return True
        return True

    def capture(self, moved_from, moved_to):
        """
        Parameters:
            1. moved_from: A string that represents the square the piece is moved from
            2. moved_to: A string that represents the square the piece is moved to
        Description: This method then removes any captured piece and updates the board, updates the game state
        if necessary by checking if the game is won, updates whose turn it is, and returns True.
            :returns: False if Piece did not capture
        """
        piece_name = self._board[moved_to].get_name()
        temp = ""
        for char in piece_name[2:]:
            if char == " ":
                break
            temp = temp + char
        if "Pawn" in self._board[moved_from].get_name():
            if (ord(moved_from[0]) - 1) > ord(moved_to[0]) > (ord(moved_from[0]) + 1):
                return False
            if abs(int(moved_from[1]) - int(moved_to[1])) == 1 and (moved_from[0] == moved_to[0]):
                return False
        self._point_board[self._board[moved_from].get_color()][temp] += 1  # Adjust score board for capturing piece.
        self._board[moved_to] = self._board[moved_from]
        self._board[moved_from] = Piece('', '')
        return True

    def display(self):
        """
        Parameters: Void
        Description: A method that prints the current board.
            :returns: Strings that are printed showing the current board
        """
        count = 1
        for key in self._board:  # Prints column header.
            print(key[0] + "        ", end='')
            if "h" in key:
                print()
                break
        for key in self._board:  # Prints row header and each Piece.
            print(self._board[key].get_name() + ' ', end='')
            if (count % 8 == 0) and (count != 0):
                print(int((64 - count) / 8) + 1)
            count += 1

game = ChessVar()
while True:
    game.display()
    a = input("From: ")
    b = input("To: ")
    game.make_move(a, b)
    if game.get_game_state() == "WHITE_WON":
        print("White Won!")
        break
    elif game.get_game_state() == "BLACK_WON":
        print("Black Won!")
        break
        
