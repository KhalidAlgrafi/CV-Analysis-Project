from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = "Create default user groups: Admin and End User. Admin gets all permissions."

    def handle(self, *args, **options):
        admin_group, _ = Group.objects.get_or_create(name="Admin")
        end_group, _ = Group.objects.get_or_create(name="End User")

        # Assign all permissions to Admin group for convenience (superuser still bypasses this)
        admin_perms = Permission.objects.all()
        admin_group.permissions.set(admin_perms)

        self.stdout.write(self.style.SUCCESS("Ensured groups: 'Admin', 'End User' (Admin has all permissions)"))

