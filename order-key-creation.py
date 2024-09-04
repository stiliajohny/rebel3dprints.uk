import random
import string
import hashlib

def generate_segment(length=4):
    """Generate a random alphanumeric segment of specified length."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def calculate_checksum(key_without_checksum):
    """Calculate a 4-character checksum based on the first three segments."""
    # Use SHA-256 to create a hash from the key_without_checksum
    hash_object = hashlib.sha256(key_without_checksum.encode())
    # Convert the hash to a hex string and take the first 4 characters as the checksum
    checksum = hash_object.hexdigest()[:4].upper()  # Take the first 4 characters in uppercase
    return checksum

def generate_cd_key():
    """Generate a CD key in the format XXXX-YYYY-ZZZZ-WWWW with the last segment as the checksum."""
    # Generate three random alphanumeric segments
    segment1 = generate_segment()
    segment2 = generate_segment()
    segment3 = generate_segment()
    
    # Concatenate the first three segments without hyphens for checksum calculation
    key_without_checksum = segment1 + segment2 + segment3
    
    # Calculate the checksum based on the first three segments
    checksum = calculate_checksum(key_without_checksum)
    
    # Return the full CD key in the format XXXX-YYYY-ZZZZ-WWWW
    return f"{segment1}-{segment2}-{segment3}-{checksum}"

def generate_multiple_cd_keys(count=10):
    """Generate a list of CD keys."""
    return [generate_cd_key() for _ in range(count)]

# Example: Generate and display 10 CD keys
if __name__ == "__main__":
    cd_keys = generate_multiple_cd_keys(10)
    for key in cd_keys:
        print(key)
