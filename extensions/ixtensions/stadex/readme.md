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

```coffee
active stadex

stadex.open(stage)[size = sys.inv.size(max)]

create stadex.sprite('portal') [
  | source = sys.file('portal.svg')
] {
  set portal.x = 0
  set portal.y = 0
  set portal.dir = 90

  define portal.'spin'(speed) {
    alt portal.dir + speed
  }

  define portal.'orbit'(size = 200 or void, speed) {
    alt portal.x + ((size * sin(sys.timer) - portal.x) * 2) / (speed * 2)
    alt portal.y + ((size * cos(sys.timer) - portal.y) * 2) / (speed * 2)
  }
}
```
