def solution(rsp):
    win = {'2':'0', '0':'5', '5':'2'}
    return ''.join([win[i] for i in rsp])