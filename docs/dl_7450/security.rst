.. _dl_7450_security:

Security
========

Synaptics has a long history of creating secure products, from Fingerprint
Sensors to Video Content Protection (HDCP etc). Employees have regular training
on security awareness. Synaptics is an active member of several industry groups:

  * `The FIDO Alliance <https://fidoalliance.org/>`_
  * `Internet of Things Security Foundation (IoTSF) Founder Members <https://iotsecurityfoundation.org/>`_
  * `Digital Content Protections (DCP) <https://www.digital-cp.com/>`_ adopters

Synaptics follows `Best Practice Security Vulnerability Management <https://www.synaptics.com/vulnerability-disclosure-policy>`_ 
and has a *Product Security Incident Response Team* (PSIRT). We are an official `*CVE Numbering Authority* <https://www.cve.org/ProgramOrganization/CNAs>`_ (CNA).

**DL-7450 Security**

Synaptics takes a standardized approach to Security. The DL-7450 has a secure
boot processor, and hardware accelerator for cryptography functions (e.g.
AES128/256). It also has locked *One Time Programmable (OTP) Elements*
provisioned in the silicon factory. The OTP elements are hardened against
physical silicon attack. The chis has secure CPU functionality with anti-side
channel attack protection built in. The boot processor and OTP provides a
secure zone for cryptographic functions.


The DL-7450 has a small trusted computing base. The primary boot code is stored
in ROM and is therefore immutable. It is heavily reviewed and validated, thus
reducing the surface area for attacks. The primary bootloader cryptographically
validates all other code. The primary boot code is deliberately small with low
complexity and manages the cryptographic primitives. More complex security
algorithms are in later layers and based on the primitives and is updatable in
case vulnerabilities are discovered. This provides the DL-7450 with a *root of
trust* (RoT). Secure assets, such as cryptographic keys, are stored in a secure
OTP Vault. All critical data is encrypted, and has mitigations against single
bit error attacks. The OTP vault is hardened against silicon level attacks. The
key types stored in OTP are

 * Application code signatures
 * Digital content Protection keys and certificates
 * Unique Serial Number
 * Silicon type identifier

The on-chip Security processor is isolated from other processors, hardened
against fault attacks, hardened against side channel scanning and linked to a
hardware AES 128/256 accelerator. This makes it *Post Quantum Cryptography*
(PQC) prepared/ resistant.

The hardware-based root of trust ensures that the DL-7450 and its identity cannot
be separated, thus preventing device forgery or spoofing. Each DL-7450 is
identified by an unforgeable cryptographic key. Keys and other assets are
provisioned at manufacture time and stored in the encrypted and hardened OTP vault.
The keys are generated and protected by our security signing release hardware.
This ensures a tamper-resistant, secured hardware root of trust from factory to
end user.

DL-7450 cryptography is based on Industry standard algorithms. It has a
built-in cryptographic core with AES 128/256 accelerator and programmable
modes. Primary security is through AES-CCM (Counter with CBC-MAC). This is a
mode approved by `NIST Cybersecurity Framework
<https://www.nist.gov/cyberframework>`_, and is suited to managing integrity of
controlled/fixed systems such as DL-7450. Security Best Practice recommends
that bulk ciphers are now expected to be an AEAD or *Authenticated Encryption
with Associated Data algorithm*, meaning that it can not only encrypt the data
but also authenticate it. The AES-CCM conforms to this requirement.

Defense-in-depth provides for multiple layers of security and thus multiple
mitigations against each threat. Each stage of the boot and application process
is protected by the previous stage. Successive Stages cannot run unless
validated. All Components are protected using industry approved cryptographic
algorithms (e.g. NIST). Once a secure system is running, then only signed
encrypted modules can be further loaded.


**Internet-of-Things (IoT) Security**
The DL-7450 can be purposed as an IoT device. For example, it could be
registered in a cloud IoT connectivity provider such as `Azure IoT Hub
<https://azure.microsoft.com/en-gb/products/iot-hub/>`_. The DL-7450 uses the
latest security protocols e.g. TLS1.3, as we control. We can leverage our
hardware root-of-trust and cryptographic enginers to provide industry-standard
client certificates and support client verifcation during *Transport Layer
Security* (TLS) handshakes. Partner application payloads can be encrypted using
the most secure cipher suits, such as `Elliptic Curve Diffie-Hellman <https://csrc.nist.gov/projects/elliptic-curve-cryptography>`_ for
*perfect forward secrecy* (PFS), in order to keep data confidential and
maintain its integrity. We can also leverage the hardware root of trust in the
DL-7450 to store immutable security credentials, and manage the data payload -
this allows the communication engine and the IoT Cloud/client data collection
to be separated but still secure.

The device software is automatically updated if required, both to add features
and to correct known vulnerabilities or security breaches. These updates
require no intervention from the product manufacturer or the end user. The
updates are managed though Microsoft Windows Update.

Errors in device software or hardware are typical in emerging security attacks.
Runtime telemetry is stored in an encrypted log file and may be used for remote
diagnostics. The DL-7450 SDK for application developers can offer the option to
retrieve telemetry for real time analysis and mitigation.


**Secure Software Development process and Life Cycle**

Synaptics follows audited security processes for managing key assets:

  * Secure Signing machine processes
     * Certicom (for OTP)
     * Air-Gapped Hardware Signing Machines (HSMs) for Secure firmware updates
  * Code Quality tools (used on check-in and build)
     * Code scanning for consistency/adherence to code guidelines
     * Code Scanning for security vulnerabilities in third-party libraries
     * The DL-7450 has an associated risk analysis and risk registers for security
  * Regular release processes
     * formalized release checklists and signing (including security checks)
     * External libraries (SBoM - Software Bill of Materials) are managed and updated if necessary
  * Encrypted/Signed and authenticated code for in-field updates

