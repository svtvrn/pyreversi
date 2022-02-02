from State import *
import math

class SpaceSearcher:

    def __init__ (self,depth,a,b):
      self.depth=depth
      self.a=a
      self.b=b
        
    def minimax(current_node,depth,a,b,colour):
        if(depth==0 or current_node.isFinal(colour)):
            return current_node.heuristic(colour)

        if(colour==State.BLACK):
            max_value = -math.inf
            children = current_node.getChildren(colour)
            for child in children:
                value = SpaceSearcher.minimax(child,depth-1,a,b,child.getOpponent(colour))
                max_value = max(max_value,value)
                a = max (a,value)
                if (b<=a):
                    break
            return max_value

        if(colour==State.WHITE):
            min_value = math.inf
            children = current_node.getChildren(colour)
            for child in children:
                value = SpaceSearcher.minimax(child,depth-1,a,b,child.getOpponent(colour))
                min_value = min(min_value,value)
                b = min(b,value)
                if(b<=a):
                    break
            return min_value