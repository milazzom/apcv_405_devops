import yaml
with open("config.yaml") as f:
    config = yaml.safe_load(f)
print(f"Hello, {config['name']}!")