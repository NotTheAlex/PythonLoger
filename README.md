# PythonLoger

#####Это простейший логер для Python
<p>Его очень просто использовать для этого нужно импортировать класс log и создать экземпляр объекта. Далее просто используем функцию add в которую передаём обычную строку. Логер изначально создает папку (logs или в папку которую вы укажите при инициализации) и в нём файл типа: "currect_data.log", а в нутри разделён на строки типа: "[currect_time] YourText"</p>

<h5>Пример использования</h5>

<pre lang="no-highlight"><code>
```python
from loger import log

l = log(log_folder = 'MyLogs')

l.add ('Test Information')
l.add ('Complete')
```
</code></pre>


<p>Данный скрипт создаст папку MyLogs и поместит туда лог в котором будет примерно так:</p>

<p>[07:19:16] Test Information</p>
<p>[07:19:17] Complete</p>