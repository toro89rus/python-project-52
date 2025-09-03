from django.utils.translation import gettext_lazy as _

LOGIN = _("You are logged in")
LOGOUT = _("You've successfully logged out")
LOGIN_REQUIRED = _("You're not authorised. Please login")

USER_CREATED = _("User has been successfully registered")
USER_UPDATED = _("User has been successfully updated")
USER_DELETED = _("User has been successfully deleted")
USER_RESTRICT_UPDATE = _("You can't edit other user")
USER_RESTRICT_DELETE = _("Can't delete, user is being used")

STATUS_CREATED = _("Status has been successfully registered")
STATUS_UPDATED = _("Status has been successfully updated")
STATUS_DELETED = _("Status has been successfully deleted")
STATUS_RESTRICT_DELETE = _("Can't delete, status is being used")

LABEL_CREATED = _("Label has been successfully registered")
LABEL_UPDATED = _("Label has been successfully updated")
LABEL_DELETED = _("Label has been successfully deleted")

TASK_CREATED = _("Task has been successfully registered")
TASK_UPDATED = _("Task has been successfully updated")
TASK_DELETED = _("Task has been successfully deleted")
TASK_RESTRICT_DELETE = _("Only author have permission to delete task")

DELETE_CONFIRM = _("Do you really want to delete %(name)s?")
