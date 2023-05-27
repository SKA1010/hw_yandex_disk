import requests

url = 'https://superheroapi.com/api/2619421814940190/'

result_dict = {}

resp_id_Hulk = requests.get(url+'/search/Hulk')
intelligance_Hulk = resp_id_Hulk.json()['results'][0]['powerstats']['intelligence']
result_dict['Hulk'] = intelligance_Hulk

resp_id_CapAm = requests.get(url+'/search/Captain America')
intelligance_CapAm = resp_id_CapAm.json()['results'][0]['powerstats']['intelligence']
result_dict['Captain America'] = intelligance_CapAm

resp_id_Thanos = requests.get(url+'/search/Thanos')
intelligance_Thanos = resp_id_Thanos.json()['results'][0]['powerstats']['intelligence']
result_dict['Thanos'] = intelligance_Thanos

#print(result_dict)
max_intelligance = max(result_dict.items(), key=lambda x: x[0])
print(max_intelligance)
