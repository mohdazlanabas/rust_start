use std::io::{self, Write};

fn main() {
    println!("=== Interactive Input Loop ===");
    println!("Type anything and I'll echo it back.");
    println!("Type 'exit' to quit.\n");

    loop {
        // Prompt
        print!("> ");
        io::stdout().flush().unwrap(); // Ensure prompt displays before input

        // Read input
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Failed to read input");

        // Trim whitespace/newline
        let input = input.trim();

        // Check for exit
        if input.eq_ignore_ascii_case("exit") {
            println!("Goodbye, Roger! 👋");
            break;
        }

        // Echo back
        println!("You said: {}\n", input);
    }
}
