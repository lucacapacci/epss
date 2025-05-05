import csv
import os
from collections import defaultdict

with open('epss_scores.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    
    writers = {}
    files = {}

    for row in reader:
        cve = row[0]
        if cve.startswith("CVE-") and len(cve) >= 13:
            try:
                year = cve.split("-")[1]
                directory = os.path.join("data_single", year)
                os.makedirs(directory, exist_ok=True)
                path = os.path.join(directory, f"{cve}.csv")
                
                if path not in writers:
                    f = open(path, "w", newline='')
                    writer = csv.writer(f)
                    writer.writerow(header)
                    writers[path] = writer
                    files[path] = f
                
                writers[path].writerow(row)
            except Exception as e:
                print(f"Skipping {cve}: {e}")

    for f in files.values():
        f.close()
