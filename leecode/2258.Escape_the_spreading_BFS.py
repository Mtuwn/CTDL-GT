
"""
- Nếu chờ đợi t phút mà vẫn an toàn thì < t phút vẫn thõa mãn ==> Sử dụng tìm kiếm nhị phân
- Sử dụng BFS để mô phỏng đám cháy sau t phút , sau đó sử dụng 1 BFS khác để mô phỏng quá trình tìm đường đi đến nơi an toàn sau thời gian đợi t phút
Note: Trong quá trình di chuyển tìm đường đi an toàn đảm bảo đánh dấu thời gian cháy đến các ô và các tường đã được đánh dấu

"""

class Solution:
        def maximumMinutes(self, grid:List[List[int]])->int:
            left = 0
            right = 10 ** 9
            R = len(grid) # Hàng 
            C = len(grid[0])    # Cột
            INF = 10**10

            q = collections.deque() # Khởi tạo deque 2 đầu
            dist = [[INF] * C for _ in range(R)] # Khởi tạo mảng lưu trữ thời gian fire đến vị trí từng ô

            directions = [(0,1), (1,0), (0, -1), (-1,0)]

            for i in range(R):
                for j in range(C):
                    if grid[i][j] == 1: # Ô bị fire
                        dist[i][j] = 0
                        q.append((0,i,j)) # lưu trữ khoảng cách và vị trí của từng ô vào queue

            while len(q) > 0:
                d,x,y = q.popleft()

                for dx, dy in directions: # Kiểm tra các ô trên dưới trái phải
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < R and 0 <= ny < C and dist[nx][ny] == INF and grid[nx][ny] != 2: # Đảm bảo nó vẫn nằm trong matrix và các ô vẫn chưa được đến thăm
                        dist[nx][ny] = d+1 # Cập nhật thời gian với fire ban đầu
                        q.append((d+1, nx, ny))

            def good(target):
                q = collections.deque() 
                visted =  [[INF] * C for _ in range(R)] # Khởi tạo mảng lưu trữ thời gian sống

                if dist[0][0] <= target:  # Nếu mà thời gian sống tối đa nhỏ hơn hoặc bằng thời gian lửa cháy đến thì sai
                    return False
                
                q.append((target, 0, 0))

                while len(q) > 0:
                    d, x, y = q.popleft()

                    for dx, dy in directions: # Các ô trên dưới trái phải
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < R and 0 <= ny < C and visted[nx][ny] == INF and grid[nx][ny] != 2 and d+1 < dist[nx][ny]: # Đảm bảo nó vẫn nằm trong matrix và các ô vẫn chưa được đến thăm, các ô không phải là tường, và thời gian đến các ô tiếp theo phải nhỏ hơn thời gian lửa cháy đến các ô đó
                            visted[nx][ny] = d+1 
                            q.append((d+1, nx, ny))

                            if nx == R - 1 and ny == C - 1: # Đã đến đích
                                return True
                        
                        if nx == R - 1 and ny == C - 1 and grid[nx][ny] != 2 and visted[nx][ny] == INF and d + 1 <= dist[nx][ny]: # gay cả khi lửa lan sang nhà an toàn ngay sau khi bạn tiếp cận nó thì vẫn được tính là đã đến nhà an toàn
                            return True


                return False

# Tìm kiếm nhị phân
            while left < right:
                mid = (left + right + 1) // 2
                
                if good(mid):
                    left = mid
                else: 
                    right = mid -1

            if left == 0:
                return 0 if good(0) else -1
            
            return left