# from hashlib import sha1 ,sha224,sha256,sha384,sha512,sha3_224,sha3_256,sha3_384,sha3_512,shake_128,shake_256 

# def hash_pass(hashed):
    
#     hashed = sha1(hashed.encode()).hexdigest()
#     hashed = sha224(hashed.encode()).hexdigest()
#     hashed = sha256(hashed.encode()).hexdigest()
#     hashed = sha384(hashed.encode()).hexdigest()
#     hashed = sha512(hashed.encode()).hexdigest()
#     hashed = sha3_224(hashed.encode()).hexdigest()
#     hashed = sha3_256(hashed.encode()).hexdigest()
#     hashed = sha3_384(hashed.encode()).hexdigest()
#     hashed = sha3_512(hashed.encode()).hexdigest()
#     hashed = shake_128(hashed.encode()).hexdigest(16)  
#     hashed = shake_256(hashed.encode()).hexdigest(32)  
    
#     return hashed


# def login(password):
    
#     user_logs = {
#         "a@gmail.com":"6eb7658cb142b914847327968c5c94f59148ebdfc25f879fb764c5c52c2d2e5aadf5fa8e7f000220743719539f4f6f58c99bb613f191ada06d978f198160aadc",
#         "b@gmail.com":"39588534a3a6adc1d56395c2bc7e826ea2fd9cb2841c62fd461ec116f0004e8a6afaf8447a343463aaf6304ae940bc79654ec2b223f54cdcf7a50223d492b9b2",
#         "c@gmail.com":"974bb9a37a44fe252623710a9eb0ab95c059360a4698c2ffd03073de8d1391238b5bb9ca86ca7223aa1dbeadfa02ed5d54676333c2279b5469b0d0a9b270f493"
#     }
    
#     return "Login Successful" if  hash_pass(password) == user_logs.items() else "Access Denied"
    


# # print(login("pass1"))
# print(hash_pass("1"))

from hashlib import (
    sha1, sha224, sha256, sha384, sha512, 
    sha3_224, sha3_256, sha3_384, sha3_512, 
    shake_128, shake_256
)

def hash_pass(data):
    """
    Hashes the given input using a series of SHA functions.
    The input is first converted to a bytes-like object if needed.
    """
    if not isinstance(data, bytes):
        data = str(data).encode()
    
    
    hashed = sha1(data).digest()
    hashed = sha224(hashed).digest()
    hashed = sha256(hashed).digest()
    hashed = sha384(hashed).digest()
    hashed = sha512(hashed).digest()
    hashed = sha3_224(hashed).digest()
    hashed = sha3_256(hashed).digest()
    hashed = sha3_384(hashed).digest()
    hashed = sha3_512(hashed).digest()
    hashed = shake_128(hashed).digest(16)  # <=
    hashed = shake_256(hashed).digest(32)  # "Shake" Requires a length parameter
    
    return hashed.hex()


# pass1 = "pass1"
# pass2 = "pass2"
# pass3 = "pass3"

# print([
# hash_pass(pass1),
# hash_pass(pass2),
# hash_pass(pass3)
# ])


# Define an array (list) of user dictionaries
users = [
    {   "name":"shahabuddin",
        "email": "shahab@gmail.com", 
        "hash": "6f460e11ff00f33ebb760f04c91ba73626a4aa200e6a90a234cb305acfe2d769"
    },
    {
        "name":"zahid",
        "email": "zahid@gmail.com", 
        "hash": "91eb28bfc919b8c125f1d41cbb5a9762b0ac54044b31a58e322a4c63a018a43f"
    },
    {
        "name":"abeera",
        "email": "abeera@gmail.com", 
        "hash": "f8b3759fd25bc68f879d1d77726c2610fec39c14c83c33804cbb55da1150477d"
    }
]

def login():
    # Ask the user for their email
    email = input("Enter your email: ").strip().lower()
    
    # Search for the user in the list
    user = next((u for u in users if u["email"] == email),None)
    
    if user:
        
        password = input(f"Welcome {user['name']}! please enter your password: ").strip().lower()
        
        if hash_pass(password) == user["hash"]:
            
            print("Login successful!")
        else:
            print("Login failed, incorrect password.")
    else:
        print(f"No user with found with this email : {email}")        
    
if __name__ == "__main__":
    login()
