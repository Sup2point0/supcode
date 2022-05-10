# General Functions

General-purpose inbuilt functions.


## Contents

- [`add`](#add)
- [`apply`](#apply)
- [`case`](#case)
- [`clear`](#clear)
- [`count`](#count)
- [`delete`](#delete)
- [`exit`](#exit)
- [`insert`](#insert)
- [`open`](#open)
- [`sort`](#sort)
- [`replace`](#replace)
- [`reverse`](#reverse)
- [`search`](#search)
- [`shuffle`](#shuffle)
- [`split`](#split)
- [`strip`](#strip)


## `case`

String casing.

```coffee
func case(str 'text') [
  | pool 'type' = {upper, lower, caps, title, caption, alternate, none}
]
```