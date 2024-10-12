class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        altern = 0
        colors = colors + colors[:2] #ilk 2 elemanı sona ekliyoruz
        for i in range(1,len(colors)-1):
            if colors[i-1] == colors[i+1] and colors[i] != colors[i-1]:
                altern +=1
        return altern
        