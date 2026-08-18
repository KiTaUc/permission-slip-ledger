# Permission Slip Ledger

**Permission Slip Ledger** — автономный локальный инструмент для сферы «Образование». Показывает, какие согласия на мероприятие получены, а кому требуется напоминание.

## Возможности

Программа хранит записи в обычном JSON-файле, проверяет обязательные поля и допустимые статусы, а затем выводит сводку по статусам. Запуск не требует учётной записи, внешнего API или фоновой передачи данных.

## Быстрый старт

```bash
python src/permission_slip_ledger.py --store data/records.json add --student-code "P-14" --event "Музей" --due-on "2026-08-29" --status "sent"
python src/permission_slip_ledger.py --store data/records.json report
```

## Проверка

```bash
python -m unittest discover -s tests -v
python -m compileall src
```

## Ограничения

Это рабочий журнал для организационных задач, а не замена профильному программному обеспечению, юридической документации, медицинской системе или системе расчётов.
