Порівняння алгоритмів

Greedy алгоритм
✅ Підхід: Завжди бере найбільший доступний номінал.
✅ Складність: O(n \* k), де n — кількість монет, k — кількість номіналів (дуже швидкий на практиці, бо k мале).
✅ Особливість: працює добре для стандартного набору монет (50, 25, 10, 5, 2, 1), але може давати не мінімальну кількість монет для складних наборів (наприклад, [9, 6, 1]).

Dynamic Programming алгоритм
✅ Підхід: Будує оптимальні рішення для всіх підсум до amount.
✅ Складність: O(n \* k), але з більшими накладними витратами на пам'ять (масиви довжини amount).
✅ Особливість: гарантує мінімальну кількість монет для будь-якого набору номіналів.
✅ Приклад, де DP кращий: coins = [9, 6, 1], amount = 11

Greedy дасть {9:1, 1:2} (3 монети), а DP дасть {6:1, 1:5} (6 монет) або інший варіант — залежить від монет.

Висновки:

⚡Жадібний алгоритм працює швидше, але не завжди оптимально.
⚡Динамічне програмування гарантує найкращий результат, але працює повільніше.
⚡Для касових апаратів або банкоматів із фіксованими номіналами — можна сміливо застосовувати жадібний підхід.
⚡Для великих сум жадібний алгоритм набагато швидший.
⚡Для універсального рішення — обирайте динамічне програмування.
