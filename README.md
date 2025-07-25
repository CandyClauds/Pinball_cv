# AirPong - Пинбол с управлением жестами
Мультиплеерная игра в стиле пинбол, в которой игроки управляют платформами с помощью движений рук перед камерой.
Поднимите руку — платформа движется вверх, опустите — вниз. Соревнуйтесь с другом в динамичной битве!


# 🎮 Функциональность
Двухпользовательский режим: Левый игрок (синяя зона) vs Правый игрок (красная зона)

Интуитивное управление: Вертикальные движения рук = движение платформы вверх/вниз

Счёт очков: Забитый мяч приносит очко сопернику

Автоматический перезапуск: Мяч автоматически запускается после гола

Визуальная обратная связь: Цветовые индикаторы и трекинг рук

# ⚙️ Установка и запуск
Клонируйте репозиторий:

```bash
git clone https://github.com/CandyClauds/Pinball_cv.git
cd Pinball_cv
```

Установите зависимости:
```bash
pip install -r requirements.txt
```

Запустите игру:

```bash
python pinball.py.py
```
Настройка позиции:

Игрок 1: Встаньте слева от камеры, работайте левой рукой

Игрок 2: Встаньте справа, работайте правой рукой

Отрегулируйте высоту: руки должны перемещаться от низа до верха кадра

# 🧩 Технологии
`Python 3.10` — язык, на котором реализована логика игры

`OpenCV` — захват видео с камеры и обработка изображения в реальном времени

`MediaPipe Hands` — обнаружение и отслеживание положения рук с помощью 21 ключевой точки

`NumPy` — математические вычисления для движения мяча и коллизий

`Pygame` — визуализация игрового поля, анимации и управление игровым циклом

# 🚀 Планы развития
Добавление звукового сопровождения и фоновой музыки

Реализация бонусных игровых механик ("power-ups"), включая ускорение мяча и изменение размера платформ

Поддержка онлайн-режима с возможностью подключения удалённых игроков через веб-камеру

Введение уровней с возрастающей сложностью

Система учёта рекордов и отображения турнирной таблицы

Расширение набора жестов, включая вращательные движения кисти для изменения траектории мяча

## Проект остаётся в стадии активного развития.
В планах — доработка игрового процесса, улучшение пользовательского опыта и возможная интеграция сетевой многопользовательской версии.

