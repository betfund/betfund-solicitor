# betfund-solicitor

![](https://github.com/betfund/betfund-solicitor/workflows/Befund%20Solicitor/badge.svg)

Workflow to send automated emails asking for favorite line votes.

## Installation

## Usage
```python
from betfund_solicitor import Message

message = Message(
    reason='test',
    sender='mitchbregs@gmail.com',
    to='leonkozlowski@gmail.com',
    subject='SubjectTest',
    body_text='TextTest',
    body_html=''
)
```

## Tests
`pytest --cov=betfund_solicitor .`
