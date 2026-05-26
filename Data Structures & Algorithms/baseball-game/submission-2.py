class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for char in operations:
           
            if char == "+":
                record.append(record[-1] + record[-2])
            elif char == "C":
                record.pop()
            elif char == "D":
                record.append(2*record[-1])
            else:
                record.append(int(char))
        return sum(record)

        

            

        