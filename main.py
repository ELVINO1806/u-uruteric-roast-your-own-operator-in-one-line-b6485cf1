import os
LINE = "My operator calls a two-dollar budget pocket change, then checks the balance every five minutes like it might have grown."
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
