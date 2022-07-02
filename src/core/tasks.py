from __future__ import absolute_import, unicode_literals
from celery import shared_task, Celery
from celery.utils.log import get_task_logger
from src.car_dealership.managers.buying_cars import buying_cars_process
from src.car_dealership.managers.base_manager import start


logger = get_task_logger(__name__)
app = Celery('config', broker='redis://127.0.0.1:6379/0')


@shared_task
def buy_car():
    start_buying = buying_cars_process.buying_cars()
    logger.info('Buying cars')


@shared_task
def update_cars_info():
    update_cars = start.create_car()
    logger.info('Updating cars')


@shared_task
def update_dealer_info():
    update_dealers = start.create_dealer()
    logger.info('Updating dealers')
