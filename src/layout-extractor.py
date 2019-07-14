from cv_utils import extract_metadata_from_img
from io_utils import get_files_in_path
import os.path


if __name__ == '__main__':
    transformed_img_base_path = "C:\\data\\article\\transformed"

    files = get_files_in_path(transformed_img_base_path)

    for file in files:
        file_path = os.path.join(transformed_img_base_path, file)
        print(file_path)

        height, width, horizontal_projection, vertical_projection = extract_metadata_from_img(file_path)

