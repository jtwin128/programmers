def solution(phone_book):
    hash_map = {}

    for phone in phone_book:
        hash_map[phone] = True

    for phone in phone_book:
        temp = ""

        for ch in phone:
            temp += ch

            if temp in hash_map and temp != phone:
                return False

    return True