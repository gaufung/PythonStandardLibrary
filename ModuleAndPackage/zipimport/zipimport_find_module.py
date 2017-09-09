import zipimport

importer = zipimport.zipimporter('zipimport_example.zip')

for module_name in ['zipimport_get_source', 'not_there']:
    print(module_name, ':', importer.find_module(module_name))