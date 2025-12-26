# Hello Rust

A bare bones "Hello, World!" application written in Rust.

## Description

This is a minimal Rust application that prints "Hello, World!" to the console. It serves as a starting template for Rust development.

## Prerequisites

- [Rust](https://www.rust-lang.org/tools/install) (1.70 or later recommended)

To install Rust:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Verify installation:

```bash
rustc --version
cargo --version
```

## Project Structure

```
hello_rust/
├── Cargo.toml    # Project manifest (dependencies, metadata)
├── README.md     # This file
└── src/
    └── main.rs   # Application entry point
```

## How to Build

Navigate to the project directory and run:

```bash
cargo build
```

For an optimized release build:

```bash
cargo build --release
```

## How to Run

Development mode:

```bash
cargo run
```

Or run the compiled binary directly:

```bash
./target/debug/hello_rust      # Debug build
./target/release/hello_rust    # Release build
```

## Expected Output

```
Hello, World!
```

## Deployment

### Option 1: Compile and Distribute Binary

1. Build the release binary:
   ```bash
   cargo build --release
   ```

2. The executable is located at `./target/release/hello_rust`

3. Copy this binary to your target server or system. No Rust installation required on the target machine.

### Option 2: Cross-Compilation

To compile for a different target platform:

```bash
# Add target (example: Linux x86_64)
rustup target add x86_64-unknown-linux-gnu

# Build for target
cargo build --release --target x86_64-unknown-linux-gnu
```

### Option 3: Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM rust:1.75 as builder
WORKDIR /app
COPY . .
RUN cargo build --release

FROM debian:bookworm-slim
COPY --from=builder /app/target/release/hello_rust /usr/local/bin/
CMD ["hello_rust"]
```

Build and run:

```bash
docker build -t hello_rust .
docker run hello_rust
```

## License

MIT
