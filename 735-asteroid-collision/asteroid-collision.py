class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for asteroid in asteroids:
            while st and asteroid < 0 and st[-1] > 0:
                # top asteroid smaller -> explode
                if st[-1] < abs(asteroid):
                    st.pop()
                # both equal -> both explode
                elif st[-1] == abs(asteroid):
                    st.pop()
                    break
                # top bigger -> current explodes
                else:
                    break
            else:
                st.append(asteroid)
        return st
