class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sample = []
        for i in range(len(mat)):
            sample.append((sum(mat[i]), i))
        # sample = [(2,0), (4,1), (1,2), (2,3), (5,4)]
        sample.sort()
        return [sample[i][1] for i in range(k)]