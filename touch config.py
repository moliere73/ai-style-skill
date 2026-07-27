import yaml


def load_style(path="style.yaml"):
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)