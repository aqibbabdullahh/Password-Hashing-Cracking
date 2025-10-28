# Import the hashlib module, just like in our hasher script.
import hashlib

def hash_password(password):
    """
    Hashes a password using the SHA-256 algorithm.
    This function is a duplicate of the one in hasher.py to keep the cracker script self-contained.
    """
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()

def main():
    """
    Performs a dictionary attack to find a matching password for a given hash.
    """
    # This is the target hash. Replace the value below with the actual hash
    # you generated from your hasher.py script.
    target_hash = "ccf9ac1c9ce02b9bb7810a1fff51e474f37d98c3582f2d3b5036caf559afd9bc"

    # Specify the name of the password dictionary file.
    dictionary_file = "passwords.txt"

    print("Starting dictionary attack...")

    try:
        # Open and read the dictionary file.
        with open(dictionary_file, 'r') as f:
            for line in f:
                # Remove any leading/trailing whitespace (like the newline character).
                password_to_check = line.strip()

                # Hash the password from the dictionary.
                hashed_password_to_check = hash_password(password_to_check)

                # Compare the generated hash with our target hash.
                if hashed_password_to_check == target_hash:
                    print(f"\n[+] Password found!")
                    print(f"[*] Original Password: {password_to_check}")
                    print(f"[*] Hashed Password:   {hashed_password_to_check}")
                    # Exit the program after finding the password.
                    return

        # If the loop completes without finding a match.
        print("\n[-] Password not found in the dictionary.")

    except FileNotFoundError:
        print(f"Error: The file '{dictionary_file}' was not found.")

if __name__ == "__main__":
    main()