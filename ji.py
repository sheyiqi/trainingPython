def del_duplicates(text):
    result_text = []
    i = 0
    while i < len(text):
        j = i
        # print(i)
        while j < len(text) and text[j] == text[i]:
            j += 1
        if j-i == 1:
            result_text.append(text[i])
            i = j
    return "".join(result_text)

def eliminate_duplicates(text,original_text):
    if len(text) <= 1:
        return text
    cur_text = del_duplicates(text)
    cur_points = len(text) - len(cur_text)
    if cur_points == 0:
        return text
    else:
        return eliminate_duplicates(cur_text, original_text)

def solution(text):
    best_text = text
    if len(text) == 1:
        return len(text)
    else:
        for i in range(len(text)+1):
            for letter in "ABC":
                new_text = text[:i] + letter + text[i:]
                new_result_text = eliminate_duplicates(new_text, new_text)
                if len(new_result_text) < len(best_text):
                    best_text = new_result_text
                    # print(best_text)
    return len(text) - len(best_text) + 1

print(solution(raw_input()))
