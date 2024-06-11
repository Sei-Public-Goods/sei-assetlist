# /// script
# dependencies = [
#   "requests==2.32.3",
# ]
# ///

import json
import requests

with open('assetlist.json') as json_data:
    assetList = json.load(json_data)
    chains = ['pacific-1', 'atlantic-2', 'arctic-1']
    for chain in chains:
        items = assetList[chain]
        for token in items:
            if token['images']:
                for suffix in token['images']:
                    stripped_name = token['name'].replace(" ","")
                    file_name = f"{stripped_name}.{suffix}"
                    token['images'][suffix] = f"https://raw.githubusercontent.com/Sei-Public-Goods/sei-assetlist/main/images/{file_name}"
    
    with open('assetlist.json', 'w') as file:
        json.dump(assetList, file, indent=4)
    

        
