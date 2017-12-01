'''
Knight movement on a chess board

Given any source point and destination point on a chess board, we need to find
whether Knight can move to the destination or not.

Knight's movements

The above figure details the movements for a knight ( 8 possibilities ). Note
that a knight cannot go out of the board.

If yes, then what would be the minimum number of steps for the knight to move
to the said point. If knight can not move from the source point to the
destination point, then return -1

Input:

N, M, x1, y1, x2, y2
where N and M are size of chess board
x1, y1  coordinates of source point
x2, y2  coordinates of destination point
Output:

return Minimum moves or -1
Example

Input : 8 8 1 1 8 8
Output :  6
'''
class Solution:
    # bfs
    def knight(self, N, M, x1, y1, x2, y2):
        from collections import deque
        jumps_xy = [(1,2),(2,1),(1,-2),(-2,1),(-1,2),(2,-1),(-1,-2),(-2,-1)]
        queue = deque([(x1, y1, 0)])
        visited = set([(x1, y1)])
        while queue:
            x, y, n = queue.popleft()
            if (x, y) == (x2, y2):
                return n
            for xd, yd in jumps_xy:
                new_x = x + xd
                new_y = y + yd
                new_xy = (new_x, new_y)
                if 0 < new_x <= N and 0 < new_y <= M and new_xy not in visited:
                    queue.append((new_x, new_y, n+1))
                    visited.add(new_xy)
        return -1

# test
print(Solution().knight(8,8,1,1,8,8))   # 6
print(Solution().knight(2,20,1,18,1,5)) # -1
print(Solution().knight(1,1,1,1,1,1))   # 0
print(Solution().knight(4,7,2,6,2,4))   # 2
