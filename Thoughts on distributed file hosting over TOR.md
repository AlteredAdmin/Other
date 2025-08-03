# ⚠️ Do not follow anything here this is just thoughts and some are probally wrong. ⚠️ 

Below is a tour of the most practical —and reasonably well‑maintained—ways to host or share files **through the Tor network**. I group them by how “distributed” they are, from fully peer‑to‑peer grids to single‑server onion services, and highlight what each is good (and not so good) at.

## 1 · Peer‑to‑peer tools for one‑off transfers

### OnionShare

* Launches an ephemeral web server on your machine and exposes it as a Tor v3 onion site; the recipient downloads directly from you without any third‑party store.
* Also supports “Receive” (drop‑box), static website hosting, and chat modes.
* Cross‑platform GUI and CLI; bundled with Tails, Qubes, Whonix. ([onionshare.org][1], [support.torproject.org][2])

### FilePizza (self‑hosted)

* Browser‑to‑browser WebRTC transfers; you can front the signalling server with an onion address so the initial rendezvous happens inside Tor.
* Fast for large files but both peers must stay online; metadata may leak unless you proxy STUN/TURN. ([file.pizza][3])

### Lufi

* Simple “encrypted‑drop” web app: files are AES‑GCM‑encrypted client‑side, then stored on the server for a configurable TTL.
* When you run Lufi as an onion service the server never sees the uploader’s IP **or** the plaintext. ([upload.disroot.org][4])

## 2 · Truly distributed storage grids

### Tahoe‑LAFS Onion Grid

* Erasure‑coded, provider‑independent storage; any set of *k* of *n* shares can reconstruct the data.
* Since v1.12 you can run introducer and storage nodes **only** over Tor, giving a grid whose participants are all hidden‑service endpoints. ([blog.torproject.org][5], [tahoe-lafs.readthedocs.io][6], [GitHub][7])

### IPFS over Tor

* IPFS is DHT‑based; wrapping transports with `torify` or the experimental **libp2p‑tor‑transport** works, but you must disable QUIC/AutoNAT to avoid leaks and many relays will reject large blocks—so expect slow pins. ([IPFS Forums][8])

### Arweave gateways as onion services

* Arweave data are immutable and replicated chain‑wide; running a gateway behind Tor makes the archive reachable even where Arweave.net is censored and masks operator location. ([DEV Community][9])

*(Storj, Sia and Filecoin nodes can also bind to Tor SOCKS5; performance drops sharply and many miners don’t relay Tor traffic, so they’re omitted here for brevity.)*

## 3 · Sync‑style “personal clouds” behind Tor

### Nextcloud

* Add a v3 onion `HiddenServicePort` in `torrc`, set `overwritehost` to the `.onion`, and you have a full web‑DAV/collab suite reachable only via Tor (or both Tor + clearnet with a reverse‑proxy rule). ([Nextcloud community][10])

### Syncthing

* No native Tor mode, but routing its discovery & relay traffic through Tor’s SOCKS5 proxy works; LAN discovery stays local. Performance is acceptable for small teams, but initial discovery can be flaky. ([Syncthing Community Forum][11])

## 4 · Whistle‑blower drop boxes

### SecureDrop

* Hardened two‑server architecture (source + journalist) accessible solely via Tor; files are PGP‑encrypted on upload, and sources get a random code‑name to return for replies.
* Widely deployed at major newsrooms and NGOs. ([docs.securedrop.org][12])

## 5 · Choosing the right option

| Scenario                                      | Good choice                                    | Why                                                |
| --------------------------------------------- | ---------------------------------------------- | -------------------------------------------------- |
| Send a friend a 4 GB video once               | **OnionShare**                                 | Direct, no server, link auto‑expires               |
| Keep password vault synced across laptops     | **Syncthing over Tor** (or Tahoe magic‑folder) | Continuous, versioned sync                         |
| Redundant, censorship‑resistant public mirror | **Tahoe‑LAFS Onion Grid** or **IPFS + Tor**    | Data survives node loss; self‑authenticating links |
| Anonymous tip‑line for journalists            | **SecureDrop**                                 | Audited threat model & two‑stage storage           |
| Permanent public archive immune to takedowns  | **Arweave gateway** behind Tor                 | Content is on‑chain; gateway access is hidden      |
| One‑click encrypted uploads for many users    | **Lufi** as an onion site                      | Server never sees keys; simple UX                  |

## 6 · Operational tips

* Prefer **v3 onion services**; v2 was deprecated in 2021.
* Run Tor in **IsolateSOCKSAuth** mode so each client/server circuit is distinct.
* Tor adds 100‑300 ms latency; use higher chunk sizes (e.g., Tahoe 10 MB) and parallel reads.
* Never expose the same service on clearnet and Tor without strict host headers—this leaks the hidden origin.
* For very large datasets (>10 GB) consider seeding via BitTorrent first, then pinning in IPFS/Tahoe to reduce initial relay strain.

---

**Bottom line:** if you only need quick, private transfers, OnionShare or Lufi are simplest. For long‑term, fault‑tolerant storage that keeps both the data **and** its hosts anonymous, Tahoe‑LAFS or Tor‑wrapped IPFS are the current front‑runners. SecureDrop, Nextcloud, and Syncthing fill niche workflow and collaboration needs once you place them behind an onion service.

[1]: https://onionshare.org/ "OnionShare"
[2]: https://support.torproject.org/misc/misc-12/?utm_source=chatgpt.com "How can I share files anonymously through Tor? | Tor Project | Support"
[3]: https://file.pizza/?utm_source=chatgpt.com "FilePizza • Your files, delivered."
[4]: https://upload.disroot.org/ "Lufi - Disroot file uploader"
[5]: https://blog.torproject.org/tor-heart-tahoe-lafs/ "Tor at the Heart: Tahoe-LAFS | The Tor Project"
[6]: https://tahoe-lafs.readthedocs.io/en/latest/anonymity-configuration.html?utm_source=chatgpt.com "Using Tahoe-LAFS with an anonymizing network: Tor, I2P"
[7]: https://github.com/david415/ansible-tahoe-lafs?utm_source=chatgpt.com "david415/ansible-tahoe-lafs - GitHub"
[8]: https://discuss.ipfs.tech/t/running-ipfs-under-tor/9071 "Running IPFS under Tor - IPFS Forums"
[9]: https://dev.to/fllstck/running-an-arweave-gateway-in-the-dark-web-262g "Running an Arweave Gateway in the Dark Web - DEV Community"
[10]: https://help.nextcloud.com/t/running-nextcloud-as-a-hidden-service-tor/25488 "Running Nextcloud as a hidden service (Tor) - ℹ️ Support - Nextcloud community"
[11]: https://forum.syncthing.net/t/syncthing-over-tor/23642 "Syncthing over Tor - Support - Syncthing Community Forum"
[12]: https://docs.securedrop.org/en/latest/source/how_to_submit.html "How To Submit — SecureDrop latest documentation"
