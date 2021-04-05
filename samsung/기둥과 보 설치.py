'''
좌표에 생성할 구조물이 문제 없는지 확인하는 함수
좌표에 생성 후 확인 함수를 통해 오류 확인 후 오류 발견 시 제거
좌표에 제거 후 확인 함수를 통해 오류 확인 후 오류 발견 시 생성
'''
def possible(answer):
    for x,y,a in answer:
        if a == 0: # 기둥
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
            # 1. 바닥에 기둥을 지었을 때, 2. 보 끝에 기둥을 지었을 때, 3. 기둥 위에 기둥을 지었을 때
                continue
            return False
        elif a == 1: # 보
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
            # 1. 양 끝 중 하나라도 기둥 있을 때, 2. 양 끝이 보랑 만날 때
                continue
            return False
    return True

def solution(n, build_frame): 
    answer = []
    for frame in build_frame:
        x,y,a,b = frame
        if b == 0: # 제거
            answer.remove([x,y,a])
            if possible(answer) == False: # 구조물이 없어질 수 없다면
                answer.append([x,y,a])
        if b == 1: # 생성
            answer.append([x,y,a])
            if possible(answer) == False: # 구조물이 지어질 수 없다면
                answer.remove([x,y,a])
    return sorted(answer)
