import os

def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def save_asset(path, content):
    with open(path, 'w') as file:
        file.write(content)
