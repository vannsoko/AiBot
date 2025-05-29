import os

ai_context: dict[str, str] = {}
path: str = '/app/context/text/'
for filenames in os.listdir(path):
    with open(f"{path}{filenames}") as f:
        ai_context[filenames.split(".")[0]] = f.read()
