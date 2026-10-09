# party-extract

Reads one recital shaped like `between Harbour Street Limited ("Customer") and Northline Data Limited ("Supplier")`.

It does not find every name in the document. Only that between-and pair.

## Run

```bash
python -m party_extract samples/recital.txt --out /tmp/parties.json
python -m unittest discover -s tests
```

Committed output: [samples/parties.json](samples/parties.json). Python 3.10+. No packages.
