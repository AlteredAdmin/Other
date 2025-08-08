Here are the **uncensored models that run best on a Raspberry Pi with Ollama**, ordered by how practical they are on a Pi (speed ↔ quality). I’m assuming a **Pi 5 with 8 GB RAM**; I note when something is still OK on a Pi 4 or when it’s likely too slow.

### Best picks (Pi 5, 8 GB)

1. **artifish/llama3.2-uncensored (3B)** — small, modern, uncensored Llama 3.2 variant made via abliteration; **\~2.2 GB (Q4)**, 128k context. Great default for a Pi: coherent, uncensored, and light.
   `ollama run artifish/llama3.2-uncensored` ([Ollama][1])

2. **dolphin-phi:2.7b** — Eric Hartford’s **uncensored** Phi‑2 (2.7B). Very light and fast on ARM; good for assistants and tools. Multiple quant tags (e.g., Q3\_K\_S \~1.3 GB).
   `ollama run dolphin-phi:2.7b` ([Ollama][2], [Ollama][3])

3. **JOSIEFIED‑Qwen3 (0.6B / 1.7B / 4B / 8B)** — Qwen3 family **“abliterated” to maximize uncensored behavior**; choose **0.6B/1.7B** for speed, **4B** for quality while still Pi‑friendly.
   Examples:
   `ollama run goekdenizguelmez/JOSIEFIED-Qwen3:1.7b`
   `ollama run goekdenizguelmez/JOSIEFIED-Qwen3:4b` ([Ollama][4])

4. **WizardLM‑7B‑Uncensored** — classic uncensored 7B; **Q4\_K\_M ≈ 4.08 GB, needs \~6.6 GB RAM**, so it fits on an 8 GB Pi 5; expect a few tokens/sec.
   `ollama run wizardlm-uncensored:13b` *(13B exists but is not Pi‑friendly; use 7B variants when available)*
   For sizes/RAM: see TheBloke’s 7B and 13B tables. ([Hugging Face][5], [Hugging Face][6])

5. **llama2-uncensored:7b** — lightweight uncensored baseline; **Ollama notes 7B generally needs ≥8 GB RAM.** Slower than the 3B/2.7B picks but workable on Pi 5.
   `ollama run llama2-uncensored:7b` ([Ollama][7], [GitHub][8])

6. **Lexi Llama‑3 8B Uncensored** — stronger quality; **Q4\_K\_M ≈ 4.9 GB**, runs on Pi 5 but noticeably slower; use if you’re OK with latency.
   `ollama run taozhiyuai/llama-3-8b-lexi-uncensored:v1_q4_k_m` ([Ollama][9])

### Ultra‑small options (fastest, least RAM)

* **TinyDolphin 1.1B (uncensored)** — good when you need speed on Pi 4/low‑power; Q4/Q5 GGUF builds exist. Use via a Modelfile or llama.cpp‑style GGUF; quality is modest. ([Hugging Face][10], [Hugging Face][11])

### Likely **too heavy** for a Raspberry Pi (list for awareness)

* **Dolphin 3.x Llama‑3.1 8B** — excellent uncensored generalist; still usable on Pi 5 at a few tok/s, but expect lag. Prefer Lexi/Dolphin only if you accept the speed hit. ([Hugging Face][12], [Ollama][13])
* **WizardLM / Wizard‑Vicuna 13B Uncensored** — **13B generally wants ≥16 GB RAM**; not recommended on a Pi without offload/remote inference. ([Ollama][14], [Hugging Face][6])
* **DeepSeek‑R1‑Distill‑Qwen‑7B‑uncensored** — Ollama card shows **\~15 GB** footprint; skip on Pi. ([Ollama][15])

---

## What to expect for speed

Community measurements on Pi 5 CPUs show roughly:

* **7B models \~2.4 tokens/sec** (Mistral‑7B Q4\_K\_M) — near “speaking speed,” but multi‑sentence replies still take time. ([Reddit][16])
* **Small models (2–3B) \~4–7 tok/s**, e.g., **dolphin‑phi \~4.7 tok/s** in one report. ([Reddit][16])

