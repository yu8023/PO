import yaml,os

def ret_yaml_data(file_name):
    file_path = os.getcwd() + os.sep + "Data" + os.sep + file_name + ".yml"
    print(file_path)   # D:\LearningTest\pycharm\Page_Object_Pro\Base\Data\search_data.yml
    with open(file_path,'r',encoding='utf-8') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
    return data


if __name__ == '__main__':
    ret_yaml_data('search_data')