# 실패한 내풀이 위쪽을 확인해야된다는 것을 포함하지 않음
# 간결하지 못해 다시 짜기로 결정
from collections import deque

def solution(places):
    answer = []
    # 오른쪽, 아래, 대각방향, 오른쪽 2칸, 아래 2칸
    dx = [1, 0, 1, 2, 0]
    dy = [0, 1, 1, 0, 2]

    for i in range(5):
        temp_arr = places[i]
        queue = deque()
        queue.append([0, 0])
        is_fail_flag = False

        while queue:  # bfs 사용
            x, y = queue.popleft()
            is_right_side = False
            is_down_side = False

            for i in range(5):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 5 or ny >= 5:
                    continue

                if temp_arr[x][y] == "P":
                    if i == 0:
                        if temp_arr[nx][ny] == "X":
                            is_right_side = True
                        elif temp_arr[nx][ny] == "P":
                            is_fail_flag = True
                            break
                    elif i == 1:
                        if temp_arr[nx][ny] == "X":
                            is_down_side = True
                        elif temp_arr[nx][ny] == "P":
                            is_fail_flag = True
                            break
                    elif i == 2:
                        if not is_right_side or not is_down_side:
                            if temp_arr[nx][ny] == "P":
                                is_fail_flag = True
                                break
                    elif i == 3:
                        if not is_right_side and temp_arr[nx][ny] == "P":
                            is_fail_flag = True
                            break
                    else:
                        if not is_down_side and temp_arr[nx][ny] == "P":
                            is_fail_flag = True
                            break
                queue.append([nx, ny])

            if is_fail_flag:
                break

        if is_fail_flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer


# 내 풀이