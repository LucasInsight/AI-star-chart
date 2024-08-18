"""
版权所有 2024 AI星图

根据 Apache License, Version 2.0（“许可证”）授权；
除非遵守许可证，否则你不能使用此文件。
你可以在以下网址获得许可证副本：

    http://www.apache.org/licenses/LICENSE-2.0

除非适用法律要求或书面同意，根据许可证分发的软件按“原样”提供，
不提供任何明示或暗示的担保或保证。
请参阅许可证以了解管理权限和限制的特定语言。

附加条款：
- 本作品的副本可以自由复制和分发，但不得进行修改、衍生或演绎。
- 如需转载或其他用途，必须事先获得 AI星图权利人的书面许可。

---

Copyright 2024 AI星图

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Additional Terms:
- Copies of this work may be freely copied and distributed, but modification, derivation, or adaptation is not allowed.
- For any form of redistribution or other use, prior written permission from the copyright holder, AI

"""

# -*- coding: utf-8 -*-
"""AI星图-Llama-3.1-8B-Instruct-finetune-release
发布时间: 2024-08-13

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XApK1lhFUPNg1vAkjEjPgg2Ba5yiChnq

**欢迎来到AI星图**

本期课程，我们对Llama3.1进行中文数据集微调，并解决实际微调中遇到的问题，确保微调达到预期的效果。

To run this, press "*Runtime*" and press "*Run all*" on a **free** Tesla T4 Google Colab instance!
<div class="align-center">
  <a href="https://github.com/unslothai/unsloth"><img src="https://github.com/unslothai/unsloth/raw/main/images/unsloth%20new%20logo.png" width="115"></a>
  <a href="https://ollama.com/"><img src="https://raw.githubusercontent.com/unslothai/unsloth/nightly/images/ollama.png" height="44"></a>
  <a href="https://discord.gg/u54VK8m8tk"><img src="https://github.com/unslothai/unsloth/raw/main/images/Discord button.png" width="145"></a>
  <a href="https://ko-fi.com/unsloth"><img src="https://github.com/unslothai/unsloth/raw/main/images/Kofi button.png" width="145"></a></a> Join Discord if you need help + ⭐ <i>Star us on <a href="https://github.com/unslothai/unsloth">Github</a> </i> ⭐
</div>

To install Unsloth on your own computer, follow the installation instructions on our Github page [here](https://github.com/unslothai/unsloth#installation-instructions---conda).

You will learn how to do [data prep](#Data) and import a CSV, how to [train](#Train), how to [run the model](#Inference), & [how to export to Ollama!](#Ollama)

[Unsloth](https://github.com/unslothai/unsloth) now allows you to automatically finetune and create a [Modelfile](https://github.com/ollama/ollama/blob/main/docs/modelfile.md), and export to [Ollama](https://ollama.com/)! This makes finetuning much easier and provides a seamless workflow from `Unsloth` to `Ollama`!

**[NEW]** We now allow uploading CSVs, Excel files - try it [here](https://colab.research.google.com/drive/1VYkncZMfGFkeCEgN2IzbZIKEDkyQuJAS?usp=sharing) by using the Titanic dataset.

**视频课程概要：对Llama3.1进行中文数据集微调，支持Ollama运行**  
**Video Course Outline: Fine-Tuning Llama3.1 with Chinese Dataset for Ollama Deployment**

**课程简介：**  
**Course Introduction:**  
本课程基于unsloth将带领观众深入了解如何在低配CPU环境下，对Llama3.1-8B-Instruct大模型进行中文数据集的指令微调，并成功运行于Ollama引擎中。通过本课程，观众将掌握模型微调的核心技术，解决常见的微调过程中的问题，并最终实现模型在Ollama环境下的高效运行。  
This course will guide viewers through the process of fine-tuning the Llama3.1-8B-Instruct model with a Chinese dataset using unsloth, even in low-spec CPU environments, and successfully running it on the Ollama engine. Viewers will learn core techniques for model fine-tuning, troubleshoot common issues, and achieve efficient model deployment on the Ollama platform.

**课程目标：**  
**Course Objectives:**  
1. **低配GPU环境下的模型微调：** 学习如何在资源有限的CPU环境下，对Llama3.1-8B-Instruct大模型进行高效微调，特别是使用中文数据集进行指令微调，适应本地化的需求。  
   **Model Fine-Tuning in Low-Spec GPU Environments:** Learn how to efficiently fine-tune the Llama3.1-8B-Instruct model in resource-constrained CPU environments, particularly with a Chinese dataset for instruction-based fine-tuning to meet localization needs.

2. **支持Ollama引擎的微调模型运行：** 掌握如何在微调完成后，将模型加载并运行于Ollama引擎中，确保模型在实际应用中的兼容性和性能。  
   **Running Fine-Tuned Models on Ollama Engine:** Master how to load and run the fine-tuned model on the Ollama engine, ensuring compatibility and performance in practical applications.

**课程内容：**  
**Course Content:**  
1. **Llama3.1-8B-Instruct版本简介与微调基础：**  
   - 介绍Llama3.1-8B-Instruct模型的特点和适用场景。  
   - 微调的基本原理与步骤概述，特别是指令微调的细节讲解。  
   **Introduction to Llama3.1-8B-Instruct and Fine-Tuning Basics:**  
   - Overview of the Llama3.1-8B-Instruct model’s features and use cases.  
   - Basic principles and steps of fine-tuning, with detailed explanations on instruction-based fine-tuning.

2. **使用unsloth进行微调的实践：**  
   - 如何配置低配GPU环境进行微调，充分利用资源进行优化。  
   - 中文数据集的准备与加载，确保数据的有效性和覆盖面。  
   **Practical Fine-Tuning with Unsloth:**  
   - How to configure a low-spec GPU environment for fine-tuning, optimizing resource use.  
   - Preparation and loading of the Chinese dataset to ensure data validity and coverage.

3. **问题排查与修复：**  
   - 解决unsloth微调过程中可能出现的程序崩溃问题，提供详细的调试方法。  
   - 处理微调后模型复读、乱码、interface不兼容、指令未接收等常见问题，确保微调效果达到预期。  
   **Troubleshooting and Fixing Issues:**  
   - Resolving potential crashes during unsloth fine-tuning, with detailed debugging methods.  
   - Handling common issues post-fine-tuning such as model repetition, garbled text, interface incompatibility, and unprocessed instructions to ensure expected fine-tuning results.

4. **模型在Ollama引擎中的部署与运行：**  
   - 介绍Ollama引擎的特点与优势。  
   - 将微调后的模型导入Ollama引擎中，并进行测试和优化，确保模型的兼容性和性能。  
   **Deploying and Running Models on Ollama Engine:**  
   - Introduction to the features and advantages of the Ollama engine.  
   - Importing the fine-tuned model into the Ollama engine, followed by testing and optimization to ensure compatibility and performance.

5. **总结与展望：**  
   - 回顾课程的关键步骤与知识点。  
   - 展望Llama3.1大模型在业务场景下的应用前景和未来发展方向。  
   **Summary and Outlook:**  
   - Recap of key steps and knowledge points from the course.  
   - Future prospects and developments of the Llama3.1 model in business scenarios.

通过本课程的学习，观众将能够在有限的硬件条件下，对Llama3.1进行高效微调，并成功部署在Ollama引擎中，解决模型应用中的实际问题。  
By the end of this course, viewers will be able to efficiently fine-tune Llama3.1 under limited hardware conditions and successfully deploy it on the Ollama engine, addressing practical issues in model applications.
"""

