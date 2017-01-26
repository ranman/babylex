```python
from babylex import LexSession()
lex_session = LexSession("WhereIsRandall", "$LATEST", "ranman")
resp = lex_session.text("where is randall")
print resp
```

returns:
`{u'slotToElicit': None,
  u'dialogState': u'Fulfilled',
  u'intentName': u'WhereRandall',
  u'responseCard': None, 
  u'message': u'Randall is in claremont, ca', 
  u'slots': {},
  u'sessionAttributes': {}}`
