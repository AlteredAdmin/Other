Here’s what runs **well on a CPU‑only machine with 16 GB RAM**. In practice you’ll get the best experience with **3–4B** models (snappy) and can run **7B** at 4‑bit (usable but slower). 13B is technically possible but leaves little headroom and will be slow on CPU. ([GitHub][1], [GitHub][2])

### Top picks (CPU‑friendly, high quality)

* **Microsoft Phi‑3.5 Mini Instruct (3.8B)** — strong instruction following for its size; MIT‑licensed, easy for commercial use. Works great in 4‑bit GGUF on CPU. Context 128k. ([Hugging Face][3], [Hugging Face][4])
* **Meta Llama‑3.2‑3B‑Instruct (3B)** — multilingual, solid quality; runs comfortably on CPU at Q4. License is more restrictive than MIT/Apache. ([Hugging Face][5], [Llama][6], [Hugging Face][7])
* **Qwen‑2.5‑3B‑Instruct (3B)** — very capable small model; GGUF “I‑quants” and “K‑quants” available (try both; K is often faster on CPU). Note: Qwen says **3B is not Apache‑2.0**, while other sizes mostly are. ([Hugging Face][8], [Reddit][9], [Qwen][10])
* **Gemma 3‑4B‑IT (4B, QAT int4)** — compact and strong; **\~2.6 GB at int4** for weights, so great on CPU. License has additional use restrictions compared to Apache/MIT. ([Google Developers Blog][11], [Google AI for Developers][12], [The Verge][13])
* **DeepSeek‑R1 Distill Qwen‑1.5B (1.5B)** — if you want small‑footprint **reasoning**. Quantized builds show \~66 tok/s on modern laptop CPUs with \~1.2 GB RAM peak; very light for 16 GB systems. ([Hugging Face][14], [Hugging Face][15])

### Can run, but slower on CPU

* **Mistral 7B Instruct / Qwen‑2.5‑7B Instruct (7B)** — run in **Q4\_K** on CPU within 16 GB; expect single‑digit to \~20 tok/s depending on CPU/RAM speed. Apache‑2.0 for Qwen‑2.5‑7B. ([GitHub][1], [GitHub][16], [NVIDIA NIM APIs][17])
* **DeepSeek‑R1 Distill 7B** — fits at Q4 on CPU; community notes say it works but is **slow**; 20 GB RAM recommended for comfort, though 16 GB can work with care. ([Hugging Face][18], [Reddit][19], [Unsloth][20])

### How much memory do you need?

* Rough guide for **Q4\_0 at 2k context** (RAM, CPU inference): **\~4 GB for 3B, \~8 GB for 7B, \~16 GB for 13B**. Higher context or higher‑bit quants need more. ([GitHub][1], [GitHub][2])
* **Context length dominates memory** (KV cache grows roughly linearly with context). Keep contexts modest on 16 GB machines. Ollama also defaults to **4096 tokens** unless you raise `num_ctx`. ([Medium][21])
* Newer **I‑quants (IQ3\_M, etc.)** trade speed for accuracy at very low bit‑rates; on **CPU, K‑quants are often faster** — try **Q4\_K\_M / Q5\_K\_M** first. ([Hugging Face][8], [Reddit][9], [ionio.ai][22])

### Expected speed on CPU (very approximate)

Actual tokens/sec depend on cores and especially **memory bandwidth**. Community and vendor data show \~7–30 tok/s for small models on mainstream CPUs; higher with tuned setups. **RAM speed matters.** ([GitHub][23], [Reddit][24], [GitHub][25], [amperecomputing.com][26])

### Easiest ways to run on CPU

* **llama.cpp** — fastest, widest hardware support; GGUF format; server with OpenAI‑compatible API; supports **speculative decoding** to speed up generation. ([GitHub][27], [GitHub][28], [GitHub][29])
* **LM Studio** — friendly UI, runs **GGUF** locally (CPU or GPU) and recently added **speculative decoding** (1.5–3× speedups possible on larger targets with tiny drafts). ([LM Studio][30], [LM Studio][31])
* **Ollama** — simple one‑line model pulls and an API; works on CPU‑only, but CPU performance trails llama.cpp in many reports. ([blog.gordonbuchan.com][32], [Reddit][33])
* **KoboldCPP** — great for chat/story; clear RAM table (see above). ([GitHub][1])

### Suggested picks by goal

