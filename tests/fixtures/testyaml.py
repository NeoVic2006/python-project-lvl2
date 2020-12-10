import yaml 

stream = open("test.yml", 'r')
dictionary = yaml.load(stream, Loader=yaml.FullLoader)


print(dictionary)