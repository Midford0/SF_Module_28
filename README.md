Проводилось тестирование пользовательского интерфейса c с элементами позитивного и негативного функциогального тестирования исходя из представленных требований c помощью программной библиотеки Selenium WebDriver и фреймворка pytest . Использовн PageObject шаблон проектирования.
Список тест-кейсов, чек-лист и баги представлены в файле “тест-кейсы.xlsx”
В файлах:
 	test_authorization_by_code_page_rt.py,
test_authorization_page_rt.py,
test_registration_page_rt.py
 написана реализация тест-кейсов

В файле conftest.py реализована логика запуска браузера и добавлен обработчик, который считывает из командной строки параметр browser_name, а так же language (если сайт поддерживает разные языки)
Браузер объявлется в фикстуре browser и передается в тест как параметр.
Install all requirements: pip3 install -r requirements.txt
Пример: тест запускается с параметром browser_name следующей командой: 
pytest -v -s --browser_name chrome .\test_authorization_page_rt.py
pytest -v -s --browser_name firefox .\test_registration_page_rt.py:
"# SF_Module_28" 
"# SF_Module_28" 
