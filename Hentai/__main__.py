import glob
import os
import asyncio
import sys
from pathlib import Path
import logging
import importlib
from Hentai import tsoheru, psoheru

#logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def load_module(plugin):
    path = Path(f"Hentai/plugins/{plugin}.py")
    modlinks = "Hentai.plugins.{}".format(plugin)
    spec = importlib.util.spec_from_file_location(modlinks, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin)
    spec.loader.exec_module(load)
    sys.modules["Hentai.plugins." + plugin] = load
    print("Successfully loaded " + plugin + " module.")


path = "Hentai/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_module(plugin_name.replace(".py", ""))


psoheru.start()
print("Bot Started")    
if __name__ == "__main__":
    if tsoheru:
        tsoheru.run_until_disconnected()
    else:
        pass
    
loop = asyncio.get_event_loop()
loop.run_forever()
