import os

def save(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def load(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()
    
def delete(filename):
    os.remove(filename)
