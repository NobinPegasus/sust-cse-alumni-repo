from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals



#
# class RockNRollConfig(AppConfig):
#     # ...
#
#     def ready(self):
#         # importing model classes
#         from .models import MyModel  # or...
#         MyModel = self.get_model('MyModel')
#
#         # registering signals with the model's string label
#         pre_save.connect(receiver, sender='app_label.MyModel')
