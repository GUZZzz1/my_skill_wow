# 发布检查清单

## 1. 范围与 Git

- 确认变更目标、受影响 Skill 和不应纳入的用户改动。
- 检查 `git status --short --branch`、分支、远程、上游和本地/远程差异。
- 发布前获取或比较远程状态；存在分歧时停止，不自动覆盖。

## 2. Skill 包验证

- 运行 `quick_validate.py` 并保留结果。
- 核对 `SKILL.md` 与 `agents/openai.yaml`。
- 检查所有直接引用的 `references/scripts/assets/examples`。
- 脚本至少运行一个正常 case 和一个安全失败 case；高风险脚本在隔离环境测试。
- 模板/资产按类型执行解析、渲染或打开检查。

## 3. 评估与安全

- 使用 `evaluate-skill-quality` 输出固定 8 维设计分、动态业务验收、六道工程门、证据等级和最终状态。
- 只有 `RELEASE_READY` 可表述为已具备发布证据；`DESIGN_PASS` 只代表设计通过，`TEST_PASS` 仍不代表已完成目标平台验证。
- 扫描凭据、私钥、个人信息、本地绝对路径、未替换占位符和私人原始文件。
- 检查新依赖、执行权限、网络访问、外部写操作和许可证影响。

## 4. README 与安装

- 更新目录行、源码链接、说明、AI 编程 Agent 安装提示词和 macOS/Linux、Windows 终端命令。
- 校验用户级与工作区级目录约定；Codex/通用 Agent Skills 使用 `.agents/skills`，Claude Code 使用 `.claude/skills`。
- 运行安装器的目标路径解析、非法输入、已有目录拒绝、直接下载与 Git sparse checkout 降级，并完成至少一个真实下载 case。
- 临时目录安装验证：只安装指定 Skill，目录名正确，包内文件完整。
- 已安装同名 Skill 的升级方式必须明确，不覆盖用户本地修改。

## 5. 提交与远程确认

- 用 `git diff --check` 检查格式，查看完整 diff 和变更统计。
- 显式 stage 范围内文件，不默认纳入其他改动。
- 提交信息说明实际变更。
- 推送后核对远程分支 commit ID。
- 记录发布前 commit，便于发布后定位变更。
