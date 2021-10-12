import argparse
import os
#from utils.all_utils import read_yaml, create_directory
import shutil
import logging

from app.main.service.utils.all_utils import read_yaml, create_directory
from app.main.util.apiResponse import apiresponse, ApiResponse

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'running_logs.log'), level=logging.INFO, format=logging_str,
                    filemode="a")

def get_data(config_path):
    config = read_yaml(config_path)
    source_download_dirs = config["source_download_dirs"]
    local_data_dirs = config["local_data_dirs"]
    create_directory(local_data_dirs)
    shutil.copy(source_download_dirs[0],local_data_dirs[0])
    logging.info(f"Input data copied successfully from {source_download_dirs} to {local_data_dirs}")


def get_data_new(data):
    try:
        config = read_yaml("app/config/config.yaml")
        input_data_path = data['input_data_path']
        source_download_dirs = None
        if input_data_path:
            source_download_dirs = input_data_path
        else:
            source_download_dirs = config["source_download_dirs"]

        local_data_dirs = config["local_data_dirs"]
        create_directory(local_data_dirs)
        shutil.copy(source_download_dirs, local_data_dirs[0])
        logging.info(f"Input data copied successfully from {source_download_dirs} to {local_data_dirs}")

        apiResponse = ApiResponse(True, "data downloaded successfully", None, None)
        return apiResponse.__dict__, 200

    except Exception as e:
        error = ApiResponse(False, 'something went wrong',
                            None, str(e))
        return (error.__dict__), 500



if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="app/config/config.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info("\n\n\n>>>>> stage one started")
        get_data(config_path=parsed_args.config)
        logging.info("stage one completed! all the data are saved in local >>>>>")
    except Exception as e:
        #logging.exception(e)
        raise e
