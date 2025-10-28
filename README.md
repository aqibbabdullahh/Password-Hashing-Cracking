Password Hashing and Dictionary Attack
This project demonstrates the fundamental cybersecurity principles of secure password storage and a common attack vector used to compromise them. It includes a script to securely hash a password and a second script that simulates a dictionary attack to find the original password from its hash.

Project Objective
The primary goal of this project is to provide a hands-on, practical example of how secure password hashing works and why robust password practices are critical. By creating a working "cracker" tool, this project highlights the real-world vulnerabilities that can arise from weak passwords.

Getting Started
Prerequisites
You only need Python 3 installed on your system to run this project.

How to Run
Clone the Repository

git clone https://github.com/aqibbabdullahh/Password-Hashing-Cracking.git

cd Password-Hashing-Cracking

Generate a Hashed Password
First, run the hasher.py script to get a securely hashed password. You can modify the plain_text_password variable inside the script to test a different password.

python hasher.py

Perform the Dictionary Attack
Update the target_hash variable in cracker.py with the hash you generated in the previous step. Then, run the cracker.py script.

python cracker.py

The script will iterate through the passwords.txt file and attempt to find a match for the target hash.

What I Learned
One-Way Functions: This project provided a practical understanding of cryptographic hash functions (specifically, SHA-256) and their one-way nature.

Dictionary Attacks: I gained hands-on experience with how a dictionary attack works, highlighting its effectiveness against common or easily guessable passwords.

Password Security: This project reinforced the critical importance of using unique, complex passwords for every account to prevent them from being compromised by simple, automated attacks.

Salting: As a next step, I will explore the concept of "salting" to make dictionary and rainbow table attacks significantly harder.

Connect with Me

LinkedIn: https://www.linkedin.com/in/aqibabdullah/


