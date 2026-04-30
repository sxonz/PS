def solution(operations):
    queue = []
    
    for i in operations:
        order, num = i.split(" ")
        if order == "I":
            queue.append(int(num))
        else:
            if not queue:
                continue
            if num == "1":
                queue.pop(queue.index(max(queue)))
            elif num == "-1":
                queue.pop(queue.index(min(queue)))
    
    if not queue:
        return [0, 0]
    return [max(queue), min(queue)]