# EPSS Mirror

This repository contains a continuously updated mirror of the [EPSS data](https://www.first.org/epss/data_stats), available in CSV format.

Data is refreshed every **2 hours** and organized in multiple formats for easier access and analysis.

## Repository Structure

CVE data is available in the following formats:

1. **All CVEs in a single file**  
   Get all CVEs &rarr; https://raw.githubusercontent.com/lucacapacci/epss/refs/heads/main/epss_scores.csv
   

3. **Files grouped by year**  
   Example: get all CVEs starting with "CVE-2025-" &rarr;
https://raw.githubusercontent.com/lucacapacci/epss/refs/heads/main/data_years/epss_scores_2025.csv

4. **Files grouped by year and first digit of the CVE ID**  
   Example: get all CVEs starting with "CVE-2025-0" &rarr; https://raw.githubusercontent.com/lucacapacci/epss/refs/heads/main/data_groups/epss_scores_2025_0.csv

5. **Single file per CVE**  
   Example: get CVE-2025-0108 &rarr;
   https://raw.githubusercontent.com/lucacapacci/epss/refs/heads/main/data_single/2025/CVE-2025-0001.csv

---

## Usage Examples

### Using `curl`

```bash
curl -L https://raw.githubusercontent.com/lucacapacci/epss/refs/heads/main/data_single/2025/CVE-2025-0001.csv
```

### Using Python

```python
import requests
import csv
from io import StringIO

url = 'https://raw.githubusercontent.com/lucacapacci/epss/refs/heads/main/data_single/2025/CVE-2025-0001.csv'
response = requests.get(url)
csv_file = StringIO(response.text)
reader = csv.reader(csv_file)
for row in reader:
    print(row)
```

---

## Update Frequency

Data is automatically updated every **2 hours**, providing near real-time CVE tracking.
