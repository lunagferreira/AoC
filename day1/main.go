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

	position := startPos // Current position of the dial

	countEndAtZero := 0   // Part 1: count how many times we end a rotation at 0
	countClickAtZero := 0 // Part 2: count how many clicks land on 0 during all rotations

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

		steps := dist // Total number of clicks for this rotation

		// Part 2: count clicks that land on 0
		clicksAtZero := zerosDuringRotation(position, steps, dir)
		countClickAtZero += clicksAtZero

		// Update final position after this rotation
		switch dir {
		case 'L':
			// Only need dist modulo numNumbers for final position
			d := steps % numNumbers                // Ensure distance is within bounds
			position = (position - d) % numNumbers // Update position
			if position < 0 {
				position += numNumbers // Wrap around if negative
			}
		case 'R':
			d := steps % numNumbers                // Ensure distance is within bounds
			position = (position + d) % numNumbers // Update position
		default:
			log.Fatalf("Invalid direction %q in line %q", string(dir), line)
		}

		// Part 1: check if final position is 0
		if position == 0 {
			countEndAtZero++ // Increment counter if we land on 0
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatalf("Error reading input: %v", err)
	}

	fmt.Println("Part 1: ", countEndAtZero)
	fmt.Println("Part 2: ", countClickAtZero)
}

// Calculates how many times the dial lands on 0
func zerosDuringRotation(position, steps int, dir byte) int {
	if steps <= 0 {
		return 0
	}

	var k0 int // Number of clicks until we first hit 0

	switch dir {
	case 'R':
		// From position p, going right, we need (100 - p) clicks to reach 0
		k0 = (numNumbers - (position % numNumbers)) % numNumbers
		if k0 == 0 {
			// If position == 0, we need a full turn (100 clicks) to see 0 again
			k0 = numNumbers
		}
	case 'L':
		// From position p, going left, we need p clicks to reach 0
		k0 = position % numNumbers
		if k0 == 0 {
			// If position == 0, we need a full turn to see 0 again
			k0 = numNumbers
		}
	default:
		log.Fatalf("Invalid direction %q", string(dir))
	}

	if steps < k0 {
		return 0 // We don't reach 0 at all in this rotation
	}

	return 1 + (steps-k0)/numNumbers // We hit 0 at click k0, then every 100 clicks after that
}
