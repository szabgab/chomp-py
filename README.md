
Description of the game: https://en.wikipedia.org/wiki/Chomp

* Something representing the board and who plays now.
* Simple code checking if a board is a loosing situation or winning situation.
* Calculate all the Winning situations from 0 to the current position.
* If the current position is a winning position, make the move that leads to a losing position.
* If the current position is a losing position, make the smallest move possible.  


A losing situation is one that no matter what the current player does the other one can win.
A winning situation is one that the current player **can** make a move to place the other player in a losing situation.

```
x
```

Is a losing situation by definition.

```
xx
```
Is a winning situation as removing (1, 2) leads to a losing situation.

```
x....x
```
Is a winning situation as removing (1, 2) leads to a losing situation.

```
x
.
.
.
x
```
Same in the above case.

If there are n in the first row and then there are n-1 additional rows each one with 1 in it,
that's a losing situation. The current player can either remove from the first row
or from the first column. The other player will do the other operation. So after these two moves
we are again in a similar situation. Having a single chocolate is a losing situation.

 
A full NxN (N > 1 )is a winning situation as one can take (2,2) and get to the previous construct.


Try:

```
python chomp/game.py 3 5
```
