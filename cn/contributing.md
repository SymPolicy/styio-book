# 版本、示例来源与贡献

这是供更新本书或复现示例结果时使用的附录。阅读和使用 Styio 不要求先理解编译器模块、维护门禁或发布流程。

## 适用版本

当前使用说明与 cookbook 对应下游 compiler commit `fd3b3e2d9a900fa58bc70641a42885c991650210`。这是源码兼容边界，不表示上游 release 或任意已安装的 `0.0.1` 二进制都具备相同能力。

示例已在该语言源码加 `85e41b90c7231b8a263b5b2c88f17fbd5833a078` 构建候选上执行：后者只修改 CMake、维护路由、测试和文档，没有修改 C++ 语言实现。构建为 GCC 14、LLVM 18.1.8、Release、Tree-sitter 开启、ICU 关闭。可执行文件 SHA-256：`2b0120e9a066dfdfc9f20cade97fdac5af9953f74e3780bd61952d9874d7c3a0`。

6 个正例和 3 个负例均符合预期，12 处中英文引用片段与固定版本源码一致。这是 cookbook 的功能验证，不表示整个编译器测试集或发布门禁全部通过。

## 可追溯来源

- [当前语法地图](https://github.com/Unka-Malloc/styio-nightly/blob/fd3b3e2d9a900fa58bc70641a42885c991650210/docs/design/syntax/ACTIVE-SYNTAX.md)
- [语法功能说明](https://github.com/Unka-Malloc/styio-nightly/blob/fd3b3e2d9a900fa58bc70641a42885c991650210/docs/design/syntax/features/README.md)
- [标准库范围](https://github.com/Unka-Malloc/styio-nightly/blob/fd3b3e2d9a900fa58bc70641a42885c991650210/library/README.md)

完整程序、stdin、expected 和哈希登记在本书仓库的 `cookbook/cases.json`。验证器读取固定 commit 中的文件，不复制一套算法语料。文件转换用例只将原来的 `/tmp/styio_doubled.txt` 适配为独立临时目录内的 `doubled.txt`；预期字节仍是 `204060`。

## 复现

在书籍仓库根目录，设置 `STYIO_SOURCE` 为包含目标 commit 的编译器 checkout，`STYIO_BIN` 为已知构建来源的可执行文件：

```bash
python3 scripts/check_docs.py
python3 scripts/verify_examples.py --source "$STYIO_SOURCE" --check-only
python3 scripts/verify_examples.py --source "$STYIO_SOURCE" --styio-bin "$STYIO_BIN" --run --build-label "<compiler commit and build-only patch>"
python3 -m unittest discover -s scripts -p 'test_*.py'
```

静态核对不会声称运行通过。运行报告单列正反例结果、退出码和可执行文件指纹；负例必须按预期诊断被拒绝，崩溃不算通过。`--build-label` 是调用者的来源声明，指纹本身不证明构建来源。

## 更新本书

先选择新编译器版本，再一起更新中英文说明、来源、哈希与预期结果，执行正反例并检查 HTML。不可执行时明确记录为未运行，不沿用旧版本的通过结论。当前说明持续反映已验证行为；设计理由与未定方案留在[历史资料](legacy-index.md)，版本变更由 Git 记录。

本书的正文面向写 Styio 程序的使用者。编译器内部模块和开发流程属于独立的 [styio-dev-doc](https://github.com/SymPolicy/styio-dev-doc)。

[返回使用说明](README.md)
