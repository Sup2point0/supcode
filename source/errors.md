# Inbuilt Errors

A collection of all the inbuilt errors in Supcode.

## Contents

`-flux`
- `synflux`
- `afflux`
- `influx`
- `reflux`
- `deflux`
- `uniflux`
- `efflux`
- `conflux`

`-dux`
- `redux`
- `indux`

`-crux`
- `accrux`
- `valcrux`

`-trux`
- `caltrux`
- `cinatrux`
- `cicatrux`

## `flux`

### `synflux`

A syntax error.

| error | description | example | source |
| :---- | :---------- | :------ | :----- |
| `synflux` | generic syntax error | `sup sup` | Evoked when no specific syntax error could be evoked.
| `.unknown` | unrecognized syntax | `print(sup ==== )` | Unrecognized characters, symbols and/or programming language detected. Rarely evoked due to supcode’s extensive character support (through Resinax). |
| `.openseg` | segment left unclosed | `if true { sys.out("sup")` | Missed a bracket or any similar segment encloser |

### `afflux`

A runtime error.

| error | description | example | source |
| :---- | :---------- | :------ | :----- |
| `.overflow` | memory overflow | `set 'crash' = 0~(69^420)` | consuming too much memory |
| `.timeout` | operation timeout | `...` | an operation left hanging |

### `influx`

A location error.

| error | description | example | source |
| :---- | :---------- | :------ | :----- |
| `.undefined` | undefined element | `sys.out(sup)` | referencing an undefined element
| `.index` | index error | `(1, 2, 3)#4` | indexing an iterable out of its range |
| `.key` | key error | `{"sup": 2.0}#"sus"` | looking up a key that does not exist in a mapping |

### `reflux`

An iteration error.

| error | description | example | source |
| :---- | :---------- | :------ | :----- |
| `.recurse` | maximum recursion depth reached | `...` | reaching a recursion depth of 200 |

### `deflux`

A calculation error.

| error | description | example | source |
| :---- | :---------- | :------ | :----- |
| `.zerodiv` | division by 0 error | `2 / 0` | dividing any *valid* value by a value of 0 |
| `.infidiv` | division by infinity error | `2 / inf` | dividing any *valid* value by a value of infinity |

### `uniflux`

Various errors.

| error | description | example | source |
| :---- | :---------- | :------ | :----- |
| `.type` | invalid type | `"sup" / 2` | argument of an invalid type |
| `.value` | unsuitable value | "sup" * 1.2 | argument of an unsuitable value |
| `.logic` | invalid logic | "sup" > 2 | |

### `efflux`

...

| error | description | example | source |
| :---- | :---------- | :------ | :----- |


### `conflux`

A generic interpreter error.

| error | description | example | source |
| :---- | :---------- | :------ | :----- |
| `.exit` | an unexpected exit call | `...` | |
| `.interrupt` | a system interrupt | `...` | |
| `.void` | not implemented | `evoke efflux.void` | indicates that a feature has not yet been implemented |

## `dux`

...

## `crux`

...

## `trux`

...
