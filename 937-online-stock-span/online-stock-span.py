class StockSpanner:
    def __init__(self):
        self.st=[]
        self.arr=[]
    def next(self, price: int) -> int:
        self.arr.append(price)
        i=len(self.arr)-1
        while self.st and self.arr[self.st[-1]]<=price:
            self.st.pop()
        if not self.st:
            ans=i+1
        else:
            ans=i-self.st[-1]
        self.st.append(i)
        return ans


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)