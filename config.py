import yaml

def load_style(path="style.yaml", profile=None):
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if profile is None:
        profile = data.get("default_profile", "concise")

    return {
        "style": data["profiles"][profile]
    }