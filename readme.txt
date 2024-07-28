red_blue_nim.py:
This program builds an agent to play a modified version of nim (called red-blue nim against a human player).
On Computer turn the best move is determined using MinMax with Alpha Beta Pruning
On Human turn the program will prompt to get the move from the human user and perform the move.
The program will alternate between these turns till the game ends and will display the winner and their score.

Usage:

To run the program, navigate to the project directory and run the following command:

python red_blue_nim.py <num-red> <num-blue> <first-player> <depth>
Example:
python red_blue_nim.py 2 4 human 1

Extra Credit:	

Reasoning behind eval function -

if the game state has either 0 red or blue marbles , score is computed as regular minmax with alphabeta pruning.
if the game state does not have an empty pile, score of the current state is calculated based on the sum of marbles in both the piles. 
if sum is even and current player is a maxplayer then score would be -2
if sum is even and current player is a minplayer then score would be 2
if sum is odd and current player is a maxplayer then score would be 2
if sum is odd and current player is a minplayer then score would be -2

if both the players play optimally, then terminal nodes would be (1,0) or (0,1). 
if terminal nodes are min nodes then scores would be -3 and -2 and max player would pick -2
if termial nodes are max nodes then scores would be 3 and 2 and min player would pick 2
the number of total steps would be the sum of marbles in both the piles - 1.
so score is defined based on the number of marbles and the type of node(minnode/maxnode).








