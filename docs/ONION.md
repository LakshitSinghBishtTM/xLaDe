# Onion Service

This project provides an official Tor onion service:

http://xladeajfgkh32qgq5sj2mtmho3te5pivto7lav44dsbov6uduciz6hqd.onion

This serves as the **official project website**.

---

## Why an Onion Service?

The onion service is part of the project's commitment to availability, integrity, and minimizing trust assumptions.

### 1. Censorship Resistance

Access to source code and research infrastructure should not depend on geographic or platform-level restrictions. The onion service provides a reliable access path in environments where traditional hosting platforms may be blocked.

### 2. Self-Authenticating Identity

Onion addresses are derived from cryptographic keys. This means the address itself acts as a form of identity, reducing reliance on external certificate authorities and DNS infrastructure.

### 3. Availability by Design

The project intentionally uses an onion service as its primary website to reduce reliance on:

* centralized DNS infrastructure
* certificate authorities
* single hosting providers

### 4. Privacy by Design

Users can access the project without exposing identifying metadata such as IP addresses. This is particularly relevant for users in restrictive or monitored environments.

---

## Trust Model

The onion service is considered the **official web presence** of this project.

To verify authenticity:

* The onion URL is published in this repository
* It should match references in other official project materials
* Any changes to the onion address will be announced through the primary repository

Please do not trust onion links from third-party sources.

---

## Threat Model

The onion service helps mitigate:

* DNS tampering and hijacking
* TLS certificate authority compromise
* Platform-level censorship

It does not protect against:

* Malicious code within the repository
* Compromised development environments
* Supply chain attacks in dependencies

Users are still responsible for verifying the integrity of the code they run.

---

## Accessing the Onion Service

To access the onion site:

1. Install the Tor Browser: https://www.torproject.org/
2. Open the onion URL listed above

Note: Kindly download Tor from official channels only!

---

## Philosophy

This project does not assume that any single platform is permanently available or inherently trustworthy.

The onion service is used as a **first-class interface to the project**, not merely as a fallback, reflecting a design choice to reduce reliance on centralized infrastructure.