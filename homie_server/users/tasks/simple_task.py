import requests
from time import sleep

from celery import Task


class SimpleTask(Task):
    
    def run(self):
        sleep(3)

        base_url = "http://api.openapi.io/ppurio/1/sendnumber/save/dobestan"
        headers = {
            'x-waple-authorization': 'MTkyMC0xNDEzODU0NTAwMzU3LTllM2VkOTM3LTYwMTEtNGU2Zi1iZWQ5LTM3NjAxMTNlNmYyMg==',
        }

        data = {
            "send_phone": "01089617633",
            "dest_phone": "01089617633",
            "msg_body": "새로운 회원 가입",
        }

        requests.post(
            base_url,
            headers=headers,
            data=data,
        )
