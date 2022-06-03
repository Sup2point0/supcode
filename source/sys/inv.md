# `sys.inv`

The system inventory, containing a plethora of useful presets.


## Contents

- [`aspect`](#aspect)
- [`blank`](#blank)
- [`size`](#size)


### `aspect`
An aspect ratio.

| variable | type | description |
| :------- | :--- | :---------- |
| `wide` | `slot` | 16:9 landscape |
| `full` | `slot` | 4:3 landscape |


### `blank`
A single whitespace character, useful as a placeholder for fields that do not accept empty strings.

```coffee
lock 'blank' = "u+200b"
```


### `size`

```coffee
class 'size' {
  'max'
}
```

| variable | type | description |
| :------- | :--- | :---------- |
| `max` | `slot` | Maximize the window to fill all available space onscreen. |
