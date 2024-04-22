# Minesweeper
Minesweeper - A complex and stegic video game.

**Minesweeper Rules**
- Board Layout: The game board is a grid composed of cells arranged in rows and columns. Some cells contain mines (bombs), while others are empty.
- Cell States: Each cell on the board can have three states:
- Covered: The cell is hidden and has not been revealed yet.
- Revealed: The cell has been clicked and its contents (mine or number) are visible.
- Flagged: The player can mark a cell they believe contains a mine with a flag.
- Numbers: When an empty cell is revealed, it may display a number indicating how many mines are adjacent to it. This number can range from 0 to 8, depending on the number of neighboring cells that contain mines.
- Winning the Game: The player wins the game by revealing all the empty cells without detonating any mines.
- Losing the Game: The player loses the game if they reveal a cell containing a mine.
- Controls:
- Reveal a Cell: The player clicks on a covered cell to reveal it.
- Flag a Cell: The player can mark a covered cell with a flag if they suspect it contains a mine.
- Adjacent Cells: Each cell is surrounded by up to 8 adjacent cells (diagonal, horizontal, and vertical neighbors).
- Flagging Mines: Flagging a cell can help the player keep track of potential mines, but it doesn't affect the gameplay outcome directly.
- Time and Scores: The game may track the time taken to complete the game and/or the number of moves made, which can be used to compare scores with other players.
- Restart: Players can restart the game at any time if they lose or want to try again.

**Code Explanation**
- The Minesweeper class takes three parameters: width (the width of the game board), height (the height of the game board), and numBombs (the number of mines to be placed on the board).
- The create_board method is responsible for randomly placing the mines on the game board. It uses nested loops to iterate over each cell and checks if a mine is already present. If not, it places a mine and updates the neighboring cells' clue values.
- The create_gui method sets up the GUI using tkinter. It creates a window, initializes a 2D array of buttons representing the cells on the game board, and displays them on the window.
- The click method is called when a button representing a cell is clicked. If the clicked cell contains a mine, the game_over method is called. Otherwise, the reveal method is called to uncover the clicked cell and its neighboring cells. If all non-mine cells are revealed, the check_win method is called to determine if the player has won the game.
- The reveal method uncovers cells on the game board. It checks if the cell is within the bounds of the board and not already revealed. If the cell contains a clue of 0, it calls itself on its neighboring cells.
- The game_over method is called when the player uncovers a cell containing a mine. It reveals all the mines on the game board, displays an error message, and destroys the game window.
- The game_won method is called when the player uncovers all non-mine cells.
- The check_win method checks if all non-mine cells have been revealed. If so, it returns True, showing that the player has won the game.
