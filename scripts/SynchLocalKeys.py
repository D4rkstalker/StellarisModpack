# Synchronizes new keys in English to other languages while keeping the previous keys untouched.

from pathlib import Path

ref_language = 'english'
LOCAL_DIR = Path('..') / 'localisation'

#Get all reference localisation files:
files = list(LOCAL_DIR.glob(ref_language+'/*.yml'))

#Get all languages directories:
languages = [x.name for x in LOCAL_DIR.iterdir() if x.is_dir() and ref_language not in x.name]

#Test settings:
# languages = ["other"]
# file_location = './tests/'
# file_extension = ".yml"
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
            print("Added {0} key to {1}".format(key, local_file.name))

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
        file.write('l_{0}:\n\n    '.format(language))

for file in files:
    try:
        ref_keys = getLocalisationKeys(file)
    except:
        print("Skipping file: ", file.name)
        continue
    for language in languages:
        language_file = LOCAL_DIR / language / file.name.replace(ref_language, language)
        try:
            current_keys = getLocalisationKeys(language_file)
        except FileNotFoundError: #No file for the current language
            createNewLanguageFile(language_file, language)
            current_keys = {}


        missing_keys = getDiffDict(ref_keys, current_keys)
        if (missing_keys):
            appendLocalisationKeys(language_file, missing_keys)
