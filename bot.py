import threading
from time import sleep
import sys
import json
import requests

fname = "config.json"

with open(fname, "r") as f:
    cfg = json.load(f)
    params = {"entry.{}".format(cfg["ety"][k]): cfg["opt"][k] for k in cfg["ety"].keys()}
    def entrada():
            requests.get(cfg["url"] + "formResponse", params=params)
            
    def main():
        c = 0                                                           
        for i in range(int(cfg["qtd"])):
            t = threading.Thread(target=entrada, args=[])                            
            t.start()

            c += 1

            sys.stdout.write('\r%05d votos...' %(c))
            while(threading.activeCount() > 30):
                sleep(0.001)
        print('')
        
    main()


