# Лабораторные работы по курсу "GUI Design Fundamentals".

Основы проектирования графического интерфейса компьютерных систем

*Выполнила*: Рудинская Елизавета, группа 6231-010402D


### Лабораторная работа 1: [GUI_Lab1](https://github.com/Small-Fiend/GUI/blob/main/GUI_Lab1.py)
Задача: Реализовать программу, отображающую графический интерфейс окна Windows.

Реализация должна содержать кнопку и лэйбл. При нажатии кнопки происходит изменение в лэйбл.

Язык: Python

### Лабораторная работа 2: [GUI_Lab2](https://github.com/Small-Fiend/GUI/blob/main/GUI_Lab2.py)
Задача: Реализовать приложение на PyQt с использованием сигнал-слот взаимодействия.

Например, приложение генератор курсов валют на торговом рынке, хранящий три связанных курса: рубль –доллар и котировку текущей стоимости нефти. При увеличении стоимости нефти рубль увеличивает стоимость => посылается сигнал «классу «рубля»». При уменьшении стоимости нефти доллар увеличивает стоимость => посылается сигнал «классу «доллара»». Курсы доллара и рубля связаны между собой коэффициентом и изменяются, например, 2, любой. Все изменения делать при нажатии на кнопку анализ.

Язык: Python

### Лабораторная работа 3: [GUI_Lab3](https://github.com/Small-Fiend/GUI/blob/main/GUI_Lab3.py)
Задача: Реализовать приложение на PyQt с использованием представления таблиц и работы с SQL.

В меню две вкладки: Set connection (установить соединение с бд), Close connection (очистить все, закрыть соединение с бд).
По умолчанию можно сделать в QTabWidget вкладки пустыми, либо создавать их по выполнению запросов при нажатии на функциональные клавиши.
Сразу после успешного коннета в Tab1 устанавливается таблица, соответствующая запросу «SELECT * FROM sqlite_master».
Кнопка bt1 делает выборочный запрос, например, «SELECT name FROM sqlite_master», результат выводится в Tab2.
При выборе колонки из выпадающего списка QComboBox результат соотвествующего запроса отправляется в Tab3.
Кнопки bt2 и bt3 выполняют запрос по выводу таблицы в Tab4 и Tab5

Язык: Python

