""" #question 1
import hashlib, time
 
dataset = [
    "Cryptography and Network Security",
    "Cryptography and Network Security!",   # 1 char changed -> avalanche test
    "SIMATS Engineering Chennai",
    "192465064",
    "The quick brown fox jumps over the lazy dog"
]
 
def get_hash(algo, data):
    h = hashlib.new(algo)
    h.update(data.encode())
    return h.hexdigest()
 
def measure_performance(algo, data, rounds=100000):
    start = time.perf_counter()
    for _ in range(rounds):
        hashlib.new(algo, data.encode()).hexdigest()
    end = time.perf_counter()
    return end - start
 
print(f"{'Input':45} {'MD5 (128-bit)':35} {'SHA-256 (256-bit)'}")
print("-"*140)
for item in dataset:
    md5_h = get_hash('md5', item)
    sha_h = get_hash('sha256', item)
    print(f"{item[:42]:45} {md5_h:35} {sha_h}")
 
print("\nAvalanche effect check (1-bit/char change in input 1 vs 2):")
print("MD5   :", get_hash('md5', dataset[0]) != get_hash('md5', dataset[1]))
print("SHA256:", get_hash('sha256', dataset[0]) != get_hash('sha256', dataset[1]))
 
print("\nPerformance (100000 hash operations on a fixed 44-byte string):")
sample = dataset[4]
t_md5 = measure_performance('md5', sample)
t_sha = measure_performance('sha256', sample)
print(f"MD5    : {t_md5:.4f} sec  ->  {100000/t_md5:.0f} hashes/sec")
print(f"SHA-256: {t_sha:.4f} sec  ->  {100000/t_sha:.0f} hashes/sec")
  """
 
 
 
 
 
 
 
 
 
 


#question2 
import hashlib
 
def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()
 
# Step 1: create an original file
with open("document.txt", "w") as f:
    f.write("Confidential Report: Q1 financial summary shows a 12% growth in revenue.")
 
original_hash = sha256_of_file("document.txt")
print("Original file hash (SHA-256):", original_hash)
 
# Step 2: simulate tampering - change a single character
with open("document.txt", "r") as f:
    content = f.read()
tampered_content = content.replace("12%", "21%")   # attacker flips digits
with open("document.txt", "w") as f:
    f.write(tampered_content)
 
tampered_hash = sha256_of_file("document.txt")
print("Tampered file hash (SHA-256):", tampered_hash)
 
# Step 3: integrity verification
print("\nIntegrity check result:")
if original_hash == tampered_hash:
    print("File is INTACT - no tampering detected.")
else:
    print("TAMPERING DETECTED - hash values differ, file integrity compromised.")
 
# quantify how many hex characters changed
diff_chars = sum(1 for a, b in zip(original_hash, tampered_hash) if a != b)
print(f"Hex characters changed out of 64: {diff_chars} ({diff_chars/64*100:.1f}% of digest)")
 





 


#Question 3



""" from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
 
# ---- Step 1: Key generation (Sender's key pair) ----
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()
 
message = b"Transfer INR 50,000 to Account No. 1234567890 - authorized by Prabhas"
 
# ---- Step 2: Signing (done by sender using PRIVATE key) ----
signature = private_key.sign(
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)
print("Message           :", message.decode())
print("Signature (hex)   :", signature.hex()[:64], "...(truncated)")
print("Signature length  :", len(signature), "bytes")
 
# ---- Step 3: Verification (done by receiver using SENDER'S PUBLIC key) ----
def verify(pub_key, msg, sig):
    try:
        pub_key.verify(
            sig, msg,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False
 
print("\nCase 1 - Genuine message & signature:")
print("Verification result:", verify(public_key, message, signature))
 
print("\nCase 2 - Tampered message, original signature:")
tampered = b"Transfer INR 90,000 to Account No. 1234567890 - authorized by Prabhas"
print("Verification result:", verify(public_key, tampered, signature))
 
print("\nCase 3 - Genuine message, verified with a DIFFERENT public key (impersonation attempt):")
attacker_key = rsa.generate_private_key(public_exponent=65537, key_size=2048).public_key()
print("Verification result:", verify(attacker_key, message, signature))
 
 """


