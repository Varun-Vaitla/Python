#dict =>it a built in datatype in python to store data in the form of key value pairs

student={
    "name":"varun",
    "age":25,
    "course":"MCA"

}
print(type(student))
print(student)
"""
<class 'dict'>
{'name': 'varun', 'age': 25, 'course': 'MCA'}

"""
#Accessing values form dict
print(student["name"])#varun
#if ke is not present 
# print(student["place"])#keyError


#methods
#1.get()=> it is used to get the value of specified key, similar to accessing value using [] but it will not retun KeyError if value is not present

St_name=student.get("name")
print(St_name)#varun

#if key is not present

st_place=student.get("place","place is not present in student dict")
print(st_place)#place is not present in student dict

#2.keys() => this method is used to get all the keys of an dict. it will return in dict_keys object which is dynamic
student_keys=student.keys()
print(student_keys)#dict_keys(['name', 'age', 'course'])
student["place"]="DVG"
print(student_keys)#dict_keys(['name', 'age', 'course', 'place'])

#3.values()=>it is used to retrive all values of dict in dict_values object
student_values=student.values()
print(student_values)#dict_values(['varun', 25, 'MCA', 'DVG'])

#4.items() => it will return all key value pairs in dict_items object
strudent_keyvalues=student.items()
print(strudent_keyvalues)#dict_items([('name', 'varun'), ('age', 25), ('course', 'MCA'), ('place', 'DVG')])

#5.update The update() method is used to add new key-value pairs or modify existing key-value pairs in a dictionary.
student.update({"grade": "A+"})
print(student)#{'name': 'varun', 'age': 25, 'course': 'MCA', 'place': 'DVG', 'grade': 'A+'}
#update existing values
student.update({"grade": "B+"})
print(student)#{'name': 'varun', 'age': 25, 'course': 'MCA', 'place': 'DVG', 'grade': 'B+'}

#6.The pop() method is used to remove a specified key-value pair from a dictionary and return its associated value.
result = student.pop("age")

print("Removed value:", result)
print("Dictionary:", student)
"""
Removed value: 25
Dictionary: {'name': 'varun', 'course': 'MCA', 'place': 'DVG', 'grade': 'B+'}

"""
# result = student.pop("salary", "Key Not Found")

# print(result)
# print(student)

#7.The popitem() method is used to remove and return the last inserted key-value pair from a dictionary.

# Unlike pop(), where we specify which key to remove, popitem() automatically removes the last inserted item.
student = {
    "name": "Varun",
    "age": 26,
    "course": "MCA",
    "city": "Davangere"
}

result = student.popitem()

print("Removed item:", result)
print("Updated dictionary:", student)
"""
Removed item: ('city', 'Davangere')
Updated dictionary: {'name': 'Varun', 'age': 26, 'course': 'MCA'}"""