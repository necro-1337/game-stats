# Export functions
import re

def export_file(file):
    a_list = []
    with open(file) as file:
        lines = file.readlines()
        r = re.compile(r"(.+)\t+([0-9]+|\d+.\d+)\t+(\d+)\t+(.+)\t+(.+)")
        for i in lines:
            match = r.match(i)
            a_list.append(match.group(1, 2, 3, 4, 5))
    return a_list