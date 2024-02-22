# Control Flow

supcode features all of the conventional control flow constructs found in other languages, and more.


<br>


## Selection

### `if`
If a provided expression evaluates to [truthy](truthiness.md), the code inside the block is run.

```
if cond {
   run()
}

if true {
   sys.out("definitely true")
}

if x = 2.0 {
   sys.out("sup?")
}

if (
   test(sup) != none or
   test(sup) = none
) {
   sys.out("probably true ngl")
}
```

> [!Note]
> Expanding long expressions is always awkward. Lay it out however you feel is best.

### `else`
If the expression is falsy, we can execute an alternative block with `else`. However, this has a `|` (pipe) after it instead.

```
if cond {
   run()
else |
   sprint()
}

if today-is-a-good-day() {
   sys.out("wassup")
else |
   sys.out("sup")
}
```

### `elif`
We can add multiple alternative blocks with `else if`, which can be contracted to `elif`.

```
if cond-1 {
   sip()
else if cond-2
   sap()
elif cond-3
   sop()
else |
   soup()
}

if x > 2.0 {
   sys.out("suppety sup")
elif x = 2.0 |
   sys.out("sup")
elif x < 2.0 |
   sys.out("soupety soup")
else |
   sys.out("you what now")
}
```


<br>


## Loops

### `loop(n)`
We can execute a block a certain number of times.

```
loop(total) {
   sys.out(loop.count)
}

loop(2) {
   sys.out("sup")
}

loop(x * 2) {
   sys.out(x)
}
```

> [!Tip]
> You can enclose the number of loops with brackets to distinguish it from other kinds of loops involving keywords.

### Loop Info
Often, knowing which loop number we are on is useful. This can accessed through the `loop.count` variable. Similarly, `loop.total` represents the value passed to `loop()`.

```
loop(len(a-container)) {
   sys.out("iteration `loop.count` of `loop.total`")
}
```

However, if we have neated loops, `loop` will always refer to the current `loop` scope we are in. To access the outer loop, we can assign it an [**alias**](aliases.md).

```
loop(12) with 'outer' {
   loop(12) with 'inner' {
      sys.out(inner.count * outer.count)
   }
}
```
