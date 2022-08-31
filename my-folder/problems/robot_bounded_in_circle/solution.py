class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Position did not change
        # Position and direction  changed
        s = set()
        x,y = 0,0
        direction = 1
        d = {1: (0,1), 2: (1,0), 3: (0,-1), 4: (-1,0)}  # 1 North 2 East 3 South 4 West
        for command in instructions:
            if command == 'G':
                x += d[direction][0]
                y += d[direction][1]
            elif command == 'L':
                if direction == 1:
                    direction = 4
                else:
                    direction -= 1
            elif command == 'R':
                if direction == 4:
                    direction = 1
                else:
                    direction += 1
        if x == 0 and y == 0:
            return True
        if (x != 0 or y != 0) and direction != 1:
            return True
        return False
                
        