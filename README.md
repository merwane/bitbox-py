Bitbox-py: A Python SDK for creating great Bitcoin Cash applications
==============================================

**Bitbox-py** is the Python port of [Gabriel Cardona](https://github.com/cgcardona)'s great Bitcoin Cash Javascript SDK [Bitbox](https://github.com/Bitcoin-com/bitbox-sdk).

I ported Bitbox to Python to make Bitcoin Cash more accessible to developers and therefore to the world.

Usage
------------
Install **Bitbox-py** using Pip:
```
pip install bitbox-py
```

Documentation
------------
Everything is basically the same as [Bitbox-sdk](https://developer.bitcoin.com/bitbox), except methods are not using camelCase in order to fit with Python's style.

You can refer to the official [Documentation](https://developer.bitcoin.com/bitbox).

**Example:**

Javascript:
```javascript
import { BITBOX } from 'bitbox-sdk'

let bitbox = new BITBOX();

let result = bitbox.Address.toLegacyAddress('bitcoincash:qrxjktfjdse3ll0ttrll20gykuhqjw764queg3w2tj');

console.log(result);
// 1KhqFHWHUoJ72tuQCkhV1m1Sk7bXCiKJgN
```

Python:
```python
import bitbox

result = bitbox.Address.to_legacy_address('bitcoincash:qrxjktfjdse3ll0ttrll20gykuhqjw764queg3w2tj')

print(result)
# 1KhqFHWHUoJ72tuQCkhV1m1Sk7bXCiKJgN
```

OR import by class:

```python
from bitbox import Address

result = Address.to_legacy_address('bitcoincash:qrxjktfjdse3ll0ttrll20gykuhqjw764queg3w2tj')

print(result)
# 1KhqFHWHUoJ72tuQCkhV1m1Sk7bXCiKJgN
```

Contributing
------------
You can find the instructions for contributing on [CONTRIBUTING.md](https://github.com/merwane/bitbox-py/blob/master/CONTRIBUTING.md).

### Features you can add that aren't implemented yet:
* The ability to get BitDB data by query.
* ECPair utilities (fromWIF, fromPublicKey etc)
* HDNode methods (fromSeed, derive etc)
* Schnorr utilities
* TransactionBuilder methods

Notes and credits
------------
* [Gabriel Cardona](https://github.com/cgcardona) for creating the original Javascript Bitbox-sdk, and for inspiring me everyday!
* [Bitcoin.com](https://www.bitcoin.com/) for enabling millions of individuals to use an uncensorable peer-to-peer cash system everyday.
* [Rosco Kalis](https://github.com/rkalis) for encouraging me to port Bitbox to Python.
