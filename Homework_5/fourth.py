import random

directions = ["up", "down", "left", "right"]
rewards = {
    "up": -1,
    "down": 1,
    "left": -2,
    "right": 2
}

q_table = {dir: 0 for dir in directions}
learning_rate = 0.1
episodes = 1000

# Q-learning simulation
for episode in range(episodes):
    action = random.choice(directions)  # choose a direction (exploration)
    reward = rewards[action]
    # Update Q-value (learn)
    q_table[action] += learning_rate * (reward - q_table[action])

# Check learned best direction
best_action = max(q_table, key=q_table.get)
print("Best direction to move based on learning:", best_action)
print("Q-values after learning:", q_table)

# Simulate 10 steps using learned knowledge
total_score = 0
for i in range(10):
    action = max(q_table, key=q_table.get)  # always choose best known direction
    reward = rewards[action]
    total_score += reward
    print(f"Step {i+1}: moved {action}, reward = {reward}")

print(f"Total score after 10 steps: {total_score}")
