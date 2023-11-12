import os

from imagesearch import *


def found(location):
    return location[0] > 0 and location[1] > 0


def find_prio_click(image_priority_list):
    for img in image_priority_list:
        location = imagesearch(img)
        if found(location):
            image = os.path.basename(img)
            return {'loc': location, 'btn': image}
    return {}


def validate_resources(image_priority_list) -> bool:
    for img in image_priority_list:
        if not os.path.exists(img):
            print(f'Resource: {os.path.abspath(img)} not found')
            return False
    return True