#question 4

""" import hashlib, time, os, random
 
# --- Simplified Kerberos simulation ---
# Entities: Client (C), Authentication Server (AS), Ticket Granting Server (TGS), Application Server (V)
# Secret keys shared out-of-band (in reality distributed at registration)
 
class KDC:
    def __init__(self):
        self.client_keys = {"prabhas": self._derive_key("client_password123")}
        self.tgs_key = self._derive_key("tgs_master_secret")
        self.service_key = self._derive_key("fileserver_master_secret")
        self.used_authenticators = set()   # replay-attack protection store
 
    def _derive_key(self, secret):
        return hashlib.sha256(secret.encode()).hexdigest()
 
    def _encrypt(self, key, plaintext):
        # XOR-based symmetric "encryption" for simulation purposes only
        k = key.encode()
        return bytes(b ^ k[i % len(k)] for i, b in enumerate(plaintext.encode())).hex()
 
    def _decrypt(self, key, ciphertext_hex):
        k = key.encode()
        data = bytes.fromhex(ciphertext_hex)
        return bytes(b ^ k[i % len(k)] for i, b in enumerate(data)).decode()
    # Step 1: AS issues Ticket Granting Ticket (TGT) after authenticating client
    def as_exchange(self, client_id):
        if client_id not in self.client_keys:
            return None
        client_key = self.client_keys[client_id]
        session_key_c_tgs = os.urandom(16).hex()
        tgt_plain = f"{client_id}|{session_key_c_tgs}|valid_until={time.time()+300}"
        tgt = self._encrypt(self.tgs_key, tgt_plain)   # TGT encrypted with TGS's key, client cannot read it
        client_msg = self._encrypt(client_key, session_key_c_tgs)  # session key sent to client
        print(f"[AS]  Issued TGT for '{client_id}', valid 300s")
        return tgt, client_msg, session_key_c_tgs
 
    # Step 2: TGS issues a Service Ticket after validating TGT + authenticator
    def tgs_exchange(self, tgt, authenticator, service_id="fileserver"):
        tgt_plain = self._decrypt(self.tgs_key, tgt)
        client_id, session_key_c_tgs, valid_until = tgt_plain.split("|")
        valid_until = float(valid_until.split("=")[1])
 
        if time.time() > valid_until:
            return None, "TGT expired"
 
        auth_plain = self._decrypt(session_key_c_tgs, authenticator)
        auth_client, timestamp = auth_plain.split("|")
        timestamp = float(timestamp)
 
        # Replay attack protection: reject stale or reused authenticators
        if authenticator in self.used_authenticators:
            return None, "REPLAY DETECTED - authenticator already used"
        if abs(time.time() - timestamp) > 120:
            return None, "Authenticator timestamp outside allowed clock-skew window"
        if auth_client != client_id:
            return None, "Client mismatch between TGT and authenticator"
 
        self.used_authenticators.add(authenticator)   # mark as consumed
 
        session_key_c_v = os.urandom(16).hex()
        st_plain = f"{client_id}|{session_key_c_v}|valid_until={time.time()+120}"
        service_ticket = self._encrypt(self.service_key, st_plain)
        client_msg = self._encrypt(session_key_c_tgs, session_key_c_v)
        print(f"[TGS] Issued Service Ticket for '{client_id}' -> '{service_id}', valid 120s")
        return (service_ticket, client_msg), None
 
    def verify_service_request(self, service_ticket, service_authenticator):
        st_plain = self._decrypt(self.service_key, service_ticket)
        client_id, session_key_c_v, valid_until = st_plain.split("|")
        valid_until = float(valid_until.split("=")[1])
        if time.time() > valid_until:
            return False, "Service ticket expired"
        auth_plain = self._decrypt(session_key_c_v, service_authenticator)
        auth_client, ts = auth_plain.split("|")
        if auth_client != client_id:
            return False, "Client identity mismatch"
        return True, f"Access GRANTED to '{client_id}'"
 
 
kdc = KDC()
 
# ----- Normal successful flow -----
print("=== Normal Authentication Flow ===")
tgt, enc_session_key, session_key_c_tgs = kdc.as_exchange("prabhas")
 
authenticator_plain = f"prabhas|{time.time()}"
authenticator = kdc._encrypt(session_key_c_tgs, authenticator_plain)
 
(service_ticket, enc_session_key_v), err = kdc.tgs_exchange(tgt, authenticator)
print("TGS result:", err if err else "Service ticket issued successfully")
 
session_key_c_v = kdc._decrypt(session_key_c_tgs, enc_session_key_v)
service_auth = kdc._encrypt(session_key_c_v, f"prabhas|{time.time()}")
ok, msg = kdc.verify_service_request(service_ticket, service_auth)
print("Application Server:", msg)
 
# ----- Replay attack simulation -----
print("\n=== Replay Attack Simulation (attacker resends the SAME authenticator) ===")
(replayed_result, err2) = kdc.tgs_exchange(tgt, authenticator)   # reuse same authenticator
print("TGS result:", err2 if err2 else "Service ticket issued (SHOULD NOT HAPPEN)")
  """


