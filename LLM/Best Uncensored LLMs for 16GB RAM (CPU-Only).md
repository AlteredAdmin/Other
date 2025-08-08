Below are solid **uncensored / lightly‑aligned** picks that run **CPU‑only on 16 GB RAM**. I note a recommended **quant** and the **Max RAM** the file needs (no GPU offload). Speeds on CPU vary a lot with memory bandwidth, but expect \~2–12 tok/s for 7–8B and \~2–5 tok/s for 13B on typical desktop CPUs. ([GitHub][1], [Reddit][2], [Level1Techs Forums][3], [Reddit][4])

### Best general chat (7–8B: safest for 16 GB)

* **Dolphin 2.9 – Llama‑3‑8B (uncensored)** — very popular “de‑aligned” chat model; good all‑rounder.
  **Use:** `Q4_K_M` (4.92 GB) or `Q5_K_M` (5.73 GB). Available in Ollama. ([Hugging Face][5], [Hugging Face][6], [Hugging Face][7], [Ollama][8])

* **OpenHermes 2.5 – Mistral‑7B** — chatty and capable; easy RAM headroom.
  **Use:** `Q4_K_M` (Max RAM \~6.87 GB) or `Q5_K_M` (\~7.63 GB). ([Hugging Face][9])

* **Zephyr‑7B‑Beta (Mistral fine‑tune)** — trained with reduced alignment; strong MT‑Bench for a 7B, but “likely to generate problematic text,” i.e., permissive.
  **Use:** `Q4_K_M` (Max RAM \~6.87 GB) or `Q5_K_M` (\~7.63 GB). ([Hugging Face][10])

### If you mainly want RP / creative freedom

* **MythoMax‑L2 13B** — long‑standing RP favorite; will fit, but responses will be slower and you’ll want modest context lengths.
  **Use:** `Q4_K_M` (file 7.87 GB; Max RAM \~10.37 GB) or `Q5_K_M` (9.23 GB; Max RAM \~11.73 GB). Users report \~2.5–5 tok/s on modern desktop CPUs. ([Hugging Face][11], [Reddit][4])

* **Pygmalion 2 7B** (or **Mistral‑Pygmalion 7B**) — purpose‑built for RP with custom tokens; lighter and faster than 13B.
  **Use:** `Q4_K_M` (file 4.08 GB; Max RAM \~6.58 GB) or `Q5_K_M` (4.78 GB; Max RAM \~7.28 GB). ([Hugging Face][12], [Hugging Face][13])

### Other community‑fav uncensored 7B options

* **Nous‑Hermes Llama‑2 7B (uncensored variants)** — still decent and very light. TheBloke page lists RAM for each quant. ([Hugging Face][14])
* **OpenChat 3.5 7B** — generally permissive and strong for reasoning among 7Bs. GGUF builds available. ([OpenCSG][15])

---

## What fits best on 16 GB RAM (CPU‑only)

* **Target 7–8B, Q4\_K\_M or Q5\_K\_M.** These give good quality with **\~5–8 GB RAM** footprint, leaving room for KV cache and the OS. ([Hugging Face][9], [Hugging Face][10])
* **13B works but is tight.** MythoMax 13B **Q4\_K\_M needs \~10.4 GB RAM** just to load; higher context windows add a few more GB for KV cache, so keep context to \~2–4k on 16 GB. ([Hugging Face][11], [GitHub][1])
* **Rule of thumb:** 7B models need roughly 8 GB RAM; 13B about 16 GB when unquantized — quantization cuts that a lot, but you still want headroom. ([GitHub][16], [GitLab][17])
* **Prefer K‑quants on CPU.** The newer **IQ** (imatrix) quants shine on GPUs; on CPU they’re typically **slower** than K‑quants at the same quality. ([Hugging Face][18])
* **Throughput depends on memory bandwidth.** Community tests show CPU tok/s scales with memory channels; e.g., \~11 tok/s for 7B on a Ryzen 5700G; 13B around 2–5 tok/s on desktop CPUs. ([GitHub][1], [Level1Techs Forums][3], [Reddit][4])

---

## Suggested quick picks

* **I want the strongest uncensored small model:** *Dolphin 2.9 Llama‑3‑8B Q5\_K\_M*. ([Hugging Face][5], [Hugging Face][7])
* **I want fast, friendly chat on CPU:** *OpenHermes 2.5 Mistral‑7B Q4\_K\_M*. ([Hugging Face][9])
* **I want RP/storytelling:** *MythoMax‑L2 13B Q4\_K\_M* (accept slower speed), or *Pygmalion 2 7B Q5\_K\_M* for speed. ([Hugging Face][11], [Hugging Face][12])
* **I want a helpful but very permissive assistant:** *Zephyr‑7B‑Beta Q5\_K\_M*. ([Hugging Face][10])

