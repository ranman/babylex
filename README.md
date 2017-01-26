# BabyLex is a quick python wrapper for lex

# The lex service is in preview and this library may not be maintained or change as lex changes

----------------------------

# Quick Start
```python
from babylex import LexSession
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

You can work with audio as well:

```python
import pyaudio
p = pyaudio.PyAudio()
lex_session = LexSession("WhereIsRandall", "$LATEST", "ranman")
resp = lex_session.content("Where is Randall", "text/plain; charset=utf-8", "audio/pcm")
stream = p.open(format=p.get_format_from_width(width=2), channels=1, rate=16000, output=True)
stream.write(resp.content)
stream.stop_stream()
stream.close()
```