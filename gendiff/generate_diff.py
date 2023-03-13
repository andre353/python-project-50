import json


def generate_diff(file_path1, file_path2):
    with open(file_path1) as f:
        file1 = json.load(f)
    with open(file_path2) as f:
        file2 = json.load(f)

    all_keys = set(file1.keys()) | set(file2.keys())

    result_diff = []
    for key in sorted(all_keys):
        val1 = file1.get(key)
        val2 = file2.get(key)
        if val1 == val2:
            result_diff.append(f"  {key}: {low_value(val1)}")
        elif val1 is None:
            result_diff.append(f"+ {key}: {low_value(val2)}")
        elif val2 is None:
            result_diff.append(f"- {key}: {low_value(val1)}")
        else:
            result_diff.append(f"- {key}: {low_value(val1)}")
            result_diff.append(f"+ {key}: {low_value(val2)}")
    
    return '{\n' + '\n'.join(result_diff) + '\n}'


def low_value(val):
    return str(val).lower() if isinstance(val, bool) else val
