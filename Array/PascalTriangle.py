def generate(self, numRows):
        triangle = []
        if numRows == 0: return triangle
        
        triangle.append([1])
        
        for i in range(1,numRows):
            prevRow = triangle[i-1]
            newRow = []
            
            newRow.append(1)
            for j in range(1,len(prevRow)):
                #element = prevElement(index - 1) + prevElement(index)
                newRow.append(prevRow[j-1] + prevRow[j])
            newRow.append(1)
            
            triangle.append(newRow)
        return triangle
