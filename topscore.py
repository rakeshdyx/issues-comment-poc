class Solution:
    def highScore(self, student_score: list) -> int:
        score = 0
        for i in student_score:
            if i > score:
                score = i
        return score
    
highest_score = Solution()
x = highest_score.highScore([78, 65, 89, 86, 55, 91, 64, 89])

print(f"The highest score in the class is: {x}")
