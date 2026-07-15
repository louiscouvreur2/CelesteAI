from pathlib import Path
import numpy as np

for file in Path("recordings").glob("*.npz"):
    print(file)

    try:
        data = np.load(file)
        print("OK")
    except Exception as e:
        print("ERREUR :", e)