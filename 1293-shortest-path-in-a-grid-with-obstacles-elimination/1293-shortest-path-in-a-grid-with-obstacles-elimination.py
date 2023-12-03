class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:  # Start and end are the same
            return 0

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Queue for BFS: each element is (row, col, remaining_obstacles, steps)
        queue = deque([(0, 0, k, 0)])

        # Set to keep track of visited states: (row, col, remaining_obstacles)
        visited = {(0, 0, k)}

        while queue:
            row, col, remaining_obstacles, steps = queue.popleft()

            # Check if reached the end
            if row == m - 1 and col == n - 1:
                return steps

            # Check all four adjacent cells
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n:
                    new_remaining_obstacles = remaining_obstacles - grid[new_row][new_col]
                    if new_remaining_obstacles >= 0 and (new_row, new_col, new_remaining_obstacles) not in visited:
                        visited.add((new_row, new_col, new_remaining_obstacles))
                        queue.append((new_row, new_col, new_remaining_obstacles, steps + 1))

        # If the queue is exhausted, it's not possible to reach the end
        return -1