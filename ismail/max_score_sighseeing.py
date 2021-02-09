from typing import List

def max_score_sightseeing_pair(A: List[int]) -> int:
    max_num = 0
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            score = A[i] + A[j] + i -j
            if score > max_num: max_num = score 
        return max_num
    
    

if __name__ == '__main__':
    print(max_score_sightseeing_pair([8,1,5,2,6]))
    