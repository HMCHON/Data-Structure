'''
Problem 4 베스트앨범

[문제 요점]
1. 우선 순위 : 장르 -> 재생 횟수 -> 고유 번호 낮은 print(순
2. defaultdict과 itemgetter 그리고 enumerate

정확성: 100.0
합계: 100.0 / 100.0
'''

from collections import defaultdict
from operator import itemgetter

def solution(genres, plays):   
    answer = []
    
    # 장르 우선순위
    ndict = defaultdict(lambda : 0)
    for gen, ply in zip(genres, plays):
        ndict[gen] += ply #  {'classic': 1450, 'pop': 3100})
    
    ndict_list = sorted(ndict.items(), key = itemgetter(1), reverse = True) #[('pop', 3100), ('classic', 1450)]
    rank = []
    for i in ndict_list:
        rank.append(i[0])
    
    
    # 장르 - 최대재생수 - 고유번호 정리
    array = defaultdict(lambda : [])
    for i, array_tuple in enumerate(zip(genres, plays)):
        array[array_tuple[0]].append((array_tuple[1], i))
    
    # 결과 출력
    answer = []
    for gen in rank:
        gen_list = sorted(array[gen], key = itemgetter(0), reverse = True)
        # [(2500, 4), (600, 1)], [(800, 3), (500, 0), (150, 2)]
        
        if len(gen_list) > 1:
            answer.append(gen_list[0][1])
            answer.append(gen_list[1][1])
        else:
            answer.append(gen_list[0][1])
        
    return answer




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

'''
다른 풀이 [2]
'''
from collections import defaultdict
from operator import itemgetter

def solution(genres, plays):
    genre_play_dict = defaultdict(lambda: 0)
    for genre, play in zip(genres, plays):
        genre_play_dict[genre] += play # defaultdict(<function solution.<locals>.<lambda> at 0x14cc4e638ca0>, {'classic': 1450, 'pop': 3100})
        
    genre_rank = [genre for genre, play in sorted(genre_play_dict.items(), key = itemgetter(1), reverse = True)] # ['pop', 'classic']
    
    
    final_dict = defaultdict(lambda : [])
    for i, genre_play_tuple in enumerate(zip(genres, plays)):
        final_dict[genre_play_tuple[0]].append((genre_play_tuple[1], i)) # defaultdict(<function solution.<locals>.<lambda> at 0x1528c0fe9d30>, {'classic': [(500, 0), (150, 2), (800, 3)], 'pop': [(600, 1), (2500, 4)]})


    answer = []
    for genre in genre_rank:
        one_genre_list = sorted(final_dict[genre], key=itemgetter(0), reverse=True)
        
        if len(one_genre_list) > 1:
            answer.append(one_genre_list[0][1])
            answer.append(one_genre_list[1][1])
        else:
            answer.append(one_genre_list[0][1])
        
    return answer
























            



