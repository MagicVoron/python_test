from pprint import pprint

def dialog(text):
    pprint(text)
    answer = input()
    return answer

def friendship(person, host):
    host.add_friend(person)