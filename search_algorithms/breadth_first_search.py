from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]  # заполнение графов
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def bfs(name):
    search_queue = deque()
    search_queue += graph[name]
    searched_list = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched_list:
            if person_is_seller(person):
                print("that's it " + person)
                return True
            else:
                search_queue += graph[person]
                searched_list.append(person)
    return False


def person_is_seller(person):  # some logic
    if person == "alice":
        return True
    return False


print(bfs("you"))