# `user`

A Discord user.

```coffee
struct 'user' [channel] {
  intr discord.id 'id'
  intr str 'shard'

  intr str 'str'

  intr discord.asset 'avatar'

  synth func 'mention'
}
```

<br>

# Properties

| property | aliases | type | description |
| :------- | :------ | :--- | :---------- |

<br>

# Functions

| function | output | description |
| :------- | :----- | :---------- |