Guides also confirm **Pi 5 8 GB can run 7B**, but smaller models respond much faster; Pi 4 can run tiny models and very slow 7B. ([It's FOSS][17], [Reddit][18], [Reddit][19])

---

## Quick install & good quant tags

1. **Install Ollama on 64‑bit Pi OS / Ubuntu:**

   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

   Then `ollama run <model>`. ([Pi My Life Up][20])

2. **Quantization to try first:**

   * **Q4\_K\_M** for balance (often \~best quality vs. size on CPU).
   * Drop to **Q3\_K\_M/Q3\_K\_L** if you run out of RAM or need more speed.
     (See each model’s table for exact sizes / “Max RAM required”.) ([Hugging Face][21], [Hugging Face][22])

3. **RAM rule of thumb (from Ollama docs):** **\~8 GB for 7B, 16 GB for 13B.** That matches experience on the Pi (7B OK, 13B not). ([GitHub][8], [Ollama][7])

---

## Copy‑paste commands

* **Fast & tiny (great default):**

  ````bash
  ollama run artifish/llama3.2-uncensored
  ``` :contentReference[oaicite:16]{index=16}

  ````
* **Fast & capable small model:**

  ````bash
  ollama run dolphin-phi:2.7b
  ``` :contentReference[oaicite:17]{index=17}

  ````
* **Small uncensored Qwen (choose size):**

  ````bash
  ollama run goekdenizguelmez/JOSIEFIED-Qwen3:1.7b
  # or
  ollama run goekdenizguelmez/JOSIEFIED-Qwen3:4b
  ``` :contentReference[oaicite:18]{index=18}

  ````
* **Stronger but slower 7B:**

  ````bash
  ollama run llama2-uncensored:7b
  ``` :contentReference[oaicite:19]{index=19}

  ````
* **Higher quality, slow 8B:**

  ````bash
  ollama run taozhiyuai/llama-3-8b-lexi-uncensored:v1_q4_k_m
  ``` :contentReference[oaicite:20]{index=20}
  ````

---

## Notes & tips

* **Thermals & power:** Long generations can throttle the Pi. Use a good PSU and active cooling; users report answer latencies ranging **6–50 s** on Llama‑3.2‑3B depending on load. ([Raspberry Pi Forums][23])
* **Want more speed?** A Pi 5 can drive an **AMD eGPU** for big speedups (not trivial, but demonstrated). ([Jeff Geerling][24], [GitHub][25])
* **Uncensored ≠ unmoderated.** Model cards explicitly warn these models will comply with sensitive or unethical requests; if you expose them, add your own safety layer and logging. ([Ollama][7], [Ollama][9], [Ollama][2])

If you tell me your exact Pi model (Pi 4 vs Pi 5, RAM) and what you value most (speed, coding quality, RP/writing, reasoning), I can narrow this to 2–3 concrete picks and the exact quant tags.

[1]: https://ollama.com/artifish/llama3.2-uncensored "artifish/llama3.2-uncensored"
[2]: https://ollama.com/library/dolphin-phi?utm_source=chatgpt.com "dolphin-phi - Ollama"
[3]: https://ollama.com/library/dolphin-phi%3A2.7b-v2.6-q3_K_S/blobs/e28142a61dc1?utm_source=chatgpt.com "dolphin-phi:2.7b-v2.6-q3_K_S/model - Ollama"
[4]: https://ollama.com/goekdenizguelmez/JOSIEFIED-Qwen3 "goekdenizguelmez/JOSIEFIED-Qwen3"
[5]: https://huggingface.co/TheBloke/WizardLM-7B-uncensored-GGUF?utm_source=chatgpt.com "TheBloke/WizardLM-7B-uncensored-GGUF - Hugging Face"
[6]: https://huggingface.co/TheBloke/WizardLM-13B-Uncensored-GGUF?utm_source=chatgpt.com "TheBloke/WizardLM-13B-Uncensored-GGUF - Hugging Face"
[7]: https://ollama.com/library/llama2-uncensored "llama2-uncensored"
[8]: https://github.com/ollama/ollama?utm_source=chatgpt.com "ollama/ollama: Get up and running with Llama 3.3, DeepSeek-R1 ..."
[9]: https://ollama.com/taozhiyuai/llama-3-8b-lexi-uncensored "taozhiyuai/llama-3-8b-lexi-uncensored"
[10]: https://huggingface.co/v8karlo/UNCENSORED-TinyDolphin-2.8.1-1.1b-Q4_K_M-GGUF?utm_source=chatgpt.com "v8karlo/UNCENSORED-TinyDolphin-2.8.1-1.1b-Q4_K_M-GGUF"
[11]: https://huggingface.co/v8karlo/UNCENSORED-TinyDolphin-2.8-1.1b-Q5_K_M-GGUF?utm_source=chatgpt.com "v8karlo/UNCENSORED-TinyDolphin-2.8-1.1b-Q5_K_M-GGUF"
[12]: https://huggingface.co/cognitivecomputations/dolphin-2.9.4-llama3.1-8b-gguf?utm_source=chatgpt.com "cognitivecomputations/dolphin-2.9.4-llama3.1-8b-gguf - Hugging Face"
[13]: https://ollama.com/search?p=1&q=dolphin&utm_source=chatgpt.com "dolphin · Ollama Search"
[14]: https://ollama.com/library/wizardlm-uncensored%3A13b?utm_source=chatgpt.com "wizardlm-uncensored:13b - Ollama"
[15]: https://ollama.com/thirdeyeai/DeepSeek-R1-Distill-Qwen-7B-uncensored "thirdeyeai/DeepSeek-R1-Distill-Qwen-7B-uncensored"
[16]: https://www.reddit.com/r/LocalLLaMA/comments/18c2uch/mistral_7b_q4_k_m_on_a_pi_5_in_realtime/ "Mistral 7B (Q4_K_M) on a Pi 5 (in realtime) : r/LocalLLaMA"
[17]: https://itsfoss.com/raspberry-pi-ollama-ai-setup/?utm_source=chatgpt.com "How to Run LLMs Locally on Raspberry Pi Using Ollama AI - It's FOSS"
[18]: https://www.reddit.com/r/LocalLLaMA/comments/18c2uch/mistral_7b_q4_k_m_on_a_pi_5_in_realtime/?utm_source=chatgpt.com "Mistral 7B (Q4_K_M) on a Pi 5 (in realtime) : r/LocalLLaMA - Reddit"
[19]: https://www.reddit.com/r/LocalLLaMA/comments/1cbt78y/how_good_is_phi3mini_for_everyone/?utm_source=chatgpt.com "How good is Phi-3-mini for everyone? : r/LocalLLaMA - Reddit"
[20]: https://pimylifeup.com/raspberry-pi-ollama/ "Running Ollama on the Raspberry Pi - Pi My Life Up"
[21]: https://huggingface.co/mradermacher/Llama-3.2-3B-Instruct-uncensored-GGUF "mradermacher/Llama-3.2-3B-Instruct-uncensored-GGUF · Hugging Face"
[22]: https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGUF "TheBloke/llama2_7b_chat_uncensored-GGUF · Hugging Face"
[23]: https://forums.raspberrypi.com/viewtopic.php?t=384602&utm_source=chatgpt.com "Performance increase with LLMs running in Ollama by overclocking?"
[24]: https://www.jeffgeerling.com/blog/2024/llms-accelerated-egpu-on-raspberry-pi-5?utm_source=chatgpt.com "LLMs accelerated with eGPU on a Raspberry Pi 5 | Jeff Geerling"
[25]: https://github.com/geerlingguy/ollama-benchmark/issues/1?utm_source=chatgpt.com "Benchmark AMD GPUs on Raspberry Pi 5 · Issue #1 - GitHub"
