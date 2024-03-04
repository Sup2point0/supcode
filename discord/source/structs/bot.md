# `bot`

A Discord bot.

```coffee
struct 'bot' {
  discord.id 'token' = none
  pool[none | default | all] 'intents' = slot(default)
  str 'prefix' = ""
}
```

<br>

# Properties

| property | aliases | type | description |
| :------- | :------ | :--- | :---------- |
| `token` | `key` | `discord.token` | API key of the bot. |
| `intents` | | `slot` | Intents the bot will be subscribed to. |
| `prefix` | `command_prefix` | `(str)s` | Prefix that precedes all commands. |

<br>

# Functions

| function | output | description |
| :------- | :----- | :---------- |
| [`create`](#create) | [`bot`](#bot) | Creates a bot. |
| [`start`](#start) | `none` | Starts the bot. |


## `create`
Creates a bot.

```coffee
evo func create [
  | token = none
  | intents = default
]
```

### Inputs
| input | aliases | type | description |
| :---- | :------ | :--- | :---------- |


## `start`
Starts the bot.

```coffee
evo func start() []
```
