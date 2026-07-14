# 评估标准的来源与边界

## 1. 上游来源

固定 8 维设计评分源自开源项目 [`sunxingboo/skill-evaluator`](https://github.com/sunxingboo/skill-evaluator)：

- 本地核对版本：上游 `main` 的 commit `b50fd8f9f10fe4269537ee4a0954ee6f023b4620`（上游 changelog 标记为 `v2.2.0`，2026-04-15）。
- 直接依据：上游 `references/dimensions.md`、`SKILL.md`、`references/prompts.md` 和 `references/report-formats.md`。
- 上游作者：`sunxingboo`。
- 上游许可证：MIT；本 Skill 保留的许可证副本见 [`../LICENSE`](../LICENSE)。

上游仓库明确采用 8 个维度，而不是 9 个：

- D1-D4 各占 `15%`。
- D5-D8 各占 `10%`。
- 每维按 `0-10` 分评价。
- 等级阈值为 `S >= 9.0`、`A >= 7.5`、`B >= 6.0`、`C >= 4.0`，否则为 `D`。
- D6 在 Skill 确实不需要附带资源时标为 `N/A`，按 `7` 分基线计入总分。

固定 8 维用于比较 Skill 的设计质量，不等于完成真实测试或上线验收。

## 2. 上游已有能力

除固定 8 维外，上游还提供：

- 单个和多个 Skill 的评分与横向比较。
- 多评估者独立评分、对分差至少 `2` 分的维度交叉审查，再由仲裁者形成最终分数。
- 无并行评估能力时的串行多视角回退。

本仓库保留这套交叉评估思想，但不把“多个模型给出相近分数”视为真实功能测试或上线证据。

## 3. 本仓库的工程扩展

以下内容不是上游固定 8 维标准，而是本仓库为“上线准入”增加的工程层：

- 动态业务验收维度。
- G1-G6 六道工程门。
- E0-E4 证据等级。
- `BLOCKED / NEEDS_REVISION / DESIGN_PASS / TEST_PASS / RELEASE_READY` 最终状态。
- D1/D2/D4/D5 不低于 `6.0` 的关键维度门槛。

分层关系如下：

- 固定 8 维回答“设计质量如何”。
- 动态业务维度回答“是否适配当前业务”。
- 六道工程门和 E0-E4 回答“证据支持到什么成熟度”。
- 最终状态回答“当前最高可声明到哪一层”。

## 4. Skill 结构参考

OpenAI 系统 `skill-creator` 用于校对 Skill 的结构和组织方式，包括：

- `SKILL.md` 的 `name/description` 元数据。
- `agents/openai.yaml` 界面元数据。
- `references/`、`scripts/`、`assets/` 的渐进式加载。
- 资源引用、脚本测试和 `quick_validate.py` 结构校验。

`skill-creator` 没有定义固定 8 维权重、S/A/B/C/D 分级或本仓库的最终准入状态。

## 5. 不采用 D9 加权

“评测闭环 / 可验证性”很重要，但本仓库不将其作为 D9 加入固定总分。它通过以下机制体现：

- 应触发 / 不应触发 query。
- 正常、缺失、超长、多对象和失败 case。
- 新旧版或有无 Skill 对照。
- G6 回归门。
- E0-E4 证据等级。

## 6. 对外表述

应表述为“基于 `sunxingboo/skill-evaluator` 8 维评分、并增加本仓库工程准入层的方法”。不应表述为 OpenAI 官方的 8 维或 9 维评分标准，也不应把本仓库扩展归因于上游作者。
