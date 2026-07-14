# my_skill_wow

个人 Agent Skills 集合仓库。每个 Skill 都可独立安装，不需要完整克隆或安装整个仓库。

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

推荐把安装提示词发给 Codex、Claude Code 或其他支持 Agent Skills 的 AI 编程 Agent，让它识别自己的标准目录并完成安装。也可以使用后面的跨平台终端方式，把 Skill 安装到当前工作区。

两种方式都只下载选中的 Skill。AI 自动安装可直接下载目标目录，并在 GitHub API 不可用时降级为 Git sparse checkout；终端方式从一开始就使用 sparse checkout，只检出安装器和所选 Skill。目标目录已经存在时应先比较版本，不要直接覆盖。

目录约定：Codex 与通用 Agent Skills 的用户级目录为 `<用户主目录>/.agents/skills`，项目级目录为 `<工作区>/.agents/skills`；Claude Code 的对应目录为 `<用户主目录>/.claude/skills` 和 `<工作区>/.claude/skills`。项目中的 `.codex` 是 Codex 配置目录，不作为项目级 Skill 目录。

### weekly-research-report

用于根据小论文、大论文、实验和下周计划生成简洁的 HTML 工作报告。

**方式一：交给 AI 编程 Agent 自动安装（推荐）**

```text
请从 GitHub 仓库 GUZZzz1/my_skill_wow 只安装 skills/weekly-research-report，不要完整克隆或安装整个仓库。

先识别你当前运行的 AI 编程 Agent 及其实际支持的 Skill 目录，不要臆造路径。自动模式下，直接安装到该 Agent 的用户级标准目录，供我的所有工作区使用：Codex 或通用 Agent Skills 使用用户主目录中的 `.agents/skills`，Claude Code 使用用户主目录中的 `.claude/skills`，其他 Agent 遵循自身官方约定。无法判断当前 Agent 或存在多个有效目录时，先给出建议路径并询问我。

优先使用仓库提供的 `scripts/install-skill.py`，以 `--scope user` 和识别到的 `--agent` 参数安装；也可以使用当前 Agent 的等价原生安装方式，但最终目录必须符合上面的约定。只下载目标 Skill 子目录。目标目录已存在时不要覆盖，先说明现有版本与仓库版本的差异并询问我。安装后检查 SKILL.md 是否存在，告诉我实际安装路径，并说明是否需要新建任务或重新加载 Agent。
```

**方式二：安装到当前工作区（终端）**

在工作区内执行，需要 Git 与 Python 3。命令先把安装器和目标 Skill 稀疏检出到系统临时目录，再安装到最近的 Git 工作区根目录；当前目录不在 Git 仓库内时，就安装到当前目录。`--agent auto` 按 `.agents`、`.codex`、`.claude` 的顺序识别环境；`.codex` 只作为 Codex 环境信号，实际仍安装到官方项目级目录 `.agents/skills`。无法识别时也使用开放约定 `.agents/skills`。

macOS / Linux：

```bash
installer_dir="$(mktemp -d)"
git clone --depth 1 --filter=blob:none --sparse https://github.com/GUZZzz1/my_skill_wow.git "$installer_dir/my_skill_wow"
git -C "$installer_dir/my_skill_wow" sparse-checkout set scripts skills/weekly-research-report
python3 "$installer_dir/my_skill_wow/scripts/install-skill.py" --skill weekly-research-report --source-root "$installer_dir/my_skill_wow" --scope workspace --agent auto
```

Windows PowerShell：

```powershell
$installerDir = Join-Path $env:TEMP ("my-skill-wow-" + [guid]::NewGuid())
git clone --depth 1 --filter=blob:none --sparse https://github.com/GUZZzz1/my_skill_wow.git "$installerDir/my_skill_wow"
git -C "$installerDir/my_skill_wow" sparse-checkout set scripts skills/weekly-research-report
py "$installerDir/my_skill_wow/scripts/install-skill.py" --skill weekly-research-report --source-root "$installerDir/my_skill_wow" --scope workspace --agent auto
```

Windows 未提供 `py` 命令时，将上面的 `py` 改为 `python`。

### evaluate-skill-quality

用于评估新建或已有 Skill。固定 8 维评分用于判断设计质量；动态业务维度用于判断业务适配；六道工程门与 E0-E4 证据等级用于判断是否达到 `DESIGN_PASS`、`TEST_PASS` 或 `RELEASE_READY`。需要时可执行独立评分、分歧互审和仲裁。评测闭环通过真实测试和回归证据体现，不作为第 9 个加权维度。

