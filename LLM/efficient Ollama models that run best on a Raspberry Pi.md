Here are the small, efficient Ollama models that run best on a Raspberry Pi (Pi 5 recommended). I list what they’re good at plus the typical download size so you can judge fit and speed.

**Top picks (general chat / reasoning)**

* **DeepSeek‑R1‑Distill 1.5B** — strongest “reasoning‑style” small model; tiny (≈**1.1 GB**, Q4\_K\_M) and reported as the *snappiest* R1 variant on Pi. Good default if you want small + capable. `ollama run deepseek-r1:1.5b`. ([Ollama][1], [Pi My Life Up][2])
* **Llama 3.2 3B Instruct** — balanced quality for general use; runs comfortably on Pi 5, \~**3–6 tok/s** on CPU. File \~3.4 GB at q8\_0 or \~2 GB at q4; use q4 for speed. `ollama run llama3.2:3b`. ([Medium][3], [GitHub][4], [ApX Machine Learning][5])
* **Gemma 2 2B Instruct** — very fast and light, strong quality for its size; used \~**3 GB RAM** in a Pi 5 test; file \~**1.7 GB** (q4\_K\_M). `ollama run gemma2:2b`. ([It's FOSS][6], [Ollama][7])

**Coding‑focused (also fine for chat)**

* **Qwen 2.5 Coder 1.5B / 3B** — excellent small coder; pick **1.5B** for speed or **3B** for more depth. 3B used \~**5.4 GB RAM** on Pi 5; file sizes \~**1.8–3.3 GB** depending on quant. `ollama run qwen2.5-coder:1.5b` or `:3b`. ([Ollama][8], [It's FOSS][6], [Ollama][9], [Ollama][10])

**Tiny & fastest**

* **TinyLlama 1.1B** — ultra‑small (≈**0.64 GB** q4\_0); fastest replies, good for quick utilities/agents where quality can be lower. `ollama run tinyllama`. ([Ollama][11], [Ollama][12], [Pi My Life Up][2])
* **SmolLM2 1.7B** — tiny, multilingual, decent quality for its size; model file ≈**1.8 GB** (q8\_0; pick a q4 tag for less RAM). `ollama run smollm2:1.7b`. ([Ollama][13], [Ollama][14])

**Other good options**

* **Phi‑3 / Phi‑3.5 Mini (≈3.8B)** — compact Microsoft models; workable on Pi, but some users see more hallucinations on complex tasks. `ollama run phi3:mini` or `phi3.5:mini`. ([Ollama][15], [Pi My Life Up][2], [It's FOSS][6])
* **Nemotron‑Mini 4B Instruct** — NVIDIA’s small, commercial‑friendly model tuned for **RAG / tools / function calling**; files **2.6–3.1 GB** depending on quant. `ollama run nemotron-mini:4b-instruct-q4_0`. ([Ollama][16], [Ollama][17], [Ollama][18])

---

### What to expect on a Pi

* **Pi 5 (8 GB or 16 GB) is strongly preferred.** It’s 64‑bit Arm and runs Ollama fine; install with `curl -fsSL https://ollama.com/install.sh | sh`. Use a **64‑bit OS**. ([Pi My Life Up][2], [Ollama][19])
* **Speed:** On a Pi 5 CPU, **llama3.2:3b** measures around **4–6 tokens/sec**; **8B** class models drop to \~2 tok/s and feel sluggish. ([GitHub][4], [Medium][3])
* **RAM headroom:** Ollama suggests **\~8 GB RAM for 7B** models; Pi 5 **16 GB** exists and can load bigger models, but CPU‑only generation will still be slow. ([GitHub][20], [Raspberry Pi][21], [Tom's Hardware][22])
* **Quantization:** Default is **Q4** in Ollama; start with **`q4_K_M`** for quality/speed balance. Lower (q3) is faster and smaller; higher (q5/q6/q8) improves quality but needs more RAM and is slower. KV‑cache quantization can further cut memory. ([Ollama][23], [Collabnix][24], [smcleod.net][25])
* **Storage:** Model downloads are large (often **>1–3 GB** each). Keep models on SSD if possible. ([Raspberry Pi Forums][26])
* **External GPUs:** You’ll run CPU‑only by default. Folks have attached AMD GPUs to a Pi 5 and reached **\~40–56 tok/s** with 3B/8B via Vulkan in llama.cpp, but **Ollama doesn’t support Vulkan** today. ([GitHub][4], [GitHub][27])
* **R1 caveat:** DeepSeek‑R1 models include censorship/bias guardrails; behavior varies by build and platform. If that matters, test with your prompts. ([Ollama][1], [WIRED][28])

---

### Quick “which model should I use?” guide

* **Fastest usable chat on any Pi:** `tinyllama` → upgrade to `smollm2:1.7b` if you want a quality bump. ([Ollama][11], [Ollama][13], [Pi My Life Up][2])
* **Best small general assistant on Pi 5:** `llama3.2:3b` or `gemma2:2b`. If you need stronger step‑by‑step reasoning at tiny size, `deepseek-r1:1.5b`. ([Medium][3], [It's FOSS][6], [Ollama][1])
* **Coding:** `qwen2.5-coder:1.5b` (speed) or `qwen2.5-coder:3b` (quality). ([Ollama][8], [It's FOSS][6])
* **RAG / tool calling:** `nemotron-mini:4b-instruct-q4_0` (short 4k context but solid tool use). ([Ollama][16])

---

### Example commands

```bash
# General chat
ollama run llama3.2:3b

# Small, strong reasoning
ollama run deepseek-r1:1.5b

# Very fast & tiny
ollama run tinyllama

# Efficient Google small model
ollama run gemma2:2b

# Coding – light or stronger
ollama run qwen2.5-coder:1.5b
ollama run qwen2.5-coder:3b

# NVIDIA SLM tuned for RAG/tools
ollama run nemotron-mini:4b-instruct-q4_0
```

([Medium][3], [Ollama][1], [Ollama][11], [Ollama][29], [Ollama][9], [Ollama][16])

---

If you tell me **which Pi (model/RAM)** and your **primary workload** (chat, coding, RAG, math/reasoning), I can narrow this to a single best model + quant and suggest context window and performance tweaks.

[1]: https://ollama.com/library/deepseek-r1%3A1.5b?utm_source=chatgpt.com "deepseek-r1:1.5b - Ollama"
[2]: https://pimylifeup.com/raspberry-pi-ollama/ "Running Ollama on the Raspberry Pi - Pi My Life Up"
[3]: https://medium.com/aidatatools/raspberry-pi-os-2024-10-22-benchmark-for-ollama-llama3-2-3b-and-1b-c649ebc1acd4?utm_source=chatgpt.com "Raspberry PI OS 2024–10–22 benchmark for Ollama (Llama3.2, 3b ..."
[4]: https://github.com/geerlingguy/ollama-benchmark/issues/1 "Benchmark AMD GPUs on Raspberry Pi 5 · Issue #1 · geerlingguy/ollama-benchmark · GitHub"
[5]: https://apxml.com/posts/ultimate-system-requirements-llama-3-models?utm_source=chatgpt.com "GPU Requirement Guide for Llama 3 (All Variants)"
[6]: https://itsfoss.com/llms-for-raspberry-pi/ "I Ran 9 Popular LLMs on Raspberry Pi 5; Here's What I Found"
[7]: https://ollama.com/library/gemma2%3A2b-instruct-q4_K_M/blobs/1e4fc624315d?utm_source=chatgpt.com "gemma2:2b-instruct-q4_K_M/model - Ollama"
[8]: https://ollama.com/library/qwen2.5-coder?utm_source=chatgpt.com "qwen2.5-coder - Ollama"
[9]: https://ollama.com/library/qwen2.5-coder%3A3b-instruct-q4_0?utm_source=chatgpt.com "qwen2.5-coder:3b-instruct-q4_0 - Ollama"
[10]: https://ollama.com/library/qwen2.5%3A3b-instruct-q4_0/blobs/5e69a0a67ad5?utm_source=chatgpt.com "qwen2.5:3b-instruct-q4_0/model - Ollama"
[11]: https://ollama.com/library/tinyllama?utm_source=chatgpt.com "tinyllama - Ollama"
[12]: https://ollama.com/library/tinyllama%3Alatest/blobs/2af3b81862c6?utm_source=chatgpt.com "tinyllama/model - Ollama"
[13]: https://ollama.com/library/smollm2%3A1.7b?utm_source=chatgpt.com "smollm2:1.7b - Ollama"
[14]: https://ollama.com/library/smollm2%3A1.7b/blobs/4d2396b16114?utm_source=chatgpt.com "smollm2:1.7b/model - Ollama"
[15]: https://ollama.com/library/phi3%3Amini?utm_source=chatgpt.com "phi3:mini - Ollama"
[16]: https://ollama.com/library/nemotron-mini%3A4b?utm_source=chatgpt.com "nemotron-mini:4b - Ollama"
[17]: https://ollama.com/library/nemotron-mini%3A4b-instruct-q4_K_M?utm_source=chatgpt.com "nemotron-mini:4b-instruct-q4_K_M - Ollama"
[18]: https://ollama.com/library/nemotron-mini%3A4b-instruct-q4_0/blobs/43b49b84f3e0?utm_source=chatgpt.com "nemotron-mini:4b-instruct-q4_0/model - Ollama"
[19]: https://ollama.com/install.sh?utm_source=chatgpt.com "install.sh - Ollama"
[20]: https://github.com/ollama/ollama?utm_source=chatgpt.com "ollama/ollama: Get up and running with Llama 3.3, DeepSeek-R1 ..."
[21]: https://www.raspberrypi.com/products/raspberry-pi-5/?utm_source=chatgpt.com "Buy a Raspberry Pi 5"
[22]: https://www.tomshardware.com/raspberry-pi/raspberry-pi-5-16gb-review?utm_source=chatgpt.com "Raspberry Pi 5 16GB Review: Plenty of memory - Tom's Hardware"
[23]: https://ollama.com/library/wizardlm%3A7b-q4_K_M?utm_source=chatgpt.com "wizardlm:7b-q4_K_M - Ollama"
[24]: https://collabnix.com/best-ollama-models-in-2025-complete-performance-comparison/?utm_source=chatgpt.com "Best Ollama Models 2025: Performance Comparison Guide"
[25]: https://smcleod.net/2024/12/bringing-k/v-context-quantisation-to-ollama/?utm_source=chatgpt.com "Bringing K/V Context Quantisation to Ollama - smcleod.net"
[26]: https://forums.raspberrypi.com/viewtopic.php?t=366146&utm_source=chatgpt.com "PI5 and easy AI/CV/LLM - Raspberry Pi Forums"
[27]: https://github.com/ollama/ollama/issues/7420?utm_source=chatgpt.com "Support AMD GPUs on Ampere, Raspberry Pis (arm64 ROCm) #7420"
[28]: https://www.wired.com/story/deepseek-censorship?utm_source=chatgpt.com "Here's How DeepSeek Censorship Actually Works-and How to Get Around It"
[29]: https://ollama.com/library/gemma2?utm_source=chatgpt.com "gemma2 - Ollama"
