# Contributing

Contributions should make `commit-roast` more useful for real code review, not just louder.

## Good Contributions

- Better review checklists for specific stacks.
- More realistic bilingual examples.
- Safer or more portable helper scripts.
- Clearer severity guidance.
- Tone improvements that stay professional.

## Ground Rules

- Roast the code, never the person.
- Do not add fake findings for comedy.
- Keep `SKILL.md` focused; put long material in `references/`.
- Test scripts before submitting changes.
- Preserve Chinese and English usability.

## Local Validation

```bash
PYTHONUTF8=1 python path/to/quick_validate.py .
python scripts/collect_diff_context.py --mode auto
```

On Windows PowerShell:

```powershell
$env:PYTHONUTF8='1'
python path\to\quick_validate.py .
python scripts\collect_diff_context.py --mode auto
```
