# Inbuilt Errors

A reference for all the inbuilt errors in Supcode.

```coffee
struct sys.'error' {
  intr str 'str'
}
```


## Contents

[`-flux`](#flux)
- [`synflux`](#synflux)
- [`afflux`](#afflux)
- [`uniflux`](#uniflux)
- [`influx`](#influx)
- [`reflux`](#reflux)
- [`deflux`](#deflux)
- [`efflux`](#efflux)
- [`conflux`](#conflux)

[`-dux`](#dux)
- [`condux`](#condux)
- [`indux`](#indux)
- [`redux`](#redux)

[`-crux`](#crux)
- [`accrux`](#accrux)
- [`valcrux`](#valcrux)

[`-trux`](#trux)
- [`caltrux`](#caltrux)
- [`cicatrux`](#cicatrux)
- [`cinatrux`](#cinatrux)


## `flux`

### `synflux`
A syntax error.

| error | description | example | source |
| :---- | :---------- | :------ | :----- |
| `synflux` | generic syntax error | `sup sup` | Evoked when no specific syntax error could be evoked.
| `.unknown` | unrecognized syntax | `print(sup ==== )` | Unrecognized characters, symbols and/or programming language detected. Rarely evoked due to supcode’s extensive character support (through Resinax). |
| `.openseg` | segment left unclosed | `if true { sys.out("sup")` | Missed a bracket or any similar segment encloser. |

### `afflux`
A runtime error.

| error | description | example | source |
| :---- | :---------- | :------ | :----- |
| `.overflow` | memory overflow | `set 'crash' = 0~(69^420)` | Consuming too much memory. |
| `.timeout` | operation timeout | `...` | An operation left hanging. |

### `uniflux`
Various errors.

| error | description | example | source |
| :---- | :---------- | :------ | :----- |
| `.type` | invalid type | `"sup" / 2` | Input of an invalid type. |
| `.value` | unsuitable value | "sup" * 1.2 | Input of an unsuitable value. |
| `.logic` | invalid logic | "sup" > 2 | |

### `influx`
A location error.

| error | description | example | source |
| :---- | :---------- | :------ | :----- |
| `.undefined` | undefined element | `sys.out(sup)` | Referencing an undefined element. |
| `.index` | index error | `(1, 2, 3)#4` | Indexing an iterable out of its range. |
| `.key` | key error | `{"sup": 2.0}#"sus"` | Looking up a key that does not exist in a mapping. |

### `reflux`
An iteration error.

| error | description | example | source |
| :---- | :---------- | :------ | :----- |
| `.recurse` | maximum recursion depth reached | `...` | Reaching a recursion depth of 200. |

### `deflux`
A calculation error.

| error | description | example | source |
| :---- | :---------- | :------ | :----- |
| `.zerodiv` | division by 0 error | `2 / 0` | Dividing any *valid* value by a value of 0. |
| `.infidiv` | division by infinity error | `2 / inf` | Dividing any *valid* value by a value of infinity. |

### `efflux`
...

| error | description | example | source |
| :---- | :---------- | :------ | :----- |


### `conflux`
A generic interpreter error.

| error | description | example | source |
| :---- | :---------- | :------ | :----- |
| `conflux` | a generic generic interpretor error. | |
| `.exit` | an unexpected exit call | `...` | |
| `.interrupt` | a system interrupt | `...` | |
| `.void` | not implemented | `evoke efflux.void` | Indicates that a feature has not yet been implemented. |


## `dux`

### `accrux`
An extension error.

| error | description | example | source |
| :---- | :---------- | :------ | :----- |
| `accrux` | generic extension-related error | | Evoked when no specific extension error could be evoked. |
| `.influx` | extension not found | `activate randomExtension` | |


## `crux`

...


## `trux`

...
