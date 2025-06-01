def solution(numbers, hand):
    answer = ""
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    left_pos = keypad['*']
    right_pos = keypad['#']

    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            left_pos = keypad[num]
        elif num in [3, 6, 9]:
            answer += "R"
            right_pos = keypad[num]
        else:
            target = keypad[num]
            l_dist = abs(left_pos[0] - target[0]) + abs(left_pos[1] - target[1])
            r_dist = abs(right_pos[0] - target[0]) + abs(right_pos[1] - target[1])
            if l_dist < r_dist:
                answer += "L"
                left_pos = target
            elif r_dist < l_dist:
                answer += "R"
                right_pos = target
            else:
                if hand == "right":
                    answer += "R"
                    right_pos = target
                else:
                    answer += "L"
                    left_pos = target
    return answer