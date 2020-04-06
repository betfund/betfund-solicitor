# betfund-solicitor

![](https://github.com/betfund/betfund-solicitor/workflows/befund-solicitor/badge.svg)

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
    body_html='TextTest'
)
```

## Tests
`make tests`
