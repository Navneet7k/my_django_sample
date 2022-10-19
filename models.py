# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#         app_label  = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#         app_label  = 'auth_group_permissions'


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#         app_label  = 'auth_permission'


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#         app_label  = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#         app_label  = 'auth_user_groups'


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)
#         app_label  = 'auth_user_user_permissions'


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#         app_label  = 'django_admin_log'
        


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#         app_label  = 'django_content_type'


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#         app_label  = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'
#         app_label  = 'django_session'


class LotteryData(models.Model):
    filename = models.CharField(max_length=50, blank=True, null=True)
    lottery_name = models.CharField(max_length=50, blank=True, null=True)
    first_prize = models.CharField(max_length=100, blank=True, null=True)
    consolation_prize = models.CharField(max_length=250, blank=True, null=True)
    second_prize = models.TextField(blank=True, null=True)
    third_prize = models.TextField(blank=True, null=True)
    fourth_prize = models.TextField(blank=True, null=True)
    fifth_prize = models.TextField(blank=True, null=True)
    sixth_prize = models.TextField(blank=True, null=True)
    seventh_prize = models.TextField(blank=True, null=True)
    eighth_prize = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lottery_data'
        app_label = 'lottery_data'

class LotteryNew(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lottery_new'
        app_label = 'lottery_new'

# class TodoApiLottery(models.Model):
#     filename = models.CharField(max_length=180)
#     lottery_name = models.CharField(max_length=180)
#     first_prize = models.CharField(max_length=180)
#     consolation_prize = models.CharField(max_length=500)
#     second_prize = models.CharField(max_length=500)
#     third_prize = models.CharField(max_length=500)
#     fourth_prize = models.CharField(max_length=500)
#     fifth_prize = models.CharField(max_length=500)
#     sixth_prize = models.CharField(max_length=500)
#     seventh_prize = models.CharField(max_length=500)
#     eighth_prize = models.CharField(max_length=500)
#     code = models.CharField(max_length=180)
#     date = models.CharField(max_length=180)

#     class Meta:
#         managed = False
#         db_table = 'todo_api_lottery'
#         app_label = 'todo_api_lottery'