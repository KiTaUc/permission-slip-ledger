# Permission Slip Ledger

Локальный учёт согласий на мероприятия: добавление, отметка о получении и список просроченных напоминаний.

```bash
python src/permission_slip_ledger.py --store data/slips.json add --student-code P-14 --event Музей --due-on 2026-08-29
python src/permission_slip_ledger.py --store data/slips.json reminders --today 2026-08-29
```