# Commented out IPython magic to ensure Python compatibility.
# # Unsloth 安装
# %%capture
# # Installs Unsloth, Xformers (Flash Attention) and all other packages!
# !pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
# !pip install --no-deps "xformers<0.0.27" "trl<0.9.0" peft accelerate bitsandbytes

"""* We support Llama, Mistral, Phi-3, Gemma, Yi, DeepSeek, Qwen, TinyLlama, Vicuna, Open Hermes etc
* We support 16bit LoRA or 4bit QLoRA. Both 2x faster.
* `max_seq_length` can be set to anything, since we do automatic RoPE Scaling via [kaiokendev's](https://kaiokendev.github.io/til) method.
* With [PR 26037](https://github.com/huggingface/transformers/pull/26037), we support downloading 4bit models **4x faster**! [Our repo](https://huggingface.co/unsloth) has Llama, Mistral 4bit models.
* [**NEW**] We make Phi-3 Medium / Mini **2x faster**! See our [Phi-3 Medium notebook](https://colab.research.google.com/drive/1hhdhBa1j_hsymiW9m-WzxQtgqTH_NHqi?usp=sharing)
"""

# 模型装载 参数初始化
from unsloth import FastLanguageModel
import torch
max_seq_length = 131072 # Llama3.1支持128K # Choose any! We auto support RoPE Scaling internally!
dtype = None # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
load_in_4bit = True # Use 4bit quantization to reduce memory usage. Can be False.

