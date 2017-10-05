from django.contrib import admin

from .models import Transaction, Wallet


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'wallet_id', 'value', 'running_balance', 'created_at')
    raw_id_fields = ('wallet', )

    def get_walled_id(self, obj):
        return obj.id


class WalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'current_balance', 'created_at')
    raw_id_fields = ('user', )


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Wallet, WalletAdmin)
