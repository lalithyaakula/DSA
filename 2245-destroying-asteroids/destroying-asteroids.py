class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for i,num in enumerate(asteroids):
            if mass>=asteroids[i]:
                mass+=asteroids[i]
                continue
            else:
                if mass<asteroids[i]:
                    return False
        return True            



        