import g4f
import time
import sys
import random

def ask_gpt(messages: list) -> str:
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo,
        messages=messages
    )
    print(response)
    return response

my_list = [
"Understanding ROS Architect",
"Working with Topics: Managi",
"Services and Actions: Under",
"ROS Communication Patterns:",
"ROS APIs and Libraries: Fam",
"ROS Navigation Stack: Deep ",
"ROS Perception: Working wit",
"ROS Control: Implementing c",
"ROS Tools and Utilities: Pr",
"ROS Security: Ensuring the ",
"ROS Networking: Handling ne",
"ROS Hardware Integration: I",
"ROS Testing and Debugging: ",
"ROS Performance Optimizatio",
"ROS Multi-Robot Systems: De",
"ROS Simulation: Using simul",
"ROS Mobile Robots: Special ",
"ROS Industrial Applications",
"ROS Education and Training:",
"ROS Community Engagement: P",
"ROS tf transform",
"SLAM compibe with navigation stack",
"ROS Realsense",
"ROS Kalman filer",
"ROS with deep learning"
]

random_integer = random.randint(0, len(my_list)-1)
print(my_list[random_integer])

messages = []

# Open the comment if comment is needed
content = "Write only a script with no comment from chat. Write the start ```python without any `Sure! Here's an example of a...`"
messages.append({"role": "system", "content": content})
print("Start the assistant")
try:
        question = f"some ros noetic complicated scripts in python. For example: {my_list[random_integer]}"
        messages.append({'role': "user", "content": question})
        answer = ask_gpt(messages=messages)
        with open(f"D:\\Coding_AI\\test\\tes2{random_integer}.py", "w") as file:
             file.write(answer)
except KeyboardInterrupt:
   print("Exiting the program")