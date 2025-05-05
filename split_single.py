import csv
import os

with open('epss_scores.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # ['cve', 'epss', 'percentile']

    for row in reader:
        cve = row[0]
        if cve.startswith("CVE-") and len(cve) >= 13:
            try:
                year = cve.split("-")[1]
                directory = os.path.join("data_single", year)
                os.makedirs(directory, exist_ok=True)
                path = os.path.join(directory, f"{cve}.csv")

                with open(path, "w", newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    writer.writerow(row)

            except Exception as e:
                print(f"Skipping {cve}: {e}")
