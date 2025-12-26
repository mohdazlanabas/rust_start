# Input Loop

Simple interactive CLI app demonstrating Rust's stdin/stdout handling with a loop pattern.

## What It Does

1. Prompts user for input (`>`)
2. Prints back what you typed
3. Repeats until you type `exit`

## Key Concepts Demonstrated

- **`std::io`** - Standard input/output handling
- **`loop`** - Infinite loop with `break` exit condition
- **`String::new()`** - Mutable string buffer for input
- **`trim()`** - Removes whitespace/newlines from input
- **`eq_ignore_ascii_case()`** - Case-insensitive string comparison
- **`flush()`** - Forces prompt to display before blocking on input

## Run It

```bash
cargo run
```

## Sample Session

```
=== Interactive Input Loop ===
Type anything and I'll echo it back.
Type 'exit' to quit.

> Hello Rust
You said: Hello Rust

> Testing 123
You said: Testing 123

> exit
Goodbye, Roger! 👋
```

## Project Structure

```
input_loop/
├── Cargo.toml
├── README.md
└── src/
    └── main.rs
```
