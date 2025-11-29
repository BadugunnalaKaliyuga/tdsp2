
import hashlib

key = "03787449"
blob = "8b1f4c3a2d"

combined_string = key + blob
sha256_hash = hashlib.sha256(combined_string.encode()).hexdigest()

answer = sha256_hash[:12]

print(f"Combined string: {combined_string}")
print(f"SHA256 hash: {sha256_hash}")
print(f"Answer (first 12 hex chars): {answer}")
