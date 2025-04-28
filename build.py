import os, json

ROOT_DIR = './root'

def load_json(filename):
    with open(f'{ROOT_DIR}/build/{filename}.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def write_yml(data: dict, indent: int = 0) -> str:
    res = ""
    for key, val in data.items():
        if type(val) is dict:
            res += " " * indent + str(key) + ":\n"
            res += write_yml(val, indent + 2)
        elif type(val) is list:
            res += " " * indent + str(key) + ":\n"
            res += " " * (indent+2) + f"count: {len(val)}\n"
            for i in range(len(val)):
                mp = {str(i+1): val[i]}
                res += write_yml(mp, indent + 2)
        elif val is None:
            res += " " * indent + str(key) + ": null\n"
        elif type(val) is bool:
            res += " " * indent + str(key) + ": " + str(val).lower() + "\n"
        elif type(val) is int:
            res += " " * indent + str(key) + ": " + str(val) + "\n"
        else:
            res += " " * indent + str(key) + ": \"" + str(val) + "\"\n"
    return res


def write_file(filename: str, vals: dict):
    filename = ROOT_DIR + '/' + filename
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("---\n")
        f.write(write_yml(vals))
        f.write("---\n")

def main():
    projects = load_json('projects')
    awards = load_json('awards')
    badges = load_json('project_badges')

    for proj in projects:
        proj['status_color'] = badges[proj['status']]['color']
        proj['ar']['status'] = badges[proj['status']]['ar']
        proj['en']['status'] = badges[proj['status']]['en']


    write_file('index.html', {
        'name': 'معاذ القرني',
        'description': 'موقع شخصي',
        'lang': 'ar',
        'layout': 'home',
        'projects': projects,
        #'awards': awards
    })
    write_file('en.html', {
        'name': 'Muaath Alqarni',
        'description': 'Personal website',
        'lang': 'en',
        'layout': 'home',
        'projects': projects,
        #'awards': awards
    })

main()