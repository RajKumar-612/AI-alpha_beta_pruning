import sys

MAX, MIN, depth = 1000000000, -1000000000, 1000000000


class Node:
    def __init__(self, parent, maxPlayer, red, blue, depth):
        self.parent = parent
        self.maxPlayer = maxPlayer
        self.red = red
        self.blue = blue
        self.depth = depth
        self.score = 0


def eval(node):
    if (node.red+node.blue) % 2 == 0:
        if node.maxPlayer:
            node.score = -2
        else:
            node.score = 2
    else:
        if node.maxPlayer:
            node.score = 2
        else:
            node.score = -2
    return node


def minmax(node, alpha, beta):

    # Terminating condition. i.e leaf node is reached
    if node.red == 0 or node.blue == 0:
        node.score = node.red*2+node.blue*3
        if node.maxPlayer == False:
            node.score = node.score*-1
        return node
    if int(node.depth) == int(depth):
        node = eval(node)
        if int(depth) == 0:
            if int(node.red) > int(node.blue):
                node.red = node.red-1
            else:
                node.blue = node.blue-1

        return node

    children = [Node(node, not node.maxPlayer, node.red-1, node.blue, node.depth+1),
                Node(node, not node.maxPlayer, node.red, node.blue-1, node.depth+1)]
    bestNode = children[0]
    if node.maxPlayer:
        best = MIN
    else:
        best = MAX
    for child in children:
        val = minmax(child, alpha, beta)
        if node.maxPlayer:
            if val.score > best:
                best = val.score
                bestNode = val
            alpha = max(alpha, best)
        else:
            if val.score < best:
                best = val.score
                bestNode = val
            beta = min(beta, best)
        # Alpha Beta Pruning
        if beta <= alpha:
            break
    node.score = bestNode.score
    if node.parent == None:
        return bestNode
    return node


def declarewinner(red, blue, player):
    print("Game over Red:", red, ",Blue:", blue)
    if player == 'computer':
        print("Computer won with a score of ", (red*2+blue*3))
    else:
        print("Human won with a score of ", (red*2+blue*3))


if __name__ == "__main__":

    player = 'computer'
    red, blue = int(sys.argv[1]), int(sys.argv[2])
    if len(sys.argv) >= 4:
        player = sys.argv[3]
    if player.isdigit():
        depth = player
        player = 'computer'
    if len(sys.argv) >= 5:
        depth = sys.argv[4]
    while (red > 0 and blue > 0):
        print("Red:", red, ", Blue:", blue)
        if player == 'computer':
            optimalNode = minmax(Node(None, True, red, blue, 0), MIN, MAX)
            # print(optimalNode.red, ",", optimalNode.blue, " ", optimalNode.score)
            if optimalNode.red == red:
                print("Computer Move: Blue")
                blue = blue-1
            else:
                print("Computer Move: Red")
                red = red-1
            player = 'human'
        else:
            move = input("Human move(red/blue): ")
            if move == 'red':
                red = red-1
                player = 'computer'
            elif move == 'blue':
                blue = blue-1
                player = 'computer'
            else:
                print("Incorrect move!.Please enter again")
    declarewinner(red, blue, player)
