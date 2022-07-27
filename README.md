# Декоратор для обеспечения уникальности экземпляра Celery задачи

Использование декоратора позволяет добиться уникальности экземпляра задачи не зависимо от используемого брокера для Celery

## Использование
Допустим, есть экземпляр Celery, определенный в файле worker.py:
```python
from celery import Celery

celery_worker = Celery(...)
```
Определяем задачу, для которой требуется обеспечить уникальность:
```python
from .worker import celery_worker
from .decorators import unique_task


@celery_worker.task(name='some_task')
@unique_task(celery_worker)
def some_task():
    pass
```