# 4bit pre quantized models we support for 4x faster downloading + no OOMs.
fourbit_models = [
    "unsloth/Meta-Llama-3.1-8B-bnb-4bit",      # Llama-3.1 15 trillion tokens model 2x faster!
    "unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit",
    "unsloth/Meta-Llama-3.1-70B-bnb-4bit",
    "unsloth/Meta-Llama-3.1-405B-bnb-4bit",    # We also uploaded 4bit for 405b!
    "unsloth/Mistral-Nemo-Base-2407-bnb-4bit", # New Mistral 12b 2x faster!
    "unsloth/Mistral-Nemo-Instruct-2407-bnb-4bit",
    "unsloth/mistral-7b-v0.3-bnb-4bit",        # Mistral v3 2x faster!
    "unsloth/mistral-7b-instruct-v0.3-bnb-4bit",
    "unsloth/Phi-3-mini-4k-instruct",          # Phi-3 2x faster!d
    "unsloth/Phi-3-medium-4k-instruct",
    "unsloth/gemma-2-9b-bnb-4bit",
    "unsloth/gemma-2-27b-bnb-4bit",            # Gemma 2x faster!
] # More models at https://huggingface.co/unsloth

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Meta-Llama-3.1-8B-Instruct",
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
    # token = "hf_...", # use one if using gated models like meta-llama/Llama-2-7b-hf
)

"""We now add LoRA adapters so we only need to update 1 to 10% of all parameters!"""

# 微调参数初始化
model = FastLanguageModel.get_peft_model(
    model,
    r = 16, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0, # Supports any, but = 0 is optimized
    bias = "none",    # Supports any, but = "none" is optimized
    # [NEW] "unsloth" uses 30% less VRAM, fits 2x larger batch sizes!
    use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
    random_state = 3407,
    use_rslora = False,  # We support rank stabilized LoRA
    loftq_config = None, # And LoftQ
)

"""<a name="Data"></a>
### Data Prep
We now use the Alpaca dataset from [vicgalle](https://huggingface.co/datasets/vicgalle/alpaca-gpt4), which is a version of 52K of the original [Alpaca dataset](https://crfm.stanford.edu/2023/03/13/alpaca.html) generated from GPT4. You can replace this code section with your own data prep.
"""

# 装载数据集
from datasets import load_dataset
dataset = load_dataset("llm-wizard/alpaca-gpt4-data-zh", split = "train")
print(dataset.column_names)

"""One issue is this dataset has multiple columns. For `Ollama` and `llama.cpp` to function like a custom `ChatGPT` Chatbot, we must only have 2 columns - an `instruction` and an `output` column."""

# 打印数据集列
print(dataset.column_names)

"""To solve this, we shall do the following:
* Merge all columns into 1 instruction prompt.
* Remember LLMs are text predictors, so we can customize the instruction to anything we like!
* Use the `to_sharegpt` function to do this column merging process!

For example below in our [Titanic CSV finetuning notebook](https://colab.research.google.com/drive/1VYkncZMfGFkeCEgN2IzbZIKEDkyQuJAS?usp=sharing), we merged multiple columns in 1 prompt:

<img src="https://raw.githubusercontent.com/unslothai/unsloth/nightly/images/Merge.png" height="100">

To merge multiple columns into 1, use `merged_prompt`.
* Enclose all columns in curly braces `{}`.
* Optional text must be enclused in `[[]]`. For example if the column "Pclass" is empty, the merging function will not show the text and skp this. This is useful for datasets with missing values.
* You can select every column, or a few!
* Select the output or target / prediction column in `output_column_name`. For the Alpaca dataset, this will be `output`.

To make the finetune handle multiple turns (like in ChatGPT), we have to create a "fake" dataset with multiple turns - we use `conversation_extension` to randomnly select some conversations from the dataset, and pack them together into 1 conversation.
"""

