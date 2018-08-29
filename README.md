# swiss-army-knife

A set of utilities for Python (3).

## Author

Juha Jokela (juha@jokela.club)

## Runtime

Built for Python 3 runtime.

## Installation

pip install git+https://github.com/juhajokela/swiss-army-knife

## Usage

### monad

```
from swiss_army_knife.monad import Maybe


def get_street_from_company(company):
    return (
        Maybe(company)
        .then(lambda company: company.get('address'))
        .then(lambda address: address.get('street'))
        .value
    )
```
