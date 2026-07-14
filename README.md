# my_skill_wow

个人 Codex Skills 集合仓库。每个 Skill 独立安装，不需要下载整个仓库。

## 在线预览

### 研究生周报

`weekly-research-report` 的通用 HTML 模板。页面中的 `{{...}}` 是待替换字段，生成实际周报时会根据用户信息替换。

[查看 HTML 模板](https://guzzzz1.github.io/my_skill_wow/weekly-research-report-template.html)

## Skill 目录

<table>
  <thead>
    <tr>
      <th>中文名</th>
      <th>Skill</th>
      <th>用途</th>
      <th>源码</th>
      <th>安装</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>研究生周报</td>
      <td><code>weekly-research-report</code></td>
      <td>生成研究生 HTML 周报</td>
      <td><a href="./skills/weekly-research-report/"><code>查看完整源码</code></a></td>
      <td><a href="#weekly-research-report"><code>查看安装方式</code></a></td>
    </tr>
    <tr>
      <td>Skill 评估</td>
      <td><code>evaluate-skill-quality</code></td>
      <td>8 维设计评分与上线准入</td>
      <td><a href="./skills/evaluate-skill-quality/"><code>查看完整源码</code></a></td>
      <td><a href="#evaluate-skill-quality"><code>查看安装方式</code></a></td>
    </tr>
    <tr>
      <td>Skill 仓库维护</td>
      <td><code>manage-skill-repository</code></td>
      <td>新增或修改 Skill</td>
      <td><a href="./skills/manage-skill-repository/"><code>查看完整源码</code></a></td>
      <td><a href="#manage-skill-repository"><code>查看安装方式</code></a></td>
    </tr>
  </tbody>
</table>

## 按需安装

推荐直接复制“Codex 安装提示词”并发送给 Codex，由 Codex 调用系统自带的 `$skill-installer` 完成安装。也可使用后面的终端命令手动安装。

两种方式都只会安装选中的 Skill，不需要克隆整个仓库。

### weekly-research-report

用于根据小论文、大论文、实验和下周计划生成简洁的 HTML 工作报告。

**方式一：复制到 Codex（推荐）**

```text
请使用 $skill-installer 从 GitHub 仓库 GUZZzz1/my_skill_wow 安装 skills/weekly-research-report。只安装这一个 Skill，不要克隆或安装整个仓库。如果网络访问需要授权，请向我申请。安装完成后告诉我安装路径，并说明它会从下一个任务开始可用。
```

**方式二：终端命令**

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo GUZZzz1/my_skill_wow \
  --path skills/weekly-research-report
```

### evaluate-skill-quality

用于评估新建或已有 Skill。固定 8 维评分用于判断设计质量；动态业务维度用于判断业务适配；六道工程门与 E0-E4 证据等级用于判断是否达到 `DESIGN_PASS`、`TEST_PASS` 或 `RELEASE_READY`。需要时可执行独立评分、分歧互审和仲裁。评测闭环通过真实测试和回归证据体现，不作为第 9 个加权维度。

固定 8 维及交叉评估方法源自 MIT 许可的 [`sunxingboo/skill-evaluator`](https://github.com/sunxingboo/skill-evaluator)；工程准入层是本仓库扩展。该方法不是 OpenAI 官方评分标准。[查看标准来源与边界](./skills/evaluate-skill-quality/references/standard-basis.md)。

**方式一：复制到 Codex（推荐）**

```text
请使用 $skill-installer 从 GitHub 仓库 GUZZzz1/my_skill_wow 安装 skills/evaluate-skill-quality。只安装这一个 Skill，不要克隆或安装整个仓库。如果网络访问需要授权，请向我申请。安装完成后告诉我安装路径，并说明它会从下一个任务开始可用。
```

**方式二：终端命令**

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo GUZZzz1/my_skill_wow \
  --path skills/evaluate-skill-quality
```

### manage-skill-repository

仓库维护者使用。安装后，可以让 Codex 新增 Skill 或修改已有 Skill，并完成结构校验、质量评估、README 更新、提交和推送。

**方式一：复制到 Codex（推荐）**

```text
请使用 $skill-installer 从 GitHub 仓库 GUZZzz1/my_skill_wow 安装 skills/manage-skill-repository。只安装这一个 Skill，不要克隆或安装整个仓库。如果网络访问需要授权，请向我申请。安装完成后告诉我安装路径，并说明它会从下一个任务开始可用。
```

**方式二：终端命令**

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo GUZZzz1/my_skill_wow \
  --path skills/manage-skill-repository
```

安装完成后，在 Codex 的下一个任务中使用对应 Skill。

## 仓库结构

```text
my_skill_wow/
├── README.md
├── docs/
│   └── weekly-research-report-template.html
└── skills/
    ├── weekly-research-report/
    │   ├── SKILL.md
    │   ├── agents/
    │   ├── assets/
    │   └── references/
    ├── evaluate-skill-quality/
    │   ├── SKILL.md
    │   ├── LICENSE
    │   ├── agents/
    │   ├── references/
    │   └── scripts/
    └── manage-skill-repository/
        ├── SKILL.md
        ├── agents/
        └── references/
```

## 使用说明

- 每个 Skill 必须放在 `skills/<skill-name>/` 下。
- 每个 Skill 必须有自己的 `SKILL.md`。
- 仓库根目录只放集合说明和仓库级配置，不把多个 Skill 合并成一个。
- 首次安装时，如果本地已存在同名 Skill，安装器会停止，不会直接覆盖。
