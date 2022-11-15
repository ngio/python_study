"""
Desktop notifier app : Python을 이용한 Toast Message 생성
 : https://plyer.readthedocs.io/en/latest/#

jupiter-env  
>>> pip install plyer
"""

from plyer import notification

val_title = '안녕하세요~ newbie! '

val_message = 'Thankyou for reading! Take care!'

notification.notify(title = val_title
                   , message = val_message
                   , app_icon = None
                   , timeout = 10
                   , toast = False)
