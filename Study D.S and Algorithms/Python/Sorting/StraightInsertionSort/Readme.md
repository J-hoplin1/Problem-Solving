단순삽입정렬
===
***

- 삽입정렬(Insertion Sort)란?

- 삽입정렬은 주목한 원소보다 더 앞쪽에서 알맞은 위치로 삽입하며 정렬하는 알고리즘이다.

- 선택정렬과 다른 점이라면 선택정렬은 한번 검사를 마친후 주목하고 있는 값과 가장 작은 값의 위치를 바꾸는 형식이지만, 삽입정렬은 선택정렬처럼 작은 값을 선택하지 않는 부분이 다른점이라고 할 수 있다.

- 삽입정렬은 주목하고 있는 원소를 기준으로 왼쪽이 정렬된 부분, 오른쪽을 정렬되지 않은 부분으로 나눈다.

- 삽입정렬은 아직 정렬되지 않은부분(주목하고있는 원소 포함)의 맨 앞원소(이것이 즉 주목하고 있는 원소를 의미한다.)를 정렬된 부분의 알맞은 위치에 삽입한다.

- '알맞은 위치에 삽입' 하는 과정은 다음과 같다.

    - 우선 주목하고있는 원소의 값을 따로 저장해 둔다.

    - 선택하고 있는 원소의 왼쪽 이웃 원소값이 더 크면, 주목하고 있는 원소 index에 이웃한 값을 스캔(복사) 한다.

    - 이 과정을 계속 반복하다가, 만약 이웃한 원소값이 원래 주목하고 있는 값보다 작은 경우, 검사중인 해당 index에 원래 주목하는 값을 넣어준다.

    - 만약 정렬된 곳의 원소들중 주목하고 있는 원소보다 모두 크면, 맨앞(index 0)에 넣어준다.

    - 위의 모든 과정은 밑에 코드와 배열의 변환 과정을 보면서 이해하길 바란다.
    
- 기본적인 코드는 다음과 같다.

    ```python
        def insertionSort(a : MutableSequence):
            n = len(a) # 입력된 정렬되지 않은 배열의 길이
            for u in range(1, n):
                originData = a[u]
                checkIndex = u
                while checkIndex > 0 and a[checkIndex - 1] > originData:
                    a[checkIndex] = a[checkIndex - 1]
                    checkIndex -= 1
                    print(a)
                a[checkIndex] = originData
                print(a)
        a = [6,1,4,2,5,9,11,10]
        insertionSort(a)
        '''
        Result
        [6, 6, 4, 2, 5, 9, 11, 10]
        [1, 6, 4, 2, 5, 9, 11, 10]
        [1, 6, 6, 2, 5, 9, 11, 10]
        [1, 4, 6, 2, 5, 9, 11, 10]
        [1, 4, 6, 6, 5, 9, 11, 10]
        [1, 4, 4, 6, 5, 9, 11, 10]
        [1, 2, 4, 6, 5, 9, 11, 10]
        [1, 2, 4, 6, 6, 9, 11, 10]
        [1, 2, 4, 5, 6, 9, 11, 10]
        [1, 2, 4, 5, 6, 9, 11, 10]
        [1, 2, 4, 5, 6, 9, 11, 10]
        [1, 2, 4, 5, 6, 9, 11, 11]
        [1, 2, 4, 5, 6, 9, 10, 11]
        '''
    ```

- 삽입정렬은 서로 이웃하고 있는 원소들끼리에 대해서 교환을 하기때문에 안정적인 정렬이라고 할 수 있다.