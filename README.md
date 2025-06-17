# For lesson_10
##Команды для запуска отчета Allure

**cd lesson_10
pytest --alluredir allure-result
pytest lesson_10/test_reshop_recalc.py--alluredir=lesson_10/allure-result
allure serve lesson_10/allure-result**
