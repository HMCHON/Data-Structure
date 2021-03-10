# hashing (해싱)
- 데이터를 아주 빠르게 '삽입','가져올 때' 사용
- 최솟값, 최댓값을 찾는 문제는 효율이 떨어짐
- Python의 dic은 해시 테이블로 구성되어 있음
----------------------------

<img width="400" alt="epoch01_prediction" src="https://user-images.githubusercontent.com/49745654/110451415-85887980-8107-11eb-8870-4855dd7fcd9e.PNG">
사용 예시 : 전화번호를 새로 추가할 때, 추가하고자 하는 데이터로 인한 데이터 이동 최소화

## _Direct-address table_
1. input(이름) -> output(해시 값) 함수 생성
2. 이름 input 후 해시값 output 으로 return
3. 해시값을 주소로 하는 저장공간에 저장
4. John Smith의 이름을 input -> John Smith의 해시값 output
5. John Smith의 해시값을 주소로 하는 저장공간 찾아 읽기 

## _Python dict 문법_
### [1] { 'A':0, 'B':1, "C":2}
```sh
string_list = ['A', 'B', 'C'}
dictionary = {string:i for i, string in enumerate(string_list)}
print(dictionary)
```

### [2] zip 사용해서 묶기
```sh
string_list = ['A', 'B', 'C']
int-list = [1, 2, 3]
dictionary = dict(zip(string_list, int_list))
print(dictionary)
```

### [3] dict 안의 원소 지우기
```sh
del dictionary['A']
```

### [4] 출력 설정
```sh
print(answer.keys())          # dict_keys(['leo']
print(list(answer.keys())[0]) # leo
```

### [5] key와 value 이용하기
```sh
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> for key in a:
...     print(key)
... 
alice
bob
tony
suzy
```
```sh
>>> for val in a.values():
...     print(val)
... 
[1, 2, 3]
20
15
30   
```

```sh
sum_all = []
for val in ndict.values():
    sum_all.append(sum(val)) # [1450, 3100]
```


### [6] temp 사용 (리스트로 묶여있는 문자열에서 중복 문자 찾기)
```sh
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
```
### [7] defalutdict 활용 예시
```sh
from collections import defaultdict

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

ndict = defaultdict(list)
for k, v in zip(genres,plays):
    ndict[k].append(v) # defaultdict(<class 'list'>, {'classic': [500, 150, 800], 'pop': [600, 2500]})
```

### [8] itemgetter
```sh
from operater import imtegetter

sorted(student_tuples, key=itemgetter(2))
#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```
```sh
# 먼저 grade로 정렬한 다음 age로 정렬하려면
sorted(student_tuples, key=itemgetter(1,2))
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
```

### [9] enumerate
```sh
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
```













