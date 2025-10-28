# Import the hashlib module, which provides various hashing algorithms.
import hashlib

def hash_password(password):
    """
    Hashes a password using the SHA-256 algorithm and returns the hexadecimal digest.
    """
    # Create a new SHA-256 hash object.
    # SHA-256 is a widely used and secure hashing algorithm.
    sha256 = hashlib.sha256()

    # The update() method requires a bytes-like object, so we encode the string.
    # .encode('utf-8') converts the string into a sequence of bytes.
    sha256.update(password.encode('utf-8'))

    # .hexdigest() returns the hash as a hexadecimal string, which is the final output.
    return sha256.hexdigest()

if __name__ == "__main__":
    # This block will only run when the script is executed directly.
    # You can change the password below to test different inputs.
    plain_text_password = "MySecurePassword123"

    # Call the hashing function and store the result.
    hashed_password = hash_password(plain_text_password)

    # Print the original password and its hash.
    print(f"The original password is: {plain_text_password}")
    print(f"The hashed password is:   {hashed_password}")