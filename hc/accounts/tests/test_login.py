from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from hc.api.models import Check
from hc.accounts.models import Profile

class LoginTestCase(TestCase):

    def test_it_sends_link(self):
        check = Check()
        check.save()

        session = self.client.session
        session["welcome_code"] = str(check.code)
        session.save()

        form = {"email": "alice@example.org"}

        r = self.client.post("/accounts/login/", form)
        assert r.status_code == 302

        self.assertEqual(User.objects.count(), 1)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'Log in to healthchecks.io')

        self.assertIn("Hello,\n\nTo log into healthchecks.io, please open the link below:", mail.outbox[0].body)

    def test_it_pops_bad_link_from_session(self):
        self.client.session["bad_link"] = True
        self.client.get("/accounts/login/")
        assert "bad_link" not in self.client.session
