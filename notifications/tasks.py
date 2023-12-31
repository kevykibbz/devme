from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from manager.models import BroadcastNotification
import json
from celery import Celery, states
from celery.exceptions import Ignore
import asyncio


    
@shared_task(bind = True)
def broadcast_notification(self, data ,*args , **kwargs):
    print('args:',args)
    print('args:',args)
    try:
        notification = BroadcastNotification.objects.filter(id = int(data))
        if len(notification)>0:
            notification = notification.first()
            channel_layer = get_channel_layer()
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(channel_layer.group_send(
                "notification_broadcast",
                {
                    'type': 'send_notification',
                    'profile': json.dumps(notification.profile_pic),
                    'message': json.dumps(notification.message),
                    'time': json.dumps(notification.broadcast_on)
                }))
            notification.sent = True
            notification.save()
            return 'Done'

        else:
            self.update_state(
                state = 'FAILURE',
                meta = {'exe': "Not Found"}
            )

            raise Ignore()

    except:
        self.update_state(
                state = 'FAILURE',
                meta = {
                        'exe': "Failed"
                        # 'exc_type': type(ex).__name__,
                        # 'exc_message': traceback.format_exc().split('\n')
                        # 'custom': '...'
                    }
            )

        raise Ignore()