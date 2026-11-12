# ModSAPI 文档同步

需要 Python 3.10 或更新版本。同步器读取维护包的源码与声明，不执行游戏模块。

```powershell
python scripts/modsapi-docs/generate.py --source-root "<ModSAPI项目目录>" --site-root "." --stage-root "<临时输出目录>"
python scripts/modsapi-docs/generate.py --source-root "<ModSAPI项目目录>" --site-root "." --stage-root "<临时输出目录>" --apply
npm run build
```

先生成，再检查临时目录中的 manifest.json 和页面，最后 --apply。应用会核对目标文件原哈希，遇到生成后被修改的文件会停止；修改前的文件保存在临时目录 original/。

content.py 保存人工编写的场景指南、核心示例与能力限制。translations.zh-CN.json 与 localization.py 保存中文译文及重复事件契约的翻译规则；缺少译文时停止生成。references.py 解析嵌套类型和正文引用；无法解析的类型会阻止生成。源码的英文注释不受文档语言影响。自动参考页的签名来自当前实现；声明提供类型线索，不能代替原生行为验证。修改这些参考页时应同步更新同步器或模板，否则下次生成会覆盖手写变更。
