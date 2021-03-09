'''
Problem 2 완주하지 못한 선수
[문제 요점]
1. 대량의 반복적인 문자열 비교
2. 효율성

[1차 시도 결과]
정확성 83.3, 효율성 8.3
합계 91.7 / 100.0
'''

def solution(phone_book):
    
    phone_book.sort()
        
    for i in phone_book:
        for j in phone_book:
            if i != j:
                if j.startswith(i):
                    return False
               
    return True
 
######## 더 효율적 ########
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True



'''
다른 풀이 [1]
[풀이 요점]
1. hashing(dict) 이용
2. temp를 
'''

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1 # {'119': 1, '97674223': 1, '1195524421': 1}
    for phone_number in phone_book:
        temp = ""
        for number in phone_number: #전화번호를 한글자로 쪼개서 반복문 '119'이면 '1' '1' '9'
            temp += number # 1 -> 11 -> 119 -> 9 -> 97 -> ... -> 1195524421
            if temp in hash_map and temp != phone_number: # temp가 hash_map에 있지만 phone_number는 아니라면...
                answer = False
    return answer