* **Fastest feel on 16 GB CPU:** *Gemma 3‑4B‑IT (int4)*, *Phi‑3.5 Mini*, *Qwen‑2.5‑3B‑Instruct*. ([Google Developers Blog][11], [Hugging Face][3], [Hugging Face][8])
* **Smallest RAM with decent reasoning:** *DeepSeek‑R1 Distill 1.5B*. ([Hugging Face][14], [Hugging Face][15])
* **You need multilingual strength:** *Llama‑3.2‑3B‑Instruct* or *Qwen‑2.5‑3B‑Instruct*. ([Hugging Face][5], [Hugging Face][8])
* **Willing to accept slower speed for more capability:** *Mistral 7B Instruct* / *Qwen‑2.5‑7B Instruct (Apache‑2.0)* at **Q4\_K\_M**, short contexts. ([NVIDIA NIM APIs][17], [GitHub][1])

### Quick setup recipe (CPU)

1. Install **LM Studio** or **llama.cpp**. ([LM Studio][30], [GitHub][27])
2. Download a **GGUF Q4\_K\_M** of one model above. Try **IQ3\_M** only if you must save more RAM. ([Hugging Face][8], [Reddit][9])
3. Start with **context 2k–4k**, batch \~256–512, threads ≈ physical cores; measure tokens/sec and adjust. Faster RAM helps. ([Reddit][24], [GitHub][23])
4. (Optional) Enable **speculative decoding**: use a tiny draft (e.g., Llama‑3.2‑1B) to speed a 3–7B target. ([llama-cpp-python.readthedocs.io][34], [GitHub][35])

If you tell me your CPU model, I can recommend a concrete quant (e.g., **Q4\_K\_M vs IQ3\_M**) and expected tokens/sec.

