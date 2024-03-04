# `embed`

A Discord embed.

```coffee
struct 'embed' {
  int 'len'
  pool[rich | image | video | gifv | article | link] 'type'
  dict 'dict'
  
  class 'head' {
    str 'text' = sys.inv.blank
    sys.url 'link'
    class 'author' {
      str 'text'
      sys.url 'link'
      sys.url 'icon'
    }
  }
  class 'body' {
    str 'text'
    hex 'col'
  }
  class 'foot' {
    str 'text'
    sys.url 'icon'
    datix.time, datix.date, datix.datetime 'time'
  }
  class 'assets' {
    sys.url 'thumb'
    sys.url 'image'
  }

  (field)s 'fields'
  
  evo func 'add'
  evo func 'insert'
  evo func 'del'
  evo func 'clear'

  func 'clearfields'

  struct 'field'
}
```


<br>


## Properties

| property | aliases | type | description |
| :------- | :------ | :--- | :---------- |
| `len` | `length` | `int` | The total character count of the embed, including titles and footers. Useful for checking if an embed is within the 6000 character count limit. |
| `dict` | `info`, `data` | `dict` | A dictionary representation of the embed. Useful for convenient transfer. |
| `type` | | `slot` | The type of the embed. |
| [`head`](#head) | | `class` | The header of the embed. |
| [`body`](#body) | `main` | `class` | The main body of the embed, excluding fields. |
| [`foot`](#foot) | | `class` | The footer of the embed. |
| [`assets`](#assets) | `media` | `class` | Any media within the embed. |
| `fields` | | [`(embed.field)s`](#embedfield) | The fields of the embed. |

### `head`
| property | aliases | type | description |
| :------- | :------ | :--- | :---------- |
| `head.text` | `title` | `str` | The title text. |
| `head.link` | `url` | `sys.url` | The link of the title. |
| `head.author.text` | `name` | `str` | The displayed author. |
| `head.author.icon` | | `sys.url` | The displayed author icon. |

### `body`
| property | aliases | type | description |
| :------- | :------ | :--- | :---------- |
| `body.text` | | `str` | The main text. |
| `body.col` | `colour`, `color`| [`discord.col`](colour.md) | The accent colour. |

### `foot`
| property | aliases | type | description |
| :------- | :------ | :--- | :---------- |
| `foot.text` | | `str` | The footer text. |
| `foot.icon` | | `sys.url` | The footer icon. |
| `foot.time` | `timestamp`| `datix.time`, `datix.date`, `datix.datetime`  | The displayed timestamp. |

### `assets`
| property | aliases | type | description |
| :------- | :------ | :--- | :---------- |
| `assets.thumb` | `thumbnail`, `icon`| `sys.url`  | The thumbnail. |
| `assets.image` | | `sys.url` | The image. |


<br>


## Functions

| function | output | description |
| :------- | :----- | :---------- |
| [`create`](#create) | [`embed`](#embed) | Creates an embed. |
| [`clearfields`](#clearFields) | [`embed`](#embed) | Clears fields from the embed. |

### `create`
Creates an embed.

```coffee
func[evo] create(ctx) [
  | type = rich
  | dict = auto
  |
  | head {
    text = sys.inv.blank
    link = none
    author {
      text = none
      link = none
      icon = none
    }
  }
  | body {
    text = sys.inv.blank
    col = none
  }
  | foot {
    text = sys.inv.blank
    icon = none
    time = none
  }
  | assets {
    thumb = none
    image = none
  }
  |
  | fields = none
]
```

#### Inputs
{~~}

#### Examples
```coffee
create discord.embed('content') [
  | head.title = "Example Embed"
  | body.text = "testing testing"
  | foot.text = "sup"
]
```

Specifying the options with `let` afterwards allows you to adjust values based on previous options.

```coffee
create discord.embed('content') {
  let head.title = "Example Embed"
  let body.text = "testing *`head.title`* testing"
  let foot.text = case(body.text)[lower]
}
```

### `clearfields`
Clears fields from the embed.

```coffee
func embed.clearfields(
  'index' = all
) {} to embed
```

#### Inputs
| input | aliases | type | description |
| :---- | :------ | :--- | :---------- |
| `index` | `fields` | `index`, `span`, `slot` | The specific index or indexes to clear. |

#### Outputs
| output | type | source | notes |
| :----- | :--- | :----- | :---- |
| the embed itself | [`embed`](#embed) | always | Allows for fluent chaining with other functions. |

#### Example
```coffee
create discord.embed('content') [title = "Example Embed" | fields = (
  embed.field()[title = "first" | text = "sup"],
  embed.field()[title = "second" | text = "sup"],
  embed.field()[title = "third" | text = "sup"],
  embed.field()[title = "fourth" | text = "sup"],
  embed.field()[title = "fifth" | text = "sup"],
)]

content.clearfields(1)
content.clearfields(2~3)
content.clearfields()
```

<br>

---

<br>

# `embed.field`

An embed field.

```coffee
struct embed.'field' {
  int 'index'

  str 'title' = sys.inv.blank
  str 'text' = sys.inv.blank
  bool 'inline' = false
}
```


<br>


## Properties

| property | aliases | type | description |
| :------- | :------ | :--- | :---------- |
| `title` | `name` | `str` | The title text. |
| `text` | `value` | `str` | The main text. |
| `inline` | | `bool` | Whether or not the field is inline. If `true`, the field before it must also be inline for it have effect. |


<br>


## Functions

| function | output | description |
| :------- | :----- | :---------- |
| `create` | [`embed.field`](#embedfield) | Creates an embed field. |

### `create`
Creates an embed field.

```coffee
func create(ctx) [
  | title = sys.inv.blank
  | text = sys.inv.blank
  | inline = false
]
```

#### Inputs
| input | aliases | type | description |
| :---- | :------ | :--- | :---------- |
| `title` | `name` | `str` | The title text. |
| `text` | `value` | `str` | The main text. |
| `inline` | | `bool` | Whether or not the field is inline. If `true`, the field before it must also be inline for it have effect. |
