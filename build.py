import os, json, datetime, subprocess

ROOT_DIR = './root'

SECRET_COPY_DIRNAME = f'{ROOT_DIR}/secret_copy'
SECRET_DIRNAME = f'{ROOT_DIR}/secret'

import os
import requests
import base64
import json
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend



def get_env_vars():
    return os.getenv('GITHUB_TOKEN'), os.getenv('MU_REPO')

def gh_api_get(token, call):
    resp = requests.get(f'https://api.github.com/{call}', headers={
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    })
    if resp.status_code != 200:
        err = resp.json()
        print(f"Call: {call}\n")
        print(f"\n{err['status']}: {err['message']}\n")
        exit(0)
        return None
    try:
        return resp.json()
    except:
        return resp
    
def check_github_token(token) -> bool:
    if gh_api_get(token, 'octocat') == None:
        return False
    return True

def fetch_file(token, repo, file_path):
    file = gh_api_get(token, f'repos/{repo}/contents/{file_path}')
    return base64.b64decode(file['content'])

def fetch_repo_contents(token, repo) -> list:
    return [item['path'] for item in gh_api_get(token, f'repos/{repo}/contents') if item['type'] == 'file']

def encrypt_content(content, key):
    key = key.ljust(32)[:32].encode('utf-8')
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(content) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return iv + encrypted_data

def save_file(content, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as f:
        f.write(content)

def copy_secret_copy_files(secret, files):
    for file_path in files:
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                save_file(f.read(), f'{SECRET_DIRNAME}/{secret}/{os.path.basename(file_path)}')

def secret_files():
    token, mu_repo = get_env_vars()
    
    if mu_repo == '' or mu_repo == None:
        print("S: No environment variables")
        return

    if not check_github_token(token):
        print("S: Token error")
        return

    # Fetch info.json
    info_content = fetch_file(token, mu_repo, 'info.json')
    if not info_content:
        print('S: Failed to fetch info.json')
        return
    storages = json.loads(info_content.decode('utf-8'))

    # Fetch files from secret_copy/ if it exists
    if os.path.exists(SECRET_COPY_DIRNAME):
        secret_copy_files = [os.path.join(SECRET_COPY_DIRNAME, f) for f in os.listdir(SECRET_COPY_DIRNAME)] 
    else:
        secret_copy_files = []
        print("Note: No secret copy directory found")
    
    # Process each secret storage
    for storage in storages:
        secret, repo = storage['secret'], storage['repo']
        # Fetch and encrypt files from source repo
        for file_path in fetch_repo_contents(token, repo):
            content = fetch_file(token, repo, file_path)
            if content:
                encrypted_content = encrypt_content(content, secret)
                save_file(encrypted_content, f'{SECRET_DIRNAME}/{secret}/{file_path}.enc')
            else:
                print(f'S: Failed to fetch {file_path} from {repo}')
        # Copy secret_copy/ files without encryption
        copy_secret_copy_files(secret, secret_copy_files)


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


def write_file(filename: str, vals: dict, mode: str = 'w'):
    filename = ROOT_DIR + '/' + filename
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, mode, encoding='utf-8') as f:
        if mode == 'w':
            f.write("---\n")
        else:
            f.write("\n\n")

        f.write(write_yml(vals))

        if mode == 'w':
            f.write("---\n")

def get_commits_count() -> int:
    CMD = 'git rev-list --count HEAD'
    return int(subprocess.check_output(CMD, shell=True, text=True))

def main():
    build_time = datetime.datetime.now()
    build_time_str = build_time.strftime("%Y/%m/%d - %H:%M:%S")

    print(f"Started building at: {build_time_str}")
    print(f"Commit number: {get_commits_count()}")

    write_file('_config.yml', {
        'build_time': build_time_str,
        'commit_number': get_commits_count()
    }, 'a')

    projects = load_json('projects')
    awards = load_json('awards')
    badges = load_json('project_badges')

    for proj in projects:
        proj['status_color'] = badges[proj['status']]['color']
        proj['ar']['status'] = badges[proj['status']]['ar']
        proj['en']['status'] = badges[proj['status']]['en']


    write_file('index.html', {
        'title': 'معاذ القرني',
        'description': 'موقع شخصي',
        'lang': 'ar',
        'layout': 'home',
        'projects': projects,
        #'awards': awards
    })
    write_file('en.html', {
        'title': 'Muaath Alqarni',
        'description': 'Personal website',
        'lang': 'en',
        'layout': 'home',
        'projects': projects,
        #'awards': awards
    })

main()
secret_files()