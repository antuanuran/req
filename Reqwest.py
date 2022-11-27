import requests

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
resp_all_list = requests.get(url).json()

name_intel = {}
intelligence_value = []
name_1 = 'Captain America'
name_2 = 'Hulk'
name_3 = 'Thanos'


i = 0
for var in resp_all_list:
    if (resp_all_list[i]['name'] == name_1 or resp_all_list[i]['name'] == name_2 or resp_all_list[i]['name'] == name_3):
        name_intel [resp_all_list[i]['name']] = resp_all_list[i]['powerstats']['intelligence']
        intelligence_value.append(resp_all_list[i]['powerstats']['intelligence'])
    i += 1

max_value = max(intelligence_value)
print(f'\nКол-во IQ у супергероев: {name_intel}\n')


for result in name_intel:
    if name_intel[result] == max_value:
        print(f'Самый умный супергерой: {result}')



















