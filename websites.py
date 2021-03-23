import yaml

with open(r'./websites.yml') as file:
    try:
        content = yaml.safe_load(file)['websites']
    except yaml.YAMLError as e:
        print(e)