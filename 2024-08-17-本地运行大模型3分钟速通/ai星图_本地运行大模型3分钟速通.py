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
"""AI星图-本地运行大模型3分钟速通
发布时间: 2024-08-17

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TIp84ZOPed43iVD-yzxYlubs1og1Ggth

**欢迎来到AI星图**

本期课程，介绍如何在本地快速运行大模型。并通过设置指令，让大模型具备自我认知。

### 1. 下载 Ollama
 - 打开 Ollama 官网：`ollama.com`
 - 点击 **Downloads** 按钮
 - Ollama 支持 Mac、Linux 和 Windows 平台

### 2. 安装 Ollama
 - 运行下载的 Ollama 安装文件
 - 按照提示进行安装，建议选择默认设置

### 3. 运行大模型
 - **Mac 用户**: 按下 ***command + 空格键*** 打开 聚焦，输入 `Terminal` 打开终端
 - **Windows 用户**: 按下 ***Win 键***，输入 `cmd` 打开命令提示符
 - 选择大模型
 - 在终端或命令提示符中，输入以下命令，启动指定的大模型：
   ```bash
   ollama run llama3.1:8b-instruct-q4_K_M
   ```
 - Ollama 将自动下载指定的大模型文件，约 4.9GB
 - 下载完成后，您可以直接在终端或命令提示符中与大模型进行对话

### 4. 与大模型对话
 - 输入: `你是谁？`

### 5. 进阶与高级用法
 - 设置系统角色：
   ```bash
   /set system 你是AI星图，探索AI宇宙。
   ```
 - 输入: `你是谁？`

### 结语

通过以上步骤，您可以轻松启动并使用大模型。如果您想进一步探索高级功能，可以继续关注我们的课程内容。

本期视频做到这里，欢迎大家点赞关注、收藏和转发。欢迎加入我们的社群，本期课程涉及到的代码，我会放到视频下方的链接。

谢谢大家的观看！
"""