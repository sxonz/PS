def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = [-30001]
    for c,o in routes:
        if c >= camera[-1] >= o or c <= camera[-1] <= o:
            continue
        else:
            camera.append(o)
    return len(camera[1:])