#question 5

""" import datetime
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
 
# ---- Step 1: Generate a self-signed X.509 certificate (acts as sample input) ----
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "IN"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Tamil Nadu"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "SIMATS Engineering"),
    x509.NameAttribute(NameOID.COMMON_NAME, "simats-cyberlab.edu.in"),
])
 
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.datetime.utcnow())
    .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
    .add_extension(x509.SubjectAlternativeName([x509.DNSName("simats-cyberlab.edu.in")]), critical=False)
    .sign(key, hashes.SHA256())
)
 
with open("sample_cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))
 
# ---- Step 2: Parse and validate the certificate ----
with open("sample_cert.pem", "rb") as f:
    loaded_cert = x509.load_pem_x509_certificate(f.read())
 
print("=== X.509 Certificate Fields ===")
print("Subject         :", loaded_cert.subject.rfc4514_string())
print("Issuer          :", loaded_cert.issuer.rfc4514_string())
print("Serial Number   :", loaded_cert.serial_number)
print("Not Valid Before:", loaded_cert.not_valid_before_utc)
print("Not Valid After :", loaded_cert.not_valid_after_utc)
print("Signature Algo  :", loaded_cert.signature_algorithm_oid._name)
pub = loaded_cert.public_key()
print("Public Key Type :", type(pub).__name__, f"({pub.key_size}-bit)")
 
print("\n=== Validation Checks ===")
now = datetime.datetime.now(datetime.timezone.utc)
 
# Check 1: Validity period
is_time_valid = loaded_cert.not_valid_before_utc <= now <= loaded_cert.not_valid_after_utc
print("1. Within validity period       :", is_time_valid)
 
# Check 2: Self-signed check (issuer == subject)
is_self_signed = loaded_cert.issuer == loaded_cert.subject
print("2. Self-signed (issuer==subject):", is_self_signed)
 
# Check 3: Signature verification (issuer's public key verifies the cert signature)
from cryptography.hazmat.primitives.asymmetric import padding as asympad
try:
    pub.verify(
        loaded_cert.signature,
        loaded_cert.tbs_certificate_bytes,
        asympad.PKCS1v15(),
        loaded_cert.signature_hash_algorithm,
    )
    sig_valid = True
except Exception:
    sig_valid = False
print("3. Signature cryptographically valid:", sig_valid)
 
trust_verdict = "TRUSTED (self-signed, valid signature, within validity window)" \
    if (is_time_valid and sig_valid) else "NOT TRUSTED"
print("\nOverall trust verdict:", trust_verdict)
print("Note: A self-signed certificate is only trusted if explicitly added to a trust")
print("store; in a real PKI it would instead chain to a trusted root CA.")
  """