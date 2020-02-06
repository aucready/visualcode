from PIL import Image
import os
import argparse



def search_dir(dirname):
    result_file_list = []
    filenames = os.listdir(dirname)

    # print(filenames)


    for filename in filenames:
        if filename.split('.')[0] == '':
            pass
        else:
            full_path = os.path.join(dirname, filename)
            # print(full_path)

            if os.path.isdir(full_path):
                if filename != 'convert':
                    result_file_list.extend(search_dir(full_path))
            else:
                result_file_list.append(full_path)
    return result_file_list

# p = argparse.ArgumentParser()
# p.add_argument('-f', type=str)
# p.add_argument('-e', type=str)
# args = p.parse_args()

# if args.f is None or args.e is None:
#     print('사용법 :-f <대상폴더> -e <변환될 확장자>')

while True:
    input_dir = input('폴더경로:')
    if not os.path.exists(input_dir):
        print('다시입혁하세요')

    if os.path.exists(input_dir):
        input_format = input('변환될 확장자를 입력하세요:')
        break



new_format = input_format
if new_format[0] != '.':
    new_format = '.' + new_format
file_lists = search_dir(input_dir)

for file in file_lists:
    new_folder = os.path.split(file)[0] + '/convert'
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)
    src_filename = os.path.splitext(file)[0]
    # print(src_filename)

    new_file = new_folder + '/' + src_filename.split('/')[-1] + new_format
    print(new_file)
    try:
        img = Image.open(file)
        img.verify()
        img.close()
        img = Image.open(file)
        print(img.size)
        img.save(new_file)

    except:
        pass






