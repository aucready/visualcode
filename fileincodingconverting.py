import os
import os.path
import argparse

# print(os.listdir(path))
from pip._vendor.chardet import detect


def search_dir(dirname):
    result_list = []
    filenames = os.listdir(dirname)

    for filename in filenames:
        full_path = os.path.join(dirname, filename)
        if os.path.isdir(full_path):
            result_list.extend(search_dir(full_path))
        else:
            result_list.append(full_path)
    return result_list


def get_encoding_type(filepath):
    with open(filepath, 'rb') as f:
        rawdata = f.read()

    codec = detect(rawdata)
    return codec['encoding']




INCLUDE_EXT_LIST = [".txt", ".smi"]

parse = argparse.ArgumentParser()
parse.add_argument('-f', type=str)
parse.add_argument('-e', nargs= '+')
args = parse.parse_args()


path = "/Users/aucready/path_study"
filelists = search_dir(path)

for file in filelists:
    filename, ext = os.path.splitext(file)
    
    tempfile = filename + "_tmp" + ext
    
    if ext.lower() in INCLUDE_EXT_LIST:
        encoding = get_encoding_type(file)
        if encoding.lower().find('utf') < 0:

            try:
                with open(file, 'r') as reads, open(tempfile, 'w', encoding='utf-8') as writes:
                    writes.write(reads.read())

                os.unlink(file)
                os.rename(tempfile, file)
                print('{} 이 저장되었습니다.'.format(file))
                
            except:
                pass
            finally:
                if os.path.exists(tempfile):
                    os.unlink(tempfile)

                    




