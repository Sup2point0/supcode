# `emoji`

A Discord emoji.

```coffee
struct 'emoji' {
  intr discord.id 'id'
  
  evo func 'str'
}
```

<br>

# Properties

| property | aliases | type | description |
| :------- | :------ | :--- | :---------- |
| `id` | `token` | `discord.id` | The id of the emoji used by Discord for identification. |

<br>

# Functions

| function | output | description |
| :------- | :----- | :---------- |
| [`create`](#create) | [`emoji`](#emoji) | Creates an emoji. |


## `create`
Creates an emoji.

```coffee
func create(ctx = void, id)
```

## Options
| option | aliases | type | description |
| :----- | :------ | :--- | :---------- |
| `ctx` | | `ctx` | The name of the emoji. If not provided, the first argument should be the id of the emoji. |
| `id` | | `discord.id` | The id of the emoji used by Discord for identification. |
