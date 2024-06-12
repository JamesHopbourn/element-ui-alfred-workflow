import os
import sys
import json

version = os.environ['alfred_workflow_keyword']
data = open(f'{version}.json').read()
data = json.loads(data)

result = []
for item in data:
    if sys.argv[1].lower() not in item["title"].lower():
        continue
    item["icon"] = {"path": "icon.png"}
    result.append(item)
alfredJSON = json.dumps({"items": result}, indent=2, ensure_ascii=False)
sys.stdout.write(alfredJSON)