# `view`

A Discord view.

```coffee
struct 'view' {
  num 'timeout' = none
}
```


<br>


## Properties

| property | aliases | type | description |
| :------- | :------ | :--- | :---------- |
| `timeout` | | `num` | The duration which the view will remain active for. |


<br>


## Functions

| function | output | description |
| :------- | :----- | :---------- |
| [`create`](create) | [`view`](#view) | Creates a view. |

### `create`
Creates a view.

```coffee
func[evo] create(ctx) {

}
```

<br>

---

<br>

# `button`

A button within a view.

```coffee
struct view.'button' {
  discord.id 'id'

  str 'text'
  discord.emoji 'icon'
  button.style 'style'
  sys.url 'link'

  lurk 'press'
  lurk 'timeout'
  lurk 'stop'

  discord.view 'view'
}
```


<br>


## Properties

| property | aliases | type | description |
| :------- | :------ | :--- | :---------- |
| `id` | | `discord.id` | The unique identifier. |
| `text` | `label` | `str` | The text displayed. |
| `icon` | | `discord.emoji` | The icon displayed. |
| `style` | | `button.style` | The button colour. |
| `link` | `url` | `sys.url` | The URL the button links to. |
| `view` | `parent` | `discord.view` | The view the button belongs to. |


<br>


## Functions

| function | output | description |
| :------- | :----- | :---------- |
| [`create`](create) | [`view.button`](#button) | Creates a button. |


### `create`
Creates a button.

```coffee
func[evo] create(ctx) [
  | 'id' = none
  | 'text' = sys.presets.blank
  | 'icon' = none
  | 'style' = blurple
  | 'link' = none
]
```
