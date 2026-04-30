import re
def solution(new_id):
    print(new_id)
    new_id = ''.join([i for i in new_id.lower() if re.match('[\w_.]',i) or i == '-'])
    print(new_id)
    new_id = ''.join([new_id[i] for i in range(0,len(new_id)) if [new_id[i],new_id[i-1]].count('.') < 2])
    print(new_id)
    new_id = new_id.strip('.')
    print(new_id)
    if new_id == "": new_id = 'aaa'
    print(new_id)
    new_id = new_id[:15].strip('.')
    print(new_id)
    if len(new_id) == 1:new_id *= 3
    if len(new_id) == 2:new_id += new_id[1]
    print(new_id)
    return new_id