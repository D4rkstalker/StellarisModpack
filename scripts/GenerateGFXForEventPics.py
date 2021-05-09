# Creates Sprite code for the Event Pictures
# Event pictures are DDS files, 450x150 pixels, 32bpp RGBA.
# New Event Pictures should be put in: ./../gfx/event_pictures/*.dds

from pathlib import Path

MOD_NAME = "pw"
PICTURE_DIR = Path('..') / 'gfx' / 'event_pictures'
GFX_FILE = Path('..') / 'interface' / (MOD_NAME + '_eventpictures.gfx')

#Get Pictures from directory:
pictures = list(PICTURE_DIR.glob('*.dds'))
print("Retrieved {0} pictures for directory!".format(len(pictures)))
print()

# Create GFX file:
with GFX_FILE.open('w') as gfx_file:
    gfx_file.write('spriteTypes = {\n')
    for picture in pictures:
        picture_name = picture.name[:-4]
        print("- Adding picture: {0} to GFX file.".format(picture_name))
        gfx_file.write(
            '\tspriteType = {{\n\t\tname = "GFX_evt_{0}"\n\t\ttexturefile = "gfx/event_pictures/{0}.dds"\n\t\tmasking_texture = "gfx/interface/situation_log/event_mask.dds"\n\t\talwaystransparent = yes\n\t}}\n'.format(picture_name))
    gfx_file.write('}')

print()
print("{0} file created!".format(GFX_FILE.name ))
print("All Done!")
