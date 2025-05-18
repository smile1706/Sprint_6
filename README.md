## Финальный проект 6 спринта
<hr>

## Студент: Муталлапов Динар

## <h>Когорта: #21</h>
<hr>

## <h>Project: Самокат</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты и записать отчет:</h>

> python -m pytest --alluredir=./allure-results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve ./allure-results


<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла      | Содержание файла                   |
|---------------------|------------------------------------|
| Tests dir           | Директория с тестами               |
| locators dir        | Директория с локаторами            |
| pages dir           | Директория с Page Object           |
| allure_results dir  | Папка с отчетами Allure            |
| conftest.py         | Фикстуры                           |
| helpers.py          | Хэлпер/генератор для тела запросов |
| data.py             | Файл с данными                     |
| curl.py             | Файл с URL                         |
| requirements.txt    | Файл с зависимостями               |


