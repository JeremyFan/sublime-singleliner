# Sublime-SingleLiner

Sometimes I want a single line Object when writting JavaScript.

But JS Formatter always try to unfold Objects.

So I need SingleLiner.

## Install
Open sublime, go to `Preferences -> Browse packages...`, and download `singleliner` to this directory:

```
git clone git@github.com:JeremyFan/sublime-singleliner.git
```

## Config
Go to `Preferences -> Key Bindings`, and config a shortcut you like, for example `ctrl + shift + s`:

```
{
  "keys": ["ctrl+shift+s"],
  "command": "single_line"
}
```

## Using

### Define an object
```
const obj = {
  foo,
  bar: 123
}
```
then:
```
const obj = { foo, bar: 123 }
```

### When use destructuring assignment
```
const {
  code,
  data
} = response
```
then:
```
const { code, data } = response
```

### Also works for nested Object
```
const obj = {
  foo: 123,
  bar
  baz: { qux }
}
```
then:
```
const obj = { foo: 123, barbaz: { qux } }
```

Much beautiful and clear, isn't it?