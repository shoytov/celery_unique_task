from functools import wraps
from typing import Callable

from celery import Celery, current_task


def unique_task(celery_worker: Celery):
    def decorator(callback: Callable):
        """
        Обеспечение работы только одной копии задачи celery в моменте.
        """
        @wraps(callback)
        def _wrapper(*args, **kwargs):
            active_queues = celery_worker.control.inspect().active()
            if active_queues:
                for queue in active_queues:
                    for running_task in active_queues[queue]:
                        if callback.__name__ == running_task.get('name') and \
                                current_task.request.id != running_task.get('id'):
                            return

            return callback(*args, **kwargs)

        return _wrapper
    return decorator
