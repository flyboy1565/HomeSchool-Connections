

def get_vtypes(choices, qset1,qset2):
    values = {}
    for i in qset1:
        print(values)
        key = choices[i['volunteering_type_1']]
        print(key)
        if key not in values.keys():  
            values[key] = i['count']
    for i in qset2:
        key = choices[i['volunteering_type_2']]
        if key not in values.keys():
            values[key]= i['count']
        else:
            values[key]+= i['count']
    return values