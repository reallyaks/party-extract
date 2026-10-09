# party-extract

Reads one recital shaped like `between Harbor Street LLC ("Customer") and Northline Data LLC ("Vendor")`.

Not legal advice. It does not find every name in the document, only that between-and pair.

## Run

```bash
python -m party_extract samples/recital.txt --out /tmp/parties.json
python -m unittest discover -s tests
```

Committed output: [samples/parties.json](samples/parties.json). Python 3.10+. No packages.
