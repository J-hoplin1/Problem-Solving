from typing import Any
from collections import deque

'''
collections.deque의 주요 속성 및 함수

deque()의 기본적인 parameter : deque([#deque 초기화], 최대 저장개수(maxlen))

maxlen 속성 : deque의 최대 크기를 나타내는 속성으로 읽기 전용이다, 크기제한이 없으면 none이 된다.
append(x) : deque의 맨 끝에 x를 추가한다.
appendleft(x) : deque의 맨 앞(왼쪽)에 x를 추가한다.
clear() : deque의 모든 원소를 삭제하고 크기를 0으로 한다.
copy() : deque의 얕은 복사를 한다.
count(x) : deque안에 있는 x와 같은 원소 개수를 계산한다.
pop() : deque의 오른쪽에 있는 원소를 1개 삭제하고 원소를 반환한다. 원소가 없는경우 indexerror를 내보낸다.
popleft() : deque의 왼쪽에 있는 원소를 1개 삭제하고 그 원소를 반환한다.
index(x) : x가운데 가장 앞쪽에 있는 원소의 위치를 반환한다.
remove(value) : value의 첫째 항목을 삭제한다.
'''



class Stack(object):

    class empty(Exception):
        pass
    class full(Exception):
        pass

    def __init__(self, maxlen: int=256)->None:
        self.capacity = maxlen
        self.__stk = deque([],maxlen)
    
    def __len__(self) -> int: # dunder : class형 인스턴스를 __len__()에 전달할 수 있다. len(x) 와 같이 사용할 수 있다.
        return len(self.__stk)
    
    def isEmpty(self) -> bool:
        return not self.__stk
    
    def isFull(self) -> bool:
        return len(self.__stk) == self.__stk.maxlen #maxlen속성 : deque 의 최대 크기를 나타내는 속성으로 읽기전용이다, 크기 제한이 없다면 none이 된다.
    
    def push(self,value:Any) -> None:
        if self.isFull():
            raise Stack.full
        return self.__stk.append(value)
    
    def pop(self) -> Any:
        if self.isEmpty():
            raise Stack.empty
        return self.__stk.pop()
    
    def peek(self) -> Any:
        if self.isEmpty():
            raise Stack.empty
        return self.__stk[-1]
    
    def clear(self) -> None:
        self.__stk.clear()

    #stack에서 꼭대기부터 바닥까지 검색하는 경우에 처음으로 나오는 index 반환
    def find(self,value:Any) -> Any:
        p = list(self.__stk)
        for e in range(len(p)-1, -1 , -1):
            if p[e] == value:
                return e
        return -1
    '''
    stack에서 바닥에서부터 꼭대기까지 검색하는 경우에 처음으로 나오는 index 반환

    def find(self,value:Any) -> Any:
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1
    '''

    def count(self,value:Any) -> int:
        return self.__stk.count(value)
    
    def __contains__(self,value:Any) -> bool: # dunder : class형 인스턴스에 멤버십 판단 연산자인 in을 적용할 수 있다.
        return self.count(value)
    
    def dump(self) -> int:
        print(*self.__stk, sep='    ')
