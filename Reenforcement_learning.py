import numpy as np
import random

position = 5  # Positions 0 to 4
actions = 2   # 0: Left, 1: Right
sequence = [1, 0, 1]  # Required sequence: Right, Left, Right
sequence_step = 0  # Start at first step in sequence

# Q-table: positions x sequence steps x actions
Q = np.zeros((position, len(sequence) + 1, actions))

episodes = 1000
learning_rate = 0.8
gamma = 0.9
epsilon = 0.3

for episode in range(episodes):
    state = 0  # Start at position 0 every episode
    sequence_step = 0  # Start sequence from step 0

    while True:
        # Choose action (epsilon-greedy)
        if random.uniform(0,1) < epsilon:
            action = random.randint(0, actions - 1)
        else:
            action = np.argmax(Q[state, sequence_step])

        # Move left or right but stay in bounds
        if action == 0:
            next_state = max(0, state - 1)
        else:
            next_state = min(position - 1, state + 1)

        # Check if action matches expected sequence step
        if action == sequence[sequence_step]:
            reward = 10  # Correct action
            next_sequence_step = sequence_step + 1
        else:
            reward = -5  # Wrong action
            next_sequence_step = sequence_step

        # End episode if sequence complete or reached goal
        done = next_sequence_step == len(sequence) or next_state == position - 1

        # Q-learning update
        old_value = Q[state, sequence_step, action]
        next_max = np.max(Q[next_state, next_sequence_step])
        Q[state, sequence_step, action] = old_value + learning_rate * (reward + gamma * next_max - old_value)

        state = next_state
        sequence_step = next_sequence_step

        if done:
            break

# Test learned policy
state = 0
sequence_step = 0
steps = 0
print("Agent path:")

while sequence_step < len(sequence) and steps < 20:
    action = np.argmax(Q[state, sequence_step])
    move = "Left" if action == 0 else "Right"

    if action == 0:
        next_state = max(0, state - 1)
    else:
        next_state = min(position - 1, state + 1)

    print(f"Step {steps}: Position {state} -> Action {move} -> Next Position {next_state}")

    if action == sequence[sequence_step]:
        sequence_step += 1

    state = next_state
    steps += 1

if sequence_step == len(sequence):
    print(f"Sequence completed in {steps} steps!")
else:
    print("Failed to complete sequence.")
