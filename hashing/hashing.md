# hashing (해싱)
- 데이터를 아주 빠르게 '삽입','가져올 때' 사용
- 최솟값, 최댓값을 찾는 문제는 효율이 떨어짐
- Python의 dic은 해시 테이블로 구성되어 있음
----------------------------

<img width="400" alt="epoch01_prediction" src="https://user-images.githubusercontent.com/49745654/110451415-85887980-8107-11eb-8870-4855dd7fcd9e.PNG">
사용 예시 : 전화번호를 새로 추가할 때, 추가하고자 하는 데이터로 인한 데이터 이동 최소화

## Direct-address table
1. input(이름) -> output(해시 값) 함수 생성
2. 이름 input 후 해시값 output 으로 return
3. 해시값을 주소로 하는 저장공간에 저장
4. John Smith의 이름을 input -> John Smith의 해시값 output
5. John Smith의 해시값을 주소로 하는 저장공간 찾아 읽기 

