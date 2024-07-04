# -*- coding: utf-8 -*-
# @Author: pauline
# @Date: 2024/7/1
import functools
import time

import allure


# def ui_failure_screenshot_and_pagesource(func):
#     def inner(*args, **kwargs):
#         # driver = args[0].driver  # 这里的args[0]取到的是TestBaidu()这个对象，而要取到driver还得像下操作一步
#         for arg in args:
#             if hasattr(arg, 'xueqiu'):
#                 driver = arg.xueqiu.driver
#                 break
#         if not driver:
#             raise ValueError('WebDriver instance required for screenshot_on_failure decorator.')
#         try:
#             return func(*args, **kwargs)  # 这里需要return
#         except Exception as e:
#             timestamp = int(time.time())
#             image_path = f'../images/failure_images_{timestamp}.PNG'
#             page_source_path = f'../page_source/failure_pagesource_{timestamp}.html'
#
#             driver.save_screenshot(image_path)
#             with open(page_source_path, 'w', encoding='u8') as f:
#                 f.write(driver.page_source)
#                 allure.attach.file(source=image_path, name="shot", attachment_type=allure.attachment_type.PNG)
#                 allure.attach.file(source=page_source_path, name="pageSource",
#                                    attachment_type=allure.attachment_type.TEXT)
#                 raise e
#
#     return inner


# def ui_success_screenshoot_and_pagesource(func):
#     def inner(*args, **kwargs):
#         # driver = args[0].driver  # 这里的args[0]取到的是TestBaidu()这个对象，而要取到driver还得像下操作一步
#         for arg in args:
#             if hasattr(arg, 'xueqiu'):
#                 driver = arg.xueqiu.driver
#                 break
#         timestamp = int(time.time())
#         image_path = f'../images/success_images_{timestamp}.PNG'
#         page_source_path = f'../page_source/success_pagesource_{timestamp}.html'
#
#         driver.save_screenshot(image_path)
#         with open(page_source_path, 'w', encoding='u8') as f:
#             f.write(driver.page_source)
#             allure.attach.file(source=image_path, name="shot", attachment_type=allure.attachment_type.PNG)
#             allure.attach.file(source=page_source_path, name="pageSource",
#                                attachment_type=allure.attachment_type.TEXT)
#         return func(*args, **kwargs)  # 这里需要return
#
#     return inner


def ui_screenshot_and_pagesource(on_success=False):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            driver = None
            for arg in args:
                if hasattr(arg, 'app'):  # 测试对象
                    driver = arg.app.driver
                    break
            if not driver:
                raise ValueError('WebDriver instance required for screenshot_on_failure decorator.')
            try:
                result = func(*args, **kwargs)
                if on_success:
                    timestamp = int(time.time())
                    image_path = f'../images/success_images_{timestamp}.PNG'
                    page_source_path = f'../page_source/success_pagesource_{timestamp}.html'
                    driver.save_screenshot(image_path)
                    with open(page_source_path, 'w', encoding='u8') as f:
                        f.write(driver.page_source)
                        allure.attach.file(source=image_path, name="shot",
                                           attachment_type=allure.attachment_type.PNG)
                        allure.attach.file(source=page_source_path, name="pageSource",
                                           attachment_type=allure.attachment_type.TEXT)
                return result
            except Exception as e:
                timestamp = int(time.time())
                image_path = f'../images/failure_images_{timestamp}.PNG'
                page_source_path = f'../page_source/failure_pagesource_{timestamp}.html'
                driver.save_screenshot(image_path)
                with open(page_source_path, 'w', encoding='u8') as f:
                    f.write(driver.page_source)
                    allure.attach.file(source=image_path, name="shot", attachment_type=allure.attachment_type.PNG)
                    allure.attach.file(source=page_source_path, name="pageSource",
                                       attachment_type=allure.attachment_type.TEXT)
                raise e

        return inner

    return decorator
