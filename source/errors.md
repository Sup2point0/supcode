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
| `.openseg` | segment left unclosed | `if true { sys.out("sup")` | missing a bracket or any similar segment encloser | 

### `afflux`

A runtime error.

| error | description | example | source |
| :---- | :---------- | :------ | :----- |
| `.overflow` | memory overflow | `set 'crash' = 0~(69^420)` | consuming too much memory |

### `influx`

An location error.

| error | description | example | source |
| :---- | :---------- | :------ | :----- |

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
| `.infodiv` | division by infinity error | `2 / inf` | dividing any *valid* value by a value of infinity |

### `efflux`

| error | description | example | source |
| :---- | :---------- | :------ | :----- |

### `conflux`

A generic interpreter error.

| error | description | example | source |
| :---- | :---------- | :------ | :----- |

## `dux`

...

## `crux`

...

## `trux`

...
