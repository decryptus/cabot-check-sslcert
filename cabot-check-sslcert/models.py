import datetime
import socket
import ssl

from django.db import models

from cabot.cabotapp.models import StatusCheck, StatusCheckResult


class SslcertStatusCheck(StatusCheck):
    check_name = 'sslcert'
    edit_url_name = 'update-sslcert-check'
    duplicate_url_name = 'duplicate-sslcert-check'
    icon_class = 'glyphicon-transfer'
    host = models.TextField(
        help_text='Host to check.',
    )
    port = models.PositiveIntegerField(
        help_text='Port to check.',
    )
    days = models.PositiveIntegerField(
        help_text='Days before expiration.',
    )

    def ssl_expiry_datetime(self):
        context = ssl.create_default_context()
        conn = context.wrap_socket(
            socket.socket(socket.AF_INET),
            server_hostname = self.host,
        )
        conn.settimeout(self.timeout)

        conn.connect((self.host, self.port))
        ssl_info = conn.getpeercert()

        return datetime.datetime.strptime(ssl_info['notAfter'], r'%b %d %H:%M:%S %Y %Z')

    def _run(self):
        result = StatusCheckResult(status_check=self)

        try:
            remaining = self.ssl_expiry_datetime() - datetime.datetime.utcnow()

            if remaining < datetime.timedelta(days=0):
                raise Exception("Certificate expired %s days ago" % remaining.days)
            elif remaining < datetime.timedelta(days=buffer_days):
                raise Exception("Certificate expires in %s days" % remaining.days)
        except Exception as e:
            result.error = u"{} {} {}".format(e.message, self.host, self.port)
            result.succeeded = False
        else:
            result.succeeded = True

        return result
