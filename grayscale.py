#python grayscale.py --input color --output blackwhite

from PIL import Image, ImageFilter
from glob import glob
from argparse import ArgumentParser

parser = ArgumentParser(description='Zmiana jpgów na czarno-białe.')
parser.add_argument('--input', help='Folder z którego pobieram obrazy.', required=True)
parser.add_argument('--output', help='Folder do którego zapisze obrazy.', required=True)
args = parser.parse_args()

for path in glob(args.input + '/*'):
    directory, filename = path.split('\\')
    print(path, directory, filename)

    with Image.open(path) as new_image:
        grayscale_image = new_image.convert('L')
        modified_image = grayscale_image.filter(ImageFilter.DETAIL)
        grayscale_image.save(args.output + '/' + filename)
        modified_image.save(args.output + '/modified_' + filename)