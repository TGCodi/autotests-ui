import platform
import sys
from config import settings

def create_allure_environment_file():
    os_info = f"{platform.system()}, {platform.release()}"
    python_version = sys.version

    env_data = settings.model_dump()
    env_data.update({
        "os_info": os_info,
        "python_version": python_version
    })

    items = [f'{key}={value}' for key, value in env_data.items()]

    properties = '\n'.join(items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)