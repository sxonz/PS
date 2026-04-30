def solution(genres, plays):
    answer = []
    temp = {}
    for i, (genre, play) in enumerate(zip(genres,plays)):
        if genre in temp.keys():
            temp[genre] = [temp[genre][0]+play, temp[genre][1]+[[play,i]]]
        else:
            temp[genre] = [play, [[play,i]]]
    for j, indexs in sorted(temp.items(), key=lambda x: -x[1][0]):
        for index in sorted(indexs[1], key=lambda x: -x[0])[:2]:
            answer.append(index[1])

    return answer