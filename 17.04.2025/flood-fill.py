Class Solution:

    Def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        Cur = image[sr][sc]

        If cur == color:

            Return image



        N = len(image)

        M = len(image[0])

        Q = deque()

        q.append((sr, sc))

        image[sr][sc] = color



        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while q:

            row, col = q.popleft()



            for dr, dc in directions:

                newr = dr + row

                newc = dc + col

                if 0 <= newr < n and 0 <= newc < m and image[newr][newc] == cur:

                    q.append((newr, newc))

                    image[newr][newc] = color

        

        return image

