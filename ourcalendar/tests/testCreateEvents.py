from ourcalendar.models import Events, OurCalendar
from django.test import TestCase, Client, client

from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.models import User
import datetime


class TestsExcludeImage(TestCase):

    def testSendForm(self):
        date = datetime.datetime.today()
        date2 = datetime.date.today()
        response = self.client.post("/addEvent/", data={"name": "a lowercase title", "description": "vamo q vamo", 
        "date_start":datetime.datetime.now(), "date_end":datetime.datetime.now(), 'access':'PV'})

        self.assertEqual(response.status_code, HTTPStatus.OK)
