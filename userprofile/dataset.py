from crum import get_current_user

from newsletter.models import Template

from common.classes.DataMigration import DataMigration


class UserProfileData:

    def __init__(self):

        self.saveTemplate()

    def saveTemplate(self):

        self.saving(1, 'Template', Template, Template(
            unique_name="user.email.verification",
            subject="Get Started",
            short_body="Get Started",
            body="Dear {{ user.first_name }},<br><br>Please click on the link to confirm your registration.<br><br><a href='{{ email_verification_link }}'>{{ email_verification_link }}</a><br><br>OR Copy<br><br>{{ email_verification_link }}<br><br>Thank You"
        )
        )

        self.saving(2, 'Template', Template, Template(
            unique_name="user.login.notification",
            subject="Someone has login using ({{ user.username }})",
            short_body="Someone has login using ({{ user.username }})",
            body="Dear {{ user.first_name }},<br><br>Someone has login using ({{ user.username }}). <br><br><b>Browser:</b>{{ browser_str }} <br><br><b>IP:</b>{{ country.ip }}<br><b>Contitent:</b>{{ country.continent_name }}<br><b>Country:</b>{{ country.country_name }}<br><b>Region:</b>{{ country.region_name }}<br><b>City:</b>{{ country.city }}<br><br>Thank You"
        )
        )

        self.saving(3, 'Template', Template, Template(
            unique_name="user.activity.notification",
            subject="Someone has {{ activity }} using ({{ user.username }})",
            short_body="Someone has {{ activity }} using ({{ user.username }})",
            body="Dear {{ user.first_name }},<br><br>Someone has {{ activity }} using ({{ user.username }}). <br><br><b>Browser:</b>{{ browser_str }} <br><br><b>IP:</b>{{ country.ip }}<br><b>Contitent:</b>{{ country.continent_name }}<br><b>Country:</b>{{ country.country_name }}<br><b>Region:</b>{{ country.region_name }}<br><b>City:</b>{{ country.city }}<br><br>Thank You"
        )
        )

        self.saving(4, 'Template', Template, Template(
            unique_name="user.email.verification.by.code",
            subject="Get Started",
            short_body="Get Started",
            body="Dear {{ user.first_name }},<br><br>Please enter the following code to verify your account.<br><br><b>Code:</b>{{ code }}<br><br>Thank You"
        )
        )



    def saving(self, key, modelname, Modelpass, Record):
        
        data_migration = DataMigration()

        data_migration.saveRecord(key, 'userprofile', modelname, Modelpass, Record)
