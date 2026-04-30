def solution(n, times):
    left, right = 1, max(times) * n  # 최소 시간과 최대 시간 범위 설정
    
    answer = right  # 최종적으로 반환할 값
    while left <= right:
        mid = (left + right) // 2  # 중간 시간 설정
        
        total_people = 0  # mid 시간 동안 처리한 총 인원 수
        for t in times:
            total_people += mid // t  # mid 시간 동안 심사 가능한 인원 수 계산
            
            if total_people >= n:  # 심사 가능한 인원 수가 n 이상이면 더 작은 시간으로 확인
                answer = min(answer, mid)
                right = mid - 1
                break
        else:
            if total_people < n:  # 심사 가능한 인원 수가 n 미만이면 더 큰 시간으로 확인
                left = mid + 1
    
    return answer

