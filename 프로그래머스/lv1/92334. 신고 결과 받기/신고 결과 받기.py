def solution(id_list, report, k):
    reportcount = [0 for i in id_list]
    mailcount = [0 for i in id_list]
    for i in set(report):
        j,l = i.split()
        reportcount[id_list.index(l)] += 1
    for i in set(report):
        j,l = i.split()
        if int(reportcount[id_list.index(l)]) >= k:
            mailcount[id_list.index(j)] += 1
    return mailcount