# Grammar

This document outlines supcode’s [parsing expression grammar<sup>↗</sup>](https://en.wikipedia.org/wiki/Parsing_expression_grammar).


<br>


## Syntax

| Pattern | Description | Examples |
| :------ | :---------- | :------- |
| `e1 \| e2` | `e1` *or* `e2`, with `e1` taking priority |
| `LITERAL` | `"literal"` or `"LITERAL"` |
| `(e.s)*` `(e.s)+` | Occurrences of `e`, *right*-separated by `s` (with the right-most separator optional) | `(expr.",")*` matches `expr`, `expr,`, `expr, expr`, `expr, expr,` |
| `(s.e)*` `(s.e)+` | Occurrences of `e`, *left*-separated by `s` (with the left-most separator optional) | `("\|".expr)*` matches `expr`, `\| expr`, `expr \| expr`, `\| expr \| expr`


<br>


## Spec

### Expressions
```coffee
expression -->
   expr
   | expr-part-apply
   | expr-call
```

### Assignments
```coffee
assignment --> "set" pattern "=" expression

pattern --> identifier | ("(" (identifier.",")* ")")

identifier --> new-shard | shard
new-shard --> " shard "
shard -->
   ("a"-"z" | "A"-"Z")
   ("a"-"z" | "A"-"Z" | "0"-"9" | "-" | "_")*
```

### Functions
```coffee
func-def -->
   (CREATE)? FUNC
      identifier
         func-def-prot-params
         (func-def-part-params)?
      func-def-body

func-def-prot-params --> "(" (func-def-prot-param.",")* ")"
func-def-prot-param  --> (type-hint)? identifier (",")?

func-def-part-params --> "[" ("|".func-def-part-param)* "]"
func-def-part-param  --> (type-hint)? identifier ("=" expr)?

func-def-body --> "{" body "}"


expr-part-apply --> expression func-part-apply
func-part-apply --> func-call-part-params

expr-call --> expression func-call
func-call -->
   func-call-prot-params
   (func-call-part-params)?
   (func-call-body)?

func-call-prot-params -->
     "(" (expr.",")* ")"
   | expr
func-call-part-params --> "[" ("|".func-def-part-param)* "]"
func-call-part-param --> (shard "=")? expr
func-call-body --> "{" body "}"
```

### Sectors
```coffee
section --> secator-open body secator-close
secator-open --> "<" shard ">"
secator-close --> "</" shard ">"
```
