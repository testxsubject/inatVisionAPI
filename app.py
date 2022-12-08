import sys
import yaml
sys.path.append("./lib")
from inat_vision_api import InatVisionAPI  # noqa: E402

CONFIG = yaml.safe_load(open("config.yml"))

api = InatVisionAPI(CONFIG)
app = api.app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6006)
