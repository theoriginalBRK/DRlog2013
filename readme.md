# Red Cross Test Data

This is a test space for putting together the structure for a dynamic, searchable disaster response data repository. 

## Data

A script is included for anonymizing and translating the response
spreadsheet into JSON:

```sh
python scripts/csv2json.py DATA.csv data/webready.json
```

Additionally, a snapshot of this script's output is stored in
data/sample.json.