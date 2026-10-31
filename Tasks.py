def func(data):
    if isinstance(data, list):
        new_cleared_list = []
        # print(data)
        for deeper_list in data:
            # print(deeper_list)
            item = func(deeper_list)
            if item != "" and item != {} and item != [] and item != ():
                new_cleared_list.append(item)
        return new_cleared_list
    elif isinstance(data, dict):
        new_cleared_dict = {}
        for key, value in data.items():
            if key == "": continue
            item = func(value)
            new_cleared_dict[key] = item
        return new_cleared_dict
    return data


# const = [{},[],{"":123,"":"12",12:[]},12," ",[],3.14,[1,2,3]]
const = [{"": 1, "12": {"123": {"": {}}}}, {"": []}, {}]
const1 = [[], [1, [3, [4, [], [[]]]], 2]]
print(func(const1))


