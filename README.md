# my_skill_wow

个人 Codex Skills 集合仓库。每个 Skill 独立安装，不需要下载整个仓库。

## Skill 目录

| Skill | 用途 | 源码 | 安装 |
|---|---|---|---|
| `weekly-research-report` | 生成计算机研究生 HTML 周报 | [查看](./skills/weekly-research-report/) | [跳到命令](#weekly-research-report) |
| `manage-skill-repository` | 维护本仓库：新增、校验、更新和发布 Skill | [查看](./skills/manage-skill-repository/) | [跳到命令](#manage-skill-repository) |

## 按需安装

下面每条命令只会安装指定 Skill 到 `~/.codex/skills/`。在 GitHub 代码块右上角点击复制按钮，然后在终端执行。

### weekly-research-report

用于根据小论文、大论文、实验和下周计划生成简洁的 HTML 工作报告。

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo GUZZzz1/my_skill_wow \
  --path skills/weekly-research-report
```

### manage-skill-repository

仓库维护者使用。安装后，可以让 Codex 按仓库规则新增或更新 Skill。

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
└── skills/
    ├── weekly-research-report/
    │   ├── SKILL.md
    │   ├── agents/
    │   ├── assets/
    │   └── references/
    └── manage-skill-repository/
        ├── SKILL.md
        └── agents/
```

## 使用说明

- 每个 Skill 必须放在 `skills/<skill-name>/` 下。
- 每个 Skill 必须有自己的 `SKILL.md`。
- 仓库根目录只放集合说明和仓库级配置，不把多个 Skill 合并成一个。
- 首次安装时，如果本地已存在同名 Skill，安装器会停止，不会直接覆盖。