固定 8 维及交叉评估方法源自 MIT 许可的 [`sunxingboo/skill-evaluator`](https://github.com/sunxingboo/skill-evaluator)；工程准入层是本仓库扩展。该方法不是 OpenAI 官方评分标准。[查看标准来源与边界](./skills/evaluate-skill-quality/references/standard-basis.md)。

**方式一：交给 AI 编程 Agent 自动安装（推荐）**

```text
请从 GitHub 仓库 GUZZzz1/my_skill_wow 只安装 skills/evaluate-skill-quality，不要完整克隆或安装整个仓库。

先识别你当前运行的 AI 编程 Agent 及其实际支持的 Skill 目录，不要臆造路径。自动模式下，直接安装到该 Agent 的用户级标准目录，供我的所有工作区使用：Codex 或通用 Agent Skills 使用用户主目录中的 `.agents/skills`，Claude Code 使用用户主目录中的 `.claude/skills`，其他 Agent 遵循自身官方约定。无法判断当前 Agent 或存在多个有效目录时，先给出建议路径并询问我。

优先使用仓库提供的 `scripts/install-skill.py`，以 `--scope user` 和识别到的 `--agent` 参数安装；也可以使用当前 Agent 的等价原生安装方式，但最终目录必须符合上面的约定。只下载目标 Skill 子目录。目标目录已存在时不要覆盖，先说明现有版本与仓库版本的差异并询问我。安装后检查 SKILL.md 是否存在，告诉我实际安装路径，并说明是否需要新建任务或重新加载 Agent。
```

**方式二：安装到当前工作区（终端）**

macOS / Linux：

```bash
installer_dir="$(mktemp -d)"
git clone --depth 1 --filter=blob:none --sparse https://github.com/GUZZzz1/my_skill_wow.git "$installer_dir/my_skill_wow"
git -C "$installer_dir/my_skill_wow" sparse-checkout set scripts skills/evaluate-skill-quality
python3 "$installer_dir/my_skill_wow/scripts/install-skill.py" --skill evaluate-skill-quality --source-root "$installer_dir/my_skill_wow" --scope workspace --agent auto
```

Windows PowerShell：

```powershell
$installerDir = Join-Path $env:TEMP ("my-skill-wow-" + [guid]::NewGuid())
git clone --depth 1 --filter=blob:none --sparse https://github.com/GUZZzz1/my_skill_wow.git "$installerDir/my_skill_wow"
git -C "$installerDir/my_skill_wow" sparse-checkout set scripts skills/evaluate-skill-quality
py "$installerDir/my_skill_wow/scripts/install-skill.py" --skill evaluate-skill-quality --source-root "$installerDir/my_skill_wow" --scope workspace --agent auto
```

### manage-skill-repository

仓库维护者使用。安装后，可以让 AI 编程 Agent 新增或修改 Skill，并完成结构校验、质量评估、README 更新、提交和推送。

**方式一：交给 AI 编程 Agent 自动安装（推荐）**

```text
请从 GitHub 仓库 GUZZzz1/my_skill_wow 只安装 skills/manage-skill-repository，不要完整克隆或安装整个仓库。

先识别你当前运行的 AI 编程 Agent 及其实际支持的 Skill 目录，不要臆造路径。自动模式下，直接安装到该 Agent 的用户级标准目录，供我的所有工作区使用：Codex 或通用 Agent Skills 使用用户主目录中的 `.agents/skills`，Claude Code 使用用户主目录中的 `.claude/skills`，其他 Agent 遵循自身官方约定。无法判断当前 Agent 或存在多个有效目录时，先给出建议路径并询问我。

优先使用仓库提供的 `scripts/install-skill.py`，以 `--scope user` 和识别到的 `--agent` 参数安装；也可以使用当前 Agent 的等价原生安装方式，但最终目录必须符合上面的约定。只下载目标 Skill 子目录。目标目录已存在时不要覆盖，先说明现有版本与仓库版本的差异并询问我。安装后检查 SKILL.md 是否存在，告诉我实际安装路径，并说明是否需要新建任务或重新加载 Agent。
```

**方式二：安装到当前工作区（终端）**

macOS / Linux：

```bash
installer_dir="$(mktemp -d)"
git clone --depth 1 --filter=blob:none --sparse https://github.com/GUZZzz1/my_skill_wow.git "$installer_dir/my_skill_wow"
git -C "$installer_dir/my_skill_wow" sparse-checkout set scripts skills/manage-skill-repository
python3 "$installer_dir/my_skill_wow/scripts/install-skill.py" --skill manage-skill-repository --source-root "$installer_dir/my_skill_wow" --scope workspace --agent auto
```

Windows PowerShell：

```powershell
$installerDir = Join-Path $env:TEMP ("my-skill-wow-" + [guid]::NewGuid())
git clone --depth 1 --filter=blob:none --sparse https://github.com/GUZZzz1/my_skill_wow.git "$installerDir/my_skill_wow"
git -C "$installerDir/my_skill_wow" sparse-checkout set scripts skills/manage-skill-repository
py "$installerDir/my_skill_wow/scripts/install-skill.py" --skill manage-skill-repository --source-root "$installerDir/my_skill_wow" --scope workspace --agent auto
```

如需明确指定目录，可追加 `--dest <Skill 父目录>`；如需安装为当前用户全局可用，可改为 `--scope user --agent codex` 或 `--scope user --agent claude`。临时稀疏仓库可以在安装后删除，不影响已安装的 Skill。

安装完成后，新建任务或重新加载 AI 编程 Agent，再使用对应 Skill。

## 仓库结构

```text
my_skill_wow/
├── README.md
├── docs/
│   └── weekly-research-report-template.html
├── scripts/
│   └── install-skill.py
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