[1]: https://github.com/LostRuins/koboldcpp/wiki?utm_source=chatgpt.com "Home · LostRuins/koboldcpp Wiki - GitHub"
[2]: https://github.com/LostRuins/koboldcpp/wiki/Home/f5d5f03a9ba0af4ad1e07688a150cb9cb498f2da?utm_source=chatgpt.com "Home · LostRuins/koboldcpp Wiki · GitHub"
[3]: https://huggingface.co/microsoft/Phi-3.5-mini-instruct?utm_source=chatgpt.com "microsoft/Phi-3.5-mini-instruct - Hugging Face"
[4]: https://huggingface.co/microsoft/Phi-3.5-mini-instruct/blob/main/LICENSE?utm_source=chatgpt.com "LICENSE · microsoft/Phi-3.5-mini-instruct at main - Hugging Face"
[5]: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct?utm_source=chatgpt.com "meta-llama/Llama-3.2-3B-Instruct - Hugging Face"
[6]: https://www.llama.com/llama3_2/license/?utm_source=chatgpt.com "Llama 3.2 Community License Agreement"
[7]: https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct?utm_source=chatgpt.com "meta-llama/Llama-3.2-1B-Instruct - Hugging Face"
[8]: https://huggingface.co/bartowski/Qwen2.5-3B-Instruct-GGUF?utm_source=chatgpt.com "bartowski/Qwen2.5-3B-Instruct-GGUF - Hugging Face"
[9]: https://www.reddit.com/r/LocalLLaMA/comments/1ba55rj/overview_of_gguf_quantization_methods/?utm_source=chatgpt.com "Overview of GGUF quantization methods : r/LocalLLaMA - Reddit"
[10]: https://qwenlm.github.io/blog/qwen2.5/?utm_source=chatgpt.com "Qwen2.5: A Party of Foundation Models! | Qwen"
[11]: https://developers.googleblog.com/en/gemma-3-quantized-aware-trained-state-of-the-art-ai-to-consumer-gpus/?utm_source=chatgpt.com "Gemma 3 QAT Models: Bringing state-of-the-Art AI to consumer GPUs"
[12]: https://ai.google.dev/gemma/terms?utm_source=chatgpt.com "Gemma Terms of Use | Google AI for Developers - Gemini API"
[13]: https://www.theverge.com/ai-artificial-intelligence/627968/google-gemma-3-open-ai-model?utm_source=chatgpt.com "Google calls Gemma 3 the most powerful AI model you can run on one GPU"
[14]: https://huggingface.co/NexaAI/DeepSeek-R1-Distill-Qwen-1.5B-NexaQuant?utm_source=chatgpt.com "NexaAI/DeepSeek-R1-Distill-Qwen-1.5B-NexaQuant - Hugging Face"
[15]: https://huggingface.co/hdnh2006/DeepSeek-R1-Distill-Qwen-1.5B-GGUF?utm_source=chatgpt.com "hdnh2006/DeepSeek-R1-Distill-Qwen-1.5B-GGUF - Hugging Face"
[16]: https://github.com/ggml-org/llama.cpp/discussions/8273?utm_source=chatgpt.com "Performance of llama.cpp on Snapdragon X Elite/Plus #8273 - GitHub"
[17]: https://build.nvidia.com/qwen/qwen2_5-7b-instruct/modelcard?utm_source=chatgpt.com "qwen2.5-7b-instruct Model by Qwen - NVIDIA NIM APIs"
[18]: https://huggingface.co/Mungert/DeepSeek-R1-Distill-Qwen-7B-GGUF?utm_source=chatgpt.com "Mungert/DeepSeek-R1-Distill-Qwen-7B-GGUF - Hugging Face"
[19]: https://www.reddit.com/r/selfhosted/comments/1ic8zil/yes_you_can_run_deepseekr1_locally_on_your_device/?utm_source=chatgpt.com "Yes, you can run DeepSeek-R1 locally on your device (20GB RAM ..."
[20]: https://unsloth.ai/blog/deepseekr1-dynamic?utm_source=chatgpt.com "Run DeepSeek-R1 Dynamic 1.58-bit - Unsloth AI"
[21]: https://medium.com/%40lyx_62906/context-kills-vram-how-to-run-llms-on-consumer-gpus-a785e8035632?utm_source=chatgpt.com "Context Kills VRAM: How to Run LLMs on consumer GPUs - Medium"
[22]: https://www.ionio.ai/blog/llms-on-cpu-the-power-of-quantization-with-gguf-awq-gptq?utm_source=chatgpt.com "LLMs on CPU: The Power of Quantization with GGUF, AWQ, & GPTQ"
[23]: https://github.com/ggml-org/llama.cpp/discussions/3167?utm_source=chatgpt.com "CPU Performance · ggml-org llama.cpp · Discussion #3167 - GitHub"
[24]: https://www.reddit.com/r/LocalLLaMA/comments/14ilo0t/extensive_llamacpp_benchmark_more_speed_on_cpu_7b/?utm_source=chatgpt.com "Extensive LLama.cpp benchmark & more speed on CPU, 7b to 30b ..."
[25]: https://github.com/ggerganov/llama.cpp/issues/34?utm_source=chatgpt.com "benchmarks? #34 - ggml-org/llama.cpp - GitHub"
[26]: https://amperecomputing.com/en/blogs/ai-is-expensive-but-it-does-not-need-to-be?utm_source=chatgpt.com "Llama me impressed! AI is expensive, but it does not need to be"
[27]: https://github.com/ggml-org/llama.cpp?utm_source=chatgpt.com "ggml-org/llama.cpp: LLM inference in C/C++ - GitHub"
[28]: https://raw.githubusercontent.com/ggml-org/llama.cpp/master/tools/server/README.md?utm_source=chatgpt.com "https://raw.githubusercontent.com/ggml-org/llama.c..."
[29]: https://github.com/ggerganov/llama.cpp/blob/master/examples/speculative/README.md?utm_source=chatgpt.com "llama.cpp/examples/speculative/README.md at master ... - GitHub"
[30]: https://lmstudio.ai/?utm_source=chatgpt.com "LM Studio - Discover, download, and run local LLMs"
[31]: https://lmstudio.ai/blog/lmstudio-v0.3.10?utm_source=chatgpt.com "LM Studio 0.3.10: Speculative Decoding"
[32]: https://blog.gordonbuchan.com/blog/index.php/2025/01/11/using-ollama-to-host-an-llm-on-cpu-only-equipment-to-enable-a-local-chatbot-and-llm-api-server/?utm_source=chatgpt.com "Using Ollama to host an LLM on CPU-only equipment to enable a ..."
[33]: https://www.reddit.com/r/LocalLLaMA/comments/1csgnbh/how_to_optimize_ollama_for_cpuonly_inference/?utm_source=chatgpt.com "How to optimize Ollama for CPU-only inference? : r/LocalLLaMA"
[34]: https://llama-cpp-python.readthedocs.io/?utm_source=chatgpt.com "Getting Started - llama-cpp-python"
[35]: https://github.com/ggml-org/llama.cpp/discussions/10466?utm_source=chatgpt.com "Speculative decoding potential for running big LLMs on consumer ..."
















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
