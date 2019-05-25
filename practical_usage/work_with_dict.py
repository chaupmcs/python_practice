from collections import OrderedDict, Counter, defaultdict

cities = ["sai gon", "ha noi", "hue"]
populations = [10, 8, 1]

dict_ = dict()
for c, p in zip(cities, populations):
    dict_[c.title()] = p
print(dict_)
## or:
dict_2 = dict(zip(cities, populations))
print("dict_2", dict_2)

print("----------------")

### create dict with 0 as default value: 2 ways, defaultdict or counter
# option 1
my_dict = defaultdict(int) # lambda: 0 or int
# _dict = {"a":2, "b": 3}
# my_dict.update(_dict)
## or:
my_dict["a"] = 2
my_dict["b"] = 3

print("my_dict", my_dict)
print(my_dict["b"])
print(my_dict["c"])
print("----------------")

# option 2
_dict = {"a":2, "b": 3}
my_dict_2 = Counter(_dict)
print(my_dict_2)
print(my_dict_2["b"])
print(my_dict_2["c"])
print("----------------")

my_array = ["baby", "chau", "vy", "bebi", "khanhvy", "chanh", "babies"]
convert_arr_to_dict_with_key_is_len_str = defaultdict(list) # lambda : []

for name in my_array:
    key = len(name)
    convert_arr_to_dict_with_key_is_len_str[key].append(name)
print("convert_arr_to_dict_with_key_is_len_str", convert_arr_to_dict_with_key_is_len_str)


print("----------------")

while convert_arr_to_dict_with_key_is_len_str:
    k,v = convert_arr_to_dict_with_key_is_len_str.popitem()
    print("k = {}, v = {}".format(k, v))

print("----------------")

##########
message = "this is just a trivial text"

print(message.title())
print(message.capitalize())




