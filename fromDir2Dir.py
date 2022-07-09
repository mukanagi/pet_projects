import os
import shutil

os.chdir('SS22Photo')
counter = 0

# start

for dir in os.listdir():
    try:
        os.chdir(dir)
        for file in os.listdir():
            if file.endswith('_1.jpg'):
                collection = file[3:5] # коллекции - это 4 и 5 символы из названия. Срезом указали эти символы
                colletction_dir = '../../NewPhoto' + '/' + collection
                
                if not os.path.exists(colletction_dir):
                    os.mkdir(collection_dir)

                shutil.copy2(file, '../../NewPhoto') # копируем файл, который заканчивается на _1.jpg на 2 уровня выше в папку NewPhoto        
        os.chdir('..')
        counter += 1
    except NotADirectoryError:
        pass



