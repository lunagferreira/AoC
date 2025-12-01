package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

const (
	startPos   = 50
	numNumbers = 100 // 0..99
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatalf("Could not open input file: %v", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file) // Create a scanner to read the file line by line

	position := startPos // Starting position
	countZero := 0       // Counter for how many times we land on 0

	for scanner.Scan() {
		line := scanner.Text() // Read the current line
		if line == "" {
			continue // Skip empty lines
		}

		dir := line[0]                     // First character is direction 'L' or 'R'
		distStr := line[1:]                // Rest is the distance
		dist, err := strconv.Atoi(distStr) // Convert distance to integer
		if err != nil {
			log.Fatalf("Invalid distance %q in line %q: %v", distStr, line, err)
		}

		switch dir {
		case 'L':
			dist = dist % numNumbers                  // Ensure distance is within bounds
			position = (position - dist) % numNumbers // Update position
			if position < 0 {
				position += numNumbers // Wrap around if negative
			}
		case 'R':
			dist = dist % numNumbers                  // Ensure distance is within bounds
			position = (position + dist) % numNumbers // Update position
		default:
			log.Fatalf("Invalid direction %q in line %q", string(dir), line)
		}

		if position == 0 {
			countZero++ // Increment counter if we land on 0
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatalf("Error reading input: %v", err)
	}

	fmt.Println(countZero)
}
