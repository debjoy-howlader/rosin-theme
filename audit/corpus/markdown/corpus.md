---
title: corpus
---
<!-- @ md.heading.mark function # -->
<!-- @ md.heading.text function Heading -->
# Heading

<!-- @ md.bold.text variable bold -->
<!-- @ md.italic.text variable italic -->
Some **bold** and *italic* text.

<!-- @ md.code.inline string inline -->
<!-- @ md.link.text variable link -->
<!-- @ md.link.url composite example -->
Use `inline` and a [link](https://example.com).

<!-- @ md.list.bullet keyword - -->
- list item

<!-- @ md.quote comment quoted -->
> quoted text

<!-- @ md.fence.lang comment c -->
```c
//@ md.fence.c.keyword keyword return
return 0;
```

```rust
//@ md.fence.rs.macro macro println
println!("x");
```

```python
#@ md.fence.py.builtin libfn print
print("x")
```

```bash
#@ md.fence.sh.var globalvar $PORT
echo $PORT
```

```toml
#@ md.fence.toml.key member name
name = "x"
```

<!-- @ md.h2 function H2 -->
## H2
### H3
#### H4
##### H5
###### H6

<!-- @ md.setext1 function Setext -->
Setext one
==========

Setext two
----------

<!-- @ md.escape escape \* -->
Escaped \* star and ~~struck~~ text.

<!-- @ md.numbered keyword 1. -->
1. numbered item

<!-- @ md.ref.link variable ref -->
A [ref link][ref] and an ![image](pic.png).

[ref]: https://example.com

<!-- @ md.html.tag prim b -->
Some <b>html</b> here.

    indented raw block

| Col | Val |
| --- | --- |
| a   | 1   |

```c {.numberLines}
int a;
```

```cpp
//@ md.fence.cpp.keyword keyword class
class A {};
```

```json
{ "k": 1 }
```

```yaml
#@ md.fence.yaml.key member key
key: value
```

```makefile
#@ md.fence.make.var globalvar CC
CC := gcc
```

```ini
[s]
k = v
```

```diff
-old
+new
```

```log
E (1) tag: msg
```

<!-- ---- pass 1b coverage additions ---- -->

<!-- @ md.image.alt variable alt -->
![alt][logo]

<!-- @ md.autolink composite https -->
Visit <https://example.com> or <me@example.com>.

<!-- @ md.ref.def variable logo -->
[logo]: https://example.com/logo.png "Logo"

***

```jsonc
{ "a": 1 // c
}
```
