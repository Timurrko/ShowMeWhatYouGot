from json import dump, load
data = []
with open(r'C:\Users\shara\PycharmProjects\ShowMeWhatYouGot\data\hobbies', 'r', encoding='utf-8') as file:
    strings = [i.strip().split() for i in file.readlines()]
    for name, *hobbies in strings:
        data.append({'name': name, 'hobbies': hobbies})
print(data)
with open(r'C:\Users\shara\PycharmProjects\ShowMeWhatYouGot\data\hobbies.json', 'w', encoding='utf-8') as file:
    dump(data, file)
