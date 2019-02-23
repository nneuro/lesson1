dict_1={
    'city':'Москва',
    'temperature':'20'
}
print(dict_1['city'])
dict_1['temperature']=(int(dict_1['temperature'])-5)
print (dict_1)

print(dict_1.get('country'))
dict_1['country']='Россия'
print (dict_1)
dict_1['date']='27.05.2019'
print(dict_1)
print(len((dict_1)))

