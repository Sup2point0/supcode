# A Whirlwind Tour of supcode

While I find time to get round to trying to implement supcode, here are some of its features and quirks I've got planned!

> [!Note]
> For a rundown of supcode’s design principles and axioms, see [Axioms](axioms.md).


<br>


## Flavourful Identifiers

supcode uses `kebab-case` for identifiers:

```coffee
set 'full-flavour' = true
```

You can also use trailing `?` and `!` for conditions and in-place mutations:

```coffee
func 'play-track!' (~Track 'track')
{
   alt track.played? = true
   alt track.total-plays + 1
}
```


<br>


## Partially Applicable Functions

Functions accept **primary parameters** in `()`, **partial parameters** in `[]`, and a **block parameter** in `{}`:

```coffee
async func 'respond' (ctx) [
   String 'message'
]
```

You can *partially* apply a function’s partial parameters, which doesn’t call the function, but returns a modified version:

```coffee
set 'items' = List(6, 9, 4, 2, 0)

filter(items)[pred = is-even]

\ equivalent to:
set 'filter-even' = filter[pred = is-even]

filter-even(items)
```

<br>


## Flexible Function Chaining

A function with 1 or more primary parameters can be called as a method on its first argument:

```coffee
\ these are equivalent:
attack(target)
target.attack()

\ these are equivalent:
add(inventory, item)
inventory.add(item)
```

Chaining pipelines becomes fluid and follows their actual order!

```coffee
take(skip(map(filter(players))))

\ equivalent to...
take(skip(map(players.filter())))
take(skip(players.filter().map()))
take(players.filter().map().skip())
players.filter().map().skip().take()

players.filter()
   .map()
   .skip()
   .take()
```

<br>


## Functions Without Parentheses

Functions accepting 1 primary parameter can be called without parentheses:

```coffee
\ these are equivalent:
tokenise(text)
tokenise text
```

Making function application right-associative means you can call an entire pipeline without parentheses:

```coffee
\ these are all equivalent:
parse(tokenise(text))
parse tokenise(text)

parse (tokenise text)
parse tokenise text
```

Hence supcode has barely any keywords or special syntax, because they can all be achieved through functions!

<br>


## Separate Struct Declaration and Conditional Evolutions

Like Rust, supcode can split a struct’s declaration and implementation, and also conditionally implement functionality!

```coffee
struct 'Fruit-Salad' [T]
{
   | List[T] tracks
}

evolve Fruit-Salad[Track]
{
   func 'banana-breeze' (self)
   {
      self.play!()
   }
}
```
