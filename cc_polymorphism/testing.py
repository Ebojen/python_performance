from pathlib import Path
import os

print(os.path.relpath('results.json'))
print([x for x in Path('.').iterdir()])
