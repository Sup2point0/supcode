# `stadex`

An ixtension for interacting with the *stage*, an inbuilt environment for creating and manipulating sprites, to create anything imaginable, but games in particular.

## Subextensions

### `sensyx`
Sensing and interactivity.

### `geometryx`
Geometry and positioning.

### `graphyx`
Visuals and effects.

### `tracyx`
Pen rendering.

## Intrinsics

### `stadux`
Stadex-related errors.

## Specimen

```
active stadex

stadex.open(stage)[size = sys.inv.size(max)]

create stadex.sprite('portal') [
  | source = sys.file('portal.svg')
] {
  set sprite.x = 0
  set sprite.y = 0
  set sprite.dir = 90

  define portal.'spin'() {
    ...
  }
}
```
