'''
Problem 4 베스트앨범

[문제 요점]
1. 우선 순위 : 장르 -> 재생 횟수 -> 고유 번호 낮은 print(순
2. 효율성
'''




'''
다른 풀이 [1]
'''
def solution(genres, plays):
    answer = []
    _hash = {}
    for i in range(len(genres)): # {'classic': 1450, 'pop': 3100}
        if genres[i] in _hash:
            _hash[genres[i]] += plays[i]
        else:
            _hash[genres[i]] = plays[i]
    
    while len(_hash) > 0:
        genre_max = max(_hash.keys(),key=(lambda k:_hash[k]))
        del(_hash[genre_max])
        
        second = largest = 0
        for i in range(len(genres)):
            if genres[i] == genre_max:
                if plays[i] >= largest:
                    second = largest
                    largest = plays[i]
                elif second < plays[i] < largest:
                    second = plays[i]
                    
        answer.append(plays.index(largest))
        if second != 0:
            answer.append(plays.index(second))
            



