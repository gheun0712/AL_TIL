def solution(phone_book):
    hash = {}
    
    for phone in phone_book:
        hash[phone] = 1
    
    for phone in phone_book:
        temp = ''
        for num in phone:
            temp += num
            
            if temp in hash and temp != phone:
                return False
    return True