---

### Runners / launch tips (CPU)

* **llama.cpp / llama-cpp-python, LM Studio, KoboldCpp, Ollama** all run GGUF on CPU. Use **Q4\_K\_M or Q5\_K\_M**, **context 2048–4096**, and **–threads** equal to physical cores. ([Hugging Face][9], [Hugging Face][10], [Hugging Face][12], [Hugging Face][11])

> **Safety note:** “Uncensored” models will willingly produce sensitive or dangerous content. Please use them responsibly and comply with laws and platform rules. Zephyr’s own card warns it can generate problematic text. ([Hugging Face][10])

---

If you tell me your **CPU model**, **OS**, and **primary use** (general chat, coding, RP, long‑context, etc.), I can narrow this to one or two best choices and give ready‑to‑run commands.

[1]: https://github.com/ggml-org/llama.cpp/discussions/3847?utm_source=chatgpt.com "Hardware specs for GGUF 7B/13B/30B parameter models #3847"
[2]: https://www.reddit.com/r/LocalLLaMA/comments/17mjiba/max_tokenssecond_on_a_cpu_you_can_achieve_with/?utm_source=chatgpt.com "Max Tokens/second on a CPU you can achieve with Mistral ... - Reddit"
[3]: https://forum.level1techs.com/t/ollama-on-cpu-performance-some-data-and-a-request-for-more/214896?utm_source=chatgpt.com "Ollama on CPU Performance - Some Data and a Request for More"
[4]: https://www.reddit.com/r/Oobabooga/comments/1ac9otj/13b_gguf_shared_memory_and_bad_performance_help/?utm_source=chatgpt.com "13B GGUF - Shared Memory and Bad Performance - Help - Reddit"
[5]: https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF?utm_source=chatgpt.com "bartowski/dolphin-2.9-llama3-8b-GGUF - Hugging Face"
[6]: https://huggingface.co/MoMonir/dolphin-2.9-llama3-8b-GGUF?utm_source=chatgpt.com "MoMonir/dolphin-2.9-llama3-8b-GGUF - Hugging Face"
[7]: https://huggingface.co/bartowski/dolphin-2.9.1-llama-3-8b-GGUF?utm_source=chatgpt.com "bartowski/dolphin-2.9.1-llama-3-8b-GGUF - Hugging Face"
[8]: https://ollama.com/library/dolphin-llama3?utm_source=chatgpt.com "dolphin-llama3 - Ollama"
[9]: https://huggingface.co/TheBloke/OpenHermes-2.5-Mistral-7B-GGUF "TheBloke/OpenHermes-2.5-Mistral-7B-GGUF · Hugging Face"
[10]: https://huggingface.co/TheBloke/zephyr-7B-beta-GGUF "TheBloke/zephyr-7B-beta-GGUF · Hugging Face"
[11]: https://huggingface.co/TheBloke/MythoMax-L2-13B-GGUF "TheBloke/MythoMax-L2-13B-GGUF · Hugging Face"
[12]: https://huggingface.co/TheBloke/Pygmalion-2-7B-GGUF "TheBloke/Pygmalion-2-7B-GGUF · Hugging Face"
[13]: https://huggingface.co/TheBloke/Mistral-Pygmalion-7B-GGUF?utm_source=chatgpt.com "TheBloke/Mistral-Pygmalion-7B-GGUF - Hugging Face"
[14]: https://huggingface.co/TheBloke/Nous-Hermes-Llama-2-7B-GGUF?utm_source=chatgpt.com "TheBloke/Nous-Hermes-Llama-2-7B-GGUF - Hugging Face"
[15]: https://opencsg.com/models/AIWizards/openchat_3.5-GGUF?utm_source=chatgpt.com "openchat_3.5-GGUF - 开源模型 - TheBloke - OpenCSG"
[16]: https://github.com/LostRuins/koboldcpp/wiki?utm_source=chatgpt.com "Home · LostRuins/koboldcpp Wiki - GitHub"
[17]: https://gitlab.informatik.uni-halle.de/ambcj/llama.cpp/-/blob/gguf-v0.4.3/README.md?utm_source=chatgpt.com "README.md · gguf-v0.4.3 · undefined - llama.cpp - GitLab"
[18]: https://huggingface.co/bartowski/gemma-2-9b-it-GGUF?utm_source=chatgpt.com "bartowski/gemma-2-9b-it-GGUF - Hugging Face"
