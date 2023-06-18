# Тестовое задние
## Стратегия тестирования нового функционала

1. Smoke тестирование

Позитивные сценарии:
   - Открыть веб-интерфейс и посмотреть, что все правильно загружается и отображается
   - Ввести корректные данные, нажать кнопку создать и убедиться, что база данных разворачивается

Негативные сценарии:
- Попытка создания базы данных без заполнения обязательных полей, убедиться что ошибка обрабатывается верно

3. Функциональное тестирование
  
  Позитивные сценарии:
   - Проверка, что база данных создалась, и появляется в списке существующих баз данных
   - Проверка, что при создании базы данных с конкретным регионом, у нее установлен выбранный регион
   - Проверка, что у базы данных верно установлено заданное имя
   - Проверка, что у базы данных верно установлен заданный размер
  
  Негативные сценарии:
- Попытка создания базы данных с вписанными в поля недопустимыми символами
- Попытка создания базы данных с именем, которое уже есть в системе

  4. Нефункциональное тестирование
   - Тестирование производительности базы данных с большим объемом данных и проверка времени отклика
   - Тестирование масштабируемости созданием базы данных в условиях высокой нагрузки
   - Тестирование надежности, продолжительной нагрузкой с большим обьемом данных

  ## Автоматизация тестирования API
  
