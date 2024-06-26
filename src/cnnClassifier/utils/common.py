import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
import unittest


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    '''

    Read a YAML file and return the content
    
    Args:
        path_to_yaml(str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type

    '''

    try:
        with open (path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    '''

    Create directories given in a list of paths

    Args:
        path_to_directories(list): list of path of directories
        ignore_log (bool, optional): ignore if multiple directories are created at once. Defaults to False

    '''

    for path in  path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    '''

    save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file

    '''

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    '''

    Load json file

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attribute instead of dict

    '''

    with open(path) as f:
        content = json.load(f)

    logger.info(f"loaded json file from: {path}")

    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    '''
    
    Save binary data into a file

    Args:
        data (Any): data to be saved as binary
        path (Path): where the data will be saved - path to binary file
    
    '''

    joblib.dump(value=data, filename=path)
    logger.info(f"binary  file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    '''

    Load binary data from a file

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file

    '''

    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")

    return data


@ensure_annotations
def get_size(path: Path)  -> str:
    '''
    
    Get size of a file or directory in KB

    Args:
        path(Path): path of the file

    Returns:
        str: size in KB

    '''

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"


def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    
    with open(filename, "wb") as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())
    


