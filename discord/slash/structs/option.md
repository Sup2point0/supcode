# `option`

A slash command option.

```coffee
struct 'option' {
  str 'name'
  str 'description'
  type, pool, dict 'options'
  var 'default'
  bool 'autocomplete'
  bool 'required'

  num 'min'
  num 'max'
}
```


<br>


## Properties

| property | aliases | type | description |
| :------- | :------ | :--- | :---------- |
| `name` | | `str` | The displayed name of the option. |
| `description` | `desc` | `str` | The description of the option. |
| `options` | `choices` | `type`, `pool`, `dict` | The collection of options that can be selected. |
| `default` | | `slot`, variable | The option selected by default. |
| `autocomplete` | `autofill`, `auto` | `bool` |  |
| `required` | `req` | `bool` |  |
| `min` | | `num` |  |
| `max` | | `num` |  |


<br>


## Functions

| function | output | description |
| :------- | :----- | :---------- |
| [`create`](create) | [`slash.option`](#option) | Creates a slash option. |

### `create`
Creates a slash option.

```coffee
func[evo] create(ctx) [
  | name = default
  | description = none
  | options = none
  | default = none
  | autocomplete = false
  | required = true
  | min = none
  | max = none
]
```
