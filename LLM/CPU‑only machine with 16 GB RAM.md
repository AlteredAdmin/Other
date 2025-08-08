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
