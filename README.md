# ♟️ ChessVar — A Chess Variant

A two-player, terminal-based chess game with a unique win condition:  
**Capture all of your opponent’s pieces of a single type to win.**

---

## Overview

This is a chess variant that runs in the terminal via `ChessVar.py`.  
The board is printed with `"________"` as empty squares and displays pieces using their color (`B` or `W`) and type (`Pawn`, `Knight`, etc.).

- There's **no check or checkmate** — instead, eliminate all of one piece type from your opponent to win the game.

---

## Starting Board

![image](https://github.com/user-attachments/assets/93630f71-62e9-4c9e-92c8-f51825dc3df1)
> At game start, the board resembles a standard chess setup.

---

## How to Win

> **Capture all of one type of your opponent’s pieces.**  
For example:
- Capture both of your opponent’s knights (2 total)
- Or all 8 pawns
- Or only the king

---

## Rules Recap

- **2 players**
- **Standard starting chess position**
- **White moves first**
- **No check, checkmate, castling, en passant, or promotion**
- **Valid moves follow standard chess rules**
- **Illegal moves are ignored, and the player must try again**

---

## Getting Started

1. Run the script in a terminal:
   ```bash
   python ChessVar.py
   ```

2. Follow the prompts:
   - **Player 1 (White)** goes first
   - Input format:
     ```
     From: a2
     To: a3
     ```
   - **Player 2 (Black)** follows with the same format.

3. Continue alternating turns until one player captures all of a specific type of piece.

---

Built by Chris Sexton
