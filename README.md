# Chess Coverage Analyzer

**Chess Coverage Analyzer** is a Python script that calculates the coverage of squares on a chessboard based on the positions of both white and black pieces. The output shows which squares are under attack or defended by each player's pieces.

### Features

- **Chess Piece Representation**: Uses Unicode symbols for chess pieces (e.g., `♔`, `♛`, `♟`, etc.) or English letters.
- **Piece Movement Simulation**: Simulates the attack/defense range for all chess pieces (king, queen, bishop, knight, rook, and pawns).
- **Board Coverage**: The script outputs two 8x8 boards showing the squares controlled by black and white pieces respectively.
- **Customizable**: Works with any 8x8 board configuration.
- **User-friendly Display**: The board can be printed in both normal and prettified formats, making it more readable.

---

## How It Works

1. **Input**: The chessboard is represented as a list of strings where:

   - **Lowercase letters** (`r`, `n`, `b`, `q`, `k`, `p`) or **Unicode symbols** (`♖`, `♘`, `♗`, `♕`, `♔`, `♙`) represent white pieces.
   - **Uppercase letters** (`R`, `N`, `B`, `Q`, `K`, `P`) or **Unicode symbols** (`♜`, `♞`, `♝`, `♛`, `♚`, `♟`) represent black pieces.
   - `.` represents an empty square.
   - `?` represents uncovered square.
2. **Output**: The script generates two boards:

   - **Black**: Squares covered by black pieces.
   - **White**: Squares covered by white pieces.
3. **Print Formats**: The boards can be displayed in two ways:

   - **Normal Format**: A simple board grid with covered squares represented by the piece symbol.
   - **Prettified Format**: A more structured board with columns labeled as `A-H` and rows `1-8`.

---

## Sample Input/Output with Unicode symbols

### Input Example:

```python
chess_board = [
    "♜♞♝♛♚♝♞♜",
    "♟♟♟♟♟♟♟♟",
    "........",
    "........",
    "........",
    "........",
    "♙♙♙♙♙♙♙♙",
    "♖♘♗♕♔♗♘♖",
]
```

### Output Example (normal format):

```bash
White side board coverage:

????????
????????
????????
????????
????????
........
♙♙♙♙♙♙♙♙
♖♘♗♕♔♗♘♖
---------------------
Black side board coverage:

♜♞♝♛♚♝♞♜
♟♟♟♟♟♟♟♟
........
????????
????????
????????
????????
????????
---------------------
```

### Output Example (prettified format) black side:

```bash
Black side board coverage (prettified):

   A     B     C     D     E     F     G     H
------------------------------------------------
|     |     |     |     |     |     |     |     |
|  ♜  |  ♞  |  ♝  |  ♛  |  ♚  |  ♝  |  ♞  |  ♜  |  1
|     |     |     |     |     |     |     |     |
------------------------------------------------
|     |     |     |     |     |     |     |     |
|  ♟  |  ♟  |  ♟  |  ♟  |  ♟  |  ♟  |  ♟  |  ♟  |  2
|     |     |     |     |     |     |     |     |
------------------------------------------------
|     |     |     |     |     |     |     |     |
|  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  3
|     |     |     |     |     |     |     |     |
------------------------------------------------
|     |     |     |     |     |     |     |     |
|  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |  ?  |  4
...
```

## Note:

In the **pretified format** example above, the board layout doesn't appear exactly as it does in the terminal output. This is because Unicode characters take up more space, which affects the alignment and overall appearance when displayed here.

## How to Run

1. Clone the repository:
   ```bash
    git clone https://github.com/CodeVnebula/chess-coverage-analyzer.git
   ```
2. Navigate to the project directory:
   ```bash
    cd chess-coverage-analyzer
   ```
3. Run the script:
   ```bash
    python chess_coverage_analyzer.py
   ```

## File Structure

* **`chess_coverage_analyzer.py`** : Main script to calculate and display coverage.
* *(Optional)* Add any additional scripts or test cases.

## Contributing

Contributions are welcome! Feel free to:

* Submit issues for bugs or feature requests.
* Fork the repository and submit a pull request for enhancements.
