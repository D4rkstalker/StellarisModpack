# Generates a single localisation file for each language + the reference.
# Overwrites previous changes with new ones.

from pathlib import Path

ref_language = 'english'
REF_DIR = Path('..') / 'localisation'
LOCAL_DIR = Path('..') / 'localisation_to_export'

#Get all reference localisation files:
files = list(REF_DIR.glob(ref_language+'/*.yml'))

#Get all languages directories:
languages = [x.name for x in REF_DIR.iterdir() if x.is_dir()]

#Test settings:
# languages = ["other"]
# file_location = './tests/'
# files = ['test_1_l_', 'test_2_l_']

def getLocalisationKeys(ref_file):
    '''
        Returns a dictionary with the localisation
        keys as keys and the localisation
        content as values.
    '''
    local_map = {}

    try:
        with ref_file.open(encoding='utf-8') as file:
            next(file) #Skips first line
            for line in file:
                line = line.lstrip() #Clears whitespaces
                if line and not line.startswith('#'): #Ignores comments
                    split_line = line.split(':', 1) #Separate keys and text
                    local_map[split_line[0]] = split_line[1]
    except FileNotFoundError:
        print("File Not Found: ", ref_file.name)
        raise
    
    print("Collected {0} from file: {1}".format(len(local_map), ref_file.name))
    return local_map

def appendLocalisationKeys(local_file, localisationMap):
    '''
        Appends a dictionary with the localisation
        keys and content to a file.
    '''

    with local_file.open('a', encoding='utf-8') as file:
        file.write('\n')
        for key in localisationMap:
            file.write('    {0}:{1}'.format(key, localisationMap[key]))
        print("Create new file: {0}".format(local_file.name))

def getDiffDict(ref_dict, comp_dict):
    '''
        Return a dictionary with the missing items from comp_dict
        using ref_dict as reference.
    '''

    ref_keys = ref_dict.keys()  # retrieve keys of the reference dictionary
    comp_keys = comp_dict.keys()  # retrieve keys of the other dictionary
    missing_keys = [key for key in ref_keys if key not in comp_keys]

    result_dict = {}
    for key in missing_keys:
        result_dict[key] = ref_dict[key]

    return result_dict


def createNewLanguageFile(new_file, language):
    '''
        Creates a new file in the specified path with the header:
        l_[language passed]:
    '''
    print("Creating new file: ", new_file)
    with new_file.open('w', encoding='utf-8') as file:
        file.write('\ufeff')
        file.write('l_{0}:'.format(language))


#Main:
every_ref_key = {}
for file in files:
    ref_keys = {"\n    #{0}".format(file.name): "\n"}
    try:
        ref_keys.update(getLocalisationKeys(file))
    except:
        print("Skipping file: ", file.name)
        continue
    every_ref_key.update(ref_keys)

print();
for language in languages:
    language_file = LOCAL_DIR / ("pw_l_" + language + ".yml")
    createNewLanguageFile(language_file, language)
    appendLocalisationKeys(language_file, every_ref_key)
    print("Files creates with {0} keys in total".format(
        len(every_ref_key) - len(files)))