# 数据merge
from unsloth import to_sharegpt
dataset = to_sharegpt(
    dataset,
    merged_prompt = "{instruction}[[\nYour input is:\n{input}]]",
    output_column_name = "output",
    conversation_extension = 0, # Select more to handle longer conversations
)

# 打印数据列、数据集的第一组微调数据
print(dataset.column_names)
print(dataset[1])

"""Finally use `standardize_sharegpt` to fix up the dataset!"""

# 数据修整
from unsloth import standardize_sharegpt
dataset = standardize_sharegpt(dataset)
print(dataset[1])

"""### Customizable Chat Templates

You also need to specify a chat template. Previously, you could use the Alpaca format as shown below.

The issue is the Alpaca format has 3 fields, whilst OpenAI style chatbots must only use 2 fields (instruction and response). That's why we used the `to_sharegpt` function to merge these columns into 1.
"""

# 定义提示词模板 生成初步prompt
chat_template = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{SYSTEM}<|eot_id|><|start_header_id|>user<|end_header_id|>

{INPUT}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

{OUTPUT}<|eot_id|>"""

from unsloth import apply_chat_template
dataset = apply_chat_template(
    dataset,
    tokenizer = tokenizer,
    chat_template = chat_template,
    default_system_message = "You are a helpful assistant",
)

print(dataset[1])

"""<a name="Train"></a>
### Train the model
Now let's use Huggingface TRL's `SFTTrainer`! More docs here: [TRL SFT docs](https://huggingface.co/docs/trl/sft_trainer). We do 60 steps to speed things up, but you can set `num_train_epochs=1` for a full run, and turn off `max_steps=None`. We also support TRL's `DPOTrainer`!
"""

# 微调引擎初始化
from trl import SFTTrainer
from transformers import TrainingArguments
from unsloth import is_bfloat16_supported
trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    dataset_text_field = "text",
    max_seq_length = max_seq_length,
    dataset_num_proc = 2,
    packing = False, # Can make training 5x faster for short sequences.
    args = TrainingArguments(
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        max_steps = 60,
        # num_train_epochs = 1, # For longer training runs!
        learning_rate = 2e-4,
        fp16 = not is_bfloat16_supported(),
        bf16 = is_bfloat16_supported(),
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs",
    ),
)

#@title Show current memory stats
gpu_stats = torch.cuda.get_device_properties(0)
start_gpu_memory = round(torch.cuda.max_memory_reserved() / 1024 / 1024 / 1024, 3)
max_memory = round(gpu_stats.total_memory / 1024 / 1024 / 1024, 3)
print(f"GPU = {gpu_stats.name}. Max memory = {max_memory} GB.")
print(f"{start_gpu_memory} GB of memory reserved.")

# 执行微调
trainer_stats = trainer.train()

#@title Show final memory and time stats
used_memory = round(torch.cuda.max_memory_reserved() / 1024 / 1024 / 1024, 3)
used_memory_for_lora = round(used_memory - start_gpu_memory, 3)
used_percentage = round(used_memory         /max_memory*100, 3)
lora_percentage = round(used_memory_for_lora/max_memory*100, 3)
print(f"{trainer_stats.metrics['train_runtime']} seconds used for training.")
print(f"{round(trainer_stats.metrics['train_runtime']/60, 2)} minutes used for training.")
print(f"Peak reserved memory = {used_memory} GB.")
print(f"Peak reserved memory for training = {used_memory_for_lora} GB.")
print(f"Peak reserved memory % of max memory = {used_percentage} %.")
print(f"Peak reserved memory for training % of max memory = {lora_percentage} %.")

"""<a name="Inference"></a>
### Inference
Let's run the model! Unsloth makes inference natively 2x faster as well! You should use prompts which are similar to the ones you had finetuned on, otherwise you might get bad results!
"""

# 推理测试
FastLanguageModel.for_inference(model) # Enable native 2x faster inference
messages = [                    # Change below!
    {"role": "user", "content": "Continue the fibonacci sequence! Your input is 1, 1, 2, 3, 5, 8,"},
]
input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt = True,
    return_tensors = "pt",
).to("cuda")

from transformers import TextStreamer
text_streamer = TextStreamer(tokenizer, skip_prompt = True)
_ = model.generate(input_ids, streamer = text_streamer, max_new_tokens = 128, pad_token_id = tokenizer.eos_token_id)

# 推理测试
FastLanguageModel.for_inference(model) # Enable native 2x faster inference
messages = [                    # Change below!
    {"role": "user", "content": "三原色是什么？你是谁？"}
]
input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt = True,
    return_tensors = "pt",
).to("cuda")

from transformers import TextStreamer
text_streamer = TextStreamer(tokenizer, skip_prompt = True)
_ = model.generate(input_ids, streamer = text_streamer, max_new_tokens = 128, pad_token_id = tokenizer.eos_token_id)

"""Since we created an actual chatbot, you can also do longer conversations by manually adding alternating conversations between the user and assistant!"""

# 推理测试
FastLanguageModel.for_inference(model) # Enable native 2x faster inference
messages = [                         # Change below!
    {"role": "user",      "content": "Continue the fibonacci sequence! Your input is 1, 1, 2, 3, 5, 8"},
    {"role": "assistant", "content": "The fibonacci sequence continues as 13, 21, 34, 55 and 89."},
    {"role": "user",      "content": "What is France's tallest tower called?"},
]
input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt = True,
    return_tensors = "pt",
).to("cuda")

from transformers import TextStreamer
text_streamer = TextStreamer(tokenizer, skip_prompt = True)
_ = model.generate(input_ids, streamer = text_streamer, max_new_tokens = 128, pad_token_id = tokenizer.eos_token_id)

"""<a name="Save"></a>
### Saving, loading finetuned models
To save the final model as LoRA adapters, either use Huggingface's `push_to_hub` for an online save or `save_pretrained` for a local save.

**[NOTE]** This ONLY saves the LoRA adapters, and not the full model. To save to 16bit or GGUF, scroll down!
"""

# lora模型持久化
model.save_pretrained("lora_model") # Local saving
tokenizer.save_pretrained("lora_model")
# model.push_to_hub("your_name/lora_model", token = "...") # Online saving
# tokenizer.push_to_hub("your_name/lora_model", token = "...") # Online saving

"""Now if you want to load the LoRA adapters we just saved for inference, set `False` to `True`:"""

# 使用unsloth内置引擎，对lora模型推理
if False:
    from unsloth import FastLanguageModel
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name = "lora_model", # YOUR MODEL YOU USED FOR TRAINING
        max_seq_length = max_seq_length,
        dtype = dtype,
        load_in_4bit = load_in_4bit,
    )
    FastLanguageModel.for_inference(model) # Enable native 2x faster inference
pass

messages = [                    # Change below!
    {"role": "user", "content": "Describe anything special about a sequence. Your input is 1, 1, 2, 3, 5, 8,"},
]
input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt = True,
    return_tensors = "pt",
).to("cuda")

from transformers import TextStreamer
text_streamer = TextStreamer(tokenizer, skip_prompt = True)
_ = model.generate(input_ids, streamer = text_streamer, max_new_tokens = 128, pad_token_id = tokenizer.eos_token_id)

"""You can also use Hugging Face's `AutoModelForPeftCausalLM`. Only use this if you do not have `unsloth` installed. It can be hopelessly slow, since `4bit` model downloading is not supported, and Unsloth's **inference is 2x faster**."""

# 使用huggingface引擎，对lora模型推理
if False:
    # I highly do NOT suggest - use Unsloth if possible
    from peft import AutoPeftModelForCausalLM
    from transformers import AutoTokenizer
    model = AutoPeftModelForCausalLM.from_pretrained(
        "lora_model", # YOUR MODEL YOU USED FOR TRAINING
        load_in_4bit = load_in_4bit,
    )
    tokenizer = AutoTokenizer.from_pretrained("lora_model")

"""<a name="Ollama"></a>
### Ollama Support

[Unsloth](https://github.com/unslothai/unsloth) now allows you to automatically finetune and create a [Modelfile](https://github.com/ollama/ollama/blob/main/docs/modelfile.md), and export to [Ollama](https://ollama.com/)! This makes finetuning much easier and provides a seamless workflow from `Unsloth` to `Ollama`!

Let's first install `Ollama`!
"""

# 安装ollama
if False:
  !curl -fsSL https://ollama.com/install.sh | sh

"""Next, we shall save the model to GGUF / llama.cpp

We clone `llama.cpp` and we default save it to `q8_0`. We allow all methods like `q4_k_m`. Use `save_pretrained_gguf` for local saving and `push_to_hub_gguf` for uploading to HF.

Some supported quant methods (full list on our [Wiki page](https://github.com/unslothai/unsloth/wiki#gguf-quantization-options)):
* `q8_0` - Fast conversion. High resource use, but generally acceptable.
* `q4_k_m` - Recommended. Uses Q6_K for half of the attention.wv and feed_forward.w2 tensors, else Q4_K.
* `q5_k_m` - Recommended. Uses Q6_K for half of the attention.wv and feed_forward.w2 tensors, else Q5_K.

We also support saving to multiple GGUF options in a list fashion! This can speed things up by 10 minutes or more if you want multiple export formats!
"""

# 微调后的模型保存到硬盘，并上传到hugging face
from google.colab import userdata


hug_token = userdata.get('hug_token')

hug_model = "LucasInsight/Meta-Llama-3.1-8B-Instruct"

# Save to 8bit Q8_0
if False: model.save_pretrained_gguf("model", tokenizer,)
# Remember to go to https://huggingface.co/settings/tokens for a token!
# And change hf to your username!
if True: model.push_to_hub_gguf(hug_model, tokenizer, token = hug_token)

# Save to 16bit GGUF
if False: model.save_pretrained_gguf("model", tokenizer, quantization_method = "f16")
if False: model.push_to_hub_gguf(hug_model, tokenizer, quantization_method = "f16", token = "")

# Save to q4_k_m GGUF
if False: model.save_pretrained_gguf("model", tokenizer, quantization_method = "q4_k_m")
if False: model.push_to_hub_gguf(hug_model, tokenizer, quantization_method = "q4_k_m", token = hug_token)

# Save to multiple GGUF options - much faster if you want multiple!
if True:
    model.push_to_hub_gguf(
        hug_model, # Change hf to your username!
        tokenizer,
        quantization_method = ["q4_k_m", "q8_0", "q5_k_m",],
        token = "", # Get a token at https://huggingface.co/settings/tokens
    )

"""We use `subprocess` to start `Ollama` up in a non blocking fashion! In your own desktop, you can simply open up a new `terminal` and type `ollama serve`, but in Colab, we have to use this hack!"""

# 启动ollama
if False:
  import subprocess
  subprocess.Popen(["ollama", "serve"])
  import time
  time.sleep(3) # Wait for a few seconds for Ollama to load!

"""`Ollama` needs a `Modelfile`, which specifies the model's prompt format. Let's print Unsloth's auto generated one:"""

# 打印ollama Modelfile
print(tokenizer._ollama_modelfile)

"""We now will create an `Ollama` model called `unsloth_model` using the `Modelfile` which we auto generated!"""

# ollama装载微调后的模型
# !ollama create unsloth_model -f ./model/Modelfile

"""And now we can do inference on it via `Ollama`!

You can also upload to `Ollama` and try the `Ollama` Desktop app by heading to https://www.ollama.com/
"""

# 调用ollama装载的微调后的模型chat接口
if False:
  !curl http://localhost:11434/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{ \
      "model": "unsloth_model", \
      "messages": [ \
        { \
          "role": "system", \
          "content": "你是LucasInsight的数字分身。" \
        }, \
        { \
          "role": "user", \
          "content": "你是谁？" \
        } \
      ] \
    }'

# 调用ollama装载的微调后的模型chat接口

if False:
  !curl http://localhost:11434/api/chat -d '{ \
      "model": "unsloth_model", \
      "messages": [ \
          { "role": "user", "content": "Continue the Fibonacci sequence: 1, 1, 2, 3, 5, 8," } \
      ] \
      }'

"""本期视频做到这里，欢迎大家点赞关注、收藏和转发。欢迎加入我们的社群，本期课程涉及到的代码，我会放到视频下方的链接。

谢谢大家的观看！

# ChatGPT interactive mode

### ⭐ To run the finetuned model like in a ChatGPT style interface, first click the **| >_ |** button.
![](https://raw.githubusercontent.com/unslothai/unsloth/nightly/images/Where_Terminal.png)

---
---
---

### ⭐ Then, type `ollama run unsloth_model`

![](https://raw.githubusercontent.com/unslothai/unsloth/nightly/images/Terminal_Type.png)

---
---
---
### ⭐ And you have a CHatGPT style assistant!

### Type any question you like and press `ENTER`. If you want to exit, hit `CTRL + D`
![](https://raw.githubusercontent.com/unslothai/unsloth/nightly/images/Assistant.png)

And we're done! If you have any questions on Unsloth, we have a [Discord](https://discord.gg/u54VK8m8tk) channel! If you find any bugs or want to keep updated with the latest LLM stuff, or need help, join projects etc, feel free to join our Discord!

Try our [Ollama CSV notebook](https://colab.research.google.com/drive/1VYkncZMfGFkeCEgN2IzbZIKEDkyQuJAS?usp=sharing) to upload CSVs for finetuning!

Some other links:
1. Zephyr DPO 2x faster [free Colab](https://colab.research.google.com/drive/15vttTpzzVXv_tJwEk-hIcQ0S9FcEWvwP?usp=sharing)
2. Llama 7b 2x faster [free Colab](https://colab.research.google.com/drive/1lBzz5KeZJKXjvivbYvmGarix9Ao6Wxe5?usp=sharing)
3. TinyLlama 4x faster full Alpaca 52K in 1 hour [free Colab](https://colab.research.google.com/drive/1AZghoNBQaMDgWJpi4RbffGM1h6raLUj9?usp=sharing)
4. CodeLlama 34b 2x faster [A100 on Colab](https://colab.research.google.com/drive/1y7A0AxE3y8gdj4AVkl2aZX47Xu3P1wJT?usp=sharing)
5. Mistral 7b [free Kaggle version](https://www.kaggle.com/code/danielhanchen/kaggle-mistral-7b-unsloth-notebook)
6. We also did a [blog](https://huggingface.co/blog/unsloth-trl) with 🤗 HuggingFace, and we're in the TRL [docs](https://huggingface.co/docs/trl/main/en/sft_trainer#accelerate-fine-tuning-2x-using-unsloth)!
7. `ChatML` for ShareGPT datasets, [conversational notebook](https://colab.research.google.com/drive/1Aau3lgPzeZKQ-98h69CCu1UJcvIBLmy2?usp=sharing)
8. Text completions like novel writing [notebook](https://colab.research.google.com/drive/1ef-tab5bhkvWmBOObepl1WgJvfvSzn5Q?usp=sharing)
9. [**NEW**] We make Phi-3 Medium / Mini **2x faster**! See our [Phi-3 Medium notebook](https://colab.research.google.com/drive/1hhdhBa1j_hsymiW9m-WzxQtgqTH_NHqi?usp=sharing)

<div class="align-center">
  <a href="https://github.com/unslothai/unsloth"><img src="https://github.com/unslothai/unsloth/raw/main/images/unsloth%20new%20logo.png" width="115"></a>
  <a href="https://ollama.com/"><img src="https://raw.githubusercontent.com/unslothai/unsloth/nightly/images/ollama.png" height="44"></a>
  <a href="https://discord.gg/u54VK8m8tk"><img src="https://github.com/unslothai/unsloth/raw/main/images/Discord button.png" width="145"></a>
  <a href="https://ko-fi.com/unsloth"><img src="https://github.com/unslothai/unsloth/raw/main/images/Kofi button.png" width="145"></a></a> Join Discord if you need help + ⭐ <i>Star us on <a href="https://github.com/unslothai/unsloth">Github</a> </i> ⭐
</div>
"""