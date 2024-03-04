## `mention`
Mentions a particular Discord component.

```coffee
func 'mention'(object 'target' = none) {
  
}
```

### Inputs
| input | default | type | description |
| :---- | :------ | :--- | :---------- |
| `object` | `self`

### Example
```coffee
set 'channel' = discord.channel(...)
set 'ping' = discord.mention(discord.user(...))
set 'message' = "sup `ping`, you’re in `mention(channel)`­­"

channel.send(